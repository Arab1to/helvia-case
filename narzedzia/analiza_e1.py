#!/usr/bin/env python3
"""Analiza E1 na pliku organizatora (HITL_Etap_1.xlsx) — odtwarza liczby z 01_etap1_diagnoza/analiza-E1.md.

Drukuje WYŁĄCZNIE agregaty (per klient / dział / proces) — wynik można wkleić do Claude.
Dane osobowe (maile z ankiety i listy pracowników) służą tylko do złączenia ankieta → dział.

Użycie:  python3 narzedzia/analiza_e1.py dane/organizator/HITL_Etap_1.xlsx
Wymaga:  pip install pandas openpyxl
"""
import sys
import warnings

import pandas as pd

warnings.filterwarnings("ignore")
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 30)


def t2(s):
    return (s >= 4).mean()


def main(f):
    kl = pd.read_excel(f, "Klienci").iloc[:14]
    hist = pd.read_excel(f, "Historia miesieczna")
    pipe = pd.read_excel(f, "Pipeline")
    wol = pd.read_excel(f, "Wolumeny klient proces")
    emp = pd.read_excel(f, "Lista pracowników szczegółowo")
    ank = pd.read_excel(f, "Ankieta szczegółowo")
    dz = pd.read_excel(f, "Działy", header=None)

    rev, marza, kary = kl["Przychód 12M (PLN)"].sum(), kl["Marża 12M (PLN)"].sum(), kl["Kary SLA 12M (PLN)"].sum()
    print("## Firma")
    print(f"Przychód {rev/1e6:.2f} mln | EBIT {marza/1e6:.2f} mln ({marza/rev:.2%}) | kary SLA {kary/1e6:.2f} mln = {kary/marza:.0%} EBIT"
          f" | marża bez kar {(marza+kary)/rev:.1%} | top 3 klientów {kl['Przychód 12M (PLN)'].nlargest(3).sum()/rev:.0%}")
    print(f"Koszty osobowe {emp['Koszt miesięczny (PLN)'].sum()*12/1e6:.2f} mln/rok | pozostałe koszty "
          f"{(kl['Koszt obsługi 12M (PLN)'].sum()-emp['Koszt miesięczny (PLN)'].sum()*12)/1e6:.2f} mln/rok")
    print(f"Kontrola: kary w 'Historia miesieczna' = {hist['Kary SLA (PLN)'].sum()/1e6:.2f} mln (vs {kary/1e6:.2f}), "
          f"przychód = {hist['Przychód (PLN)'].sum()/1e6:.2f} mln, reklamacje = {hist['Reklamacje'].sum()} (vs {kl['Reklamacje 12M'].sum()})")

    godz = wol.groupby("Klient")["Śr. godziny / mies."].sum() * 12
    k = kl.set_index("Klient")
    k["Marża przed karami %"] = (k["Marża 12M (PLN)"] + k["Kary SLA 12M (PLN)"]) / k["Przychód 12M (PLN)"] * 100
    k["Kary % przych."] = k["Kary SLA 12M (PLN)"] / k["Przychód 12M (PLN)"] * 100
    k["SLA śr. 12M"] = hist.groupby("Klient")["SLA realizacja (%)"].mean()
    k["FTE-ekw."] = godz / 12 / 160
    k["Przychód / h"] = k["Przychód 12M (PLN)"] / godz
    k["Rekl./1000 oper."] = k["Reklamacje 12M"] / (wol.groupby("Klient")["Śr. wolumen / mies."].sum() * 12) * 1000
    print("\n## Klienci")
    print(k[["Koniec kontraktu", "Udział w przychodzie 12M (%)", "Marża 12M (%)", "Marża przed karami %", "Kary SLA 12M (PLN)",
             "Kary % przych.", "SLA śr. 12M", "Dynamika wolumenu 12M (%)", "Wskaźnik satysfakcji / NPS", "FTE-ekw.", "Przychód / h",
             "Rekl./1000 oper."]].round(1).to_string())
    do = k[k["Koniec kontraktu"] <= "2027-03-31"]
    print(f"Kontrakty do 31.03.2027: {', '.join(do.index)} = {do['Przychód 12M (PLN)'].sum()/1e6:.2f} mln ({do['Przychód 12M (PLN)'].sum()/rev:.1%})")
    print(f"Przychód / h średnio: {rev/godz.sum():.0f} zł; godziny bezpośrednie = {godz.sum()/12/160:.0f} FTE-ekw. z 720")

    # Działy: bloki w arkuszu (dane od wiersza 4, 15, 26, 37 — numeracja Excela)
    def blok(r0, cols):
        b = dz.iloc[r0 - 1:r0 + 7, 1:1 + len(cols)]
        b.columns = cols
        return b.set_index("Dział")
    d = blok(4, ["Dział", "Przychód", "OPEX", "Marża działu"]).join(
        blok(15, ["Dział", "FTE", "Produktywność", "Rotacja", "Nadgodziny"])).join(
        blok(26, ["Dział", "Automatyzacja", "AHT"])).join(blok(37, ["Dział", "Błędy", "SLA", "Ocena"]))
    d = d.apply(pd.to_numeric, errors="coerce")  # AHT zarządu zapisane jako tekst „67,3 min” → brak
    a = ank.merge(emp[["E-mail (ID)", "Dział"]], left_on="E-mail (ID respondenta)", right_on="E-mail (ID)")
    s = a.groupby("Dział").agg(
        n=("Q01", "size"), eNPS=("Q02", lambda x: ((x >= 9).mean() - (x <= 6).mean()) * 100),
        Q09_obciaz_ok=("Q09", t2), Q14_zostaje=("Q14", t2), Q14_odchodzi=("Q14", lambda x: (x <= 2).mean()),
        Q19_obawa_zadania=("Q19", t2), Q20_obawa_etat=("Q20", t2), Q21_komunikacja=("Q21", t2), Q22_chce_szkolen=("Q22", t2),
        Q16_szkolenie=("Q16", lambda x: (x == "Tak").mean()), Q24_powtarzalne60=("Q24", lambda x: x.isin(["60-80%", "powyżej 80%"]).mean()))
    e = emp.groupby("Dział").agg(koszt_etatu=("Koszt miesięczny (PLN)", "mean"), junior=("Poziom", lambda x: (x == "Junior").mean()),
                                 staz_lt1=("Staż (lata)", lambda x: (x < 1).mean()))
    print("\n## Działy (dane operacyjne)")
    print(d.round(3).to_string())
    print(f"Mediana rotacji {d['Rotacja'].median():.1%}; błędy razem {d['Błędy'].sum()}; r(rotacja, SLA) = {d['Rotacja'].corr(d['SLA']):.2f}"
          f" (bez Obsługi Klienta {d.drop('Obsługa Klienta')['Rotacja'].corr(d.drop('Obsługa Klienta')['SLA']):.2f})")
    print("\n## Działy (ankieta — odsetek ocen 4–5, zwrot ankiet; lista pracowników)")
    s["zwrot"] = s["n"] / emp.groupby("Dział").size()
    print(s.join(e).round(2).to_string())
    print(f"Firma: eNPS {((a.Q02 >= 9).mean() - (a.Q02 <= 6).mean())*100:.0f}, Q21 {t2(a.Q21):.1%}, Q22 {t2(a.Q22):.0%}, "
          f"Q16 {(a.Q16 == 'Tak').mean():.0%}, Q20 {t2(a.Q20):.0%}; pracownicy < 35 lat "
          f"{emp['Grupa wiekowa'].isin(['poniżej 25', '25-34']).mean():.0%}")

    print("\n## Procesy (top 10 wg FTE-ekw.)")
    p = wol.groupby(["ID procesu", "Proces", "Dział"]).agg(godz=("Śr. godziny / mies.", "sum"), wol=("Śr. wolumen / mies.", "sum")).reset_index()
    p["FTE-ekw."] = p.godz / 160
    p["min/sprawę"] = p.godz * 60 / p.wol
    print(p.sort_values("godz", ascending=False).head(10).round(1).to_string(index=False))
    print("\nFTE-ekw. klientów per dział (NORDA / Lumea):")
    print(wol[wol.Klient.isin(["NORDA Logistics", "Lumea Telecom"])].pivot_table(
        index="Dział", columns="Klient", values="Śr. godziny / mies.", aggfunc="sum").div(160).round(1).to_string())

    print("\n## Pipeline (arkusz ukryty)")
    pipe["EV"] = pipe["Roczna wartość (PLN)"] * pipe["Szansa (%)"] / 100
    pipe["FTE ważone"] = pipe["FTE wymagane"] * pipe["Szansa (%)"] / 100
    print(pipe.groupby("Dział")[["Roczna wartość (PLN)", "EV", "FTE wymagane", "FTE ważone"]].sum().round(1).to_string())
    print(f"Razem: {len(pipe)} szans, EV {pipe.EV.sum()/1e6:.2f} mln, FTE {pipe['FTE wymagane'].sum():.1f} (ważone {pipe['FTE ważone'].sum():.1f}); "
          f"Dashboard liczy S-01…S-09: EV {pipe.EV.iloc[:9].sum()/1e6:.2f} mln, FTE {pipe['FTE wymagane'].iloc[:9].sum():.1f}; "
          f"przychód/FTE w pipeline {pipe['Roczna wartość (PLN)'].sum()/pipe['FTE wymagane'].sum()/1e3:.0f} tys. vs {rev/720/1e3:.0f} tys. dziś")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
