#!/usr/bin/env python3
"""Generuje excel/HELVIA_szablony.xlsx — wszystkie puste tabele z playbooka, z formułami.

Formuły są zapisane w notacji EN (tak przechowuje je plik .xlsx); Excel PL wyświetli je
automatycznie po polsku (SUMA, JEŻELI, …). Komórki do wypełnienia są żółte.

Użycie:  python3 narzedzia/generuj_szablony.py [ścieżka_wyjściowa.xlsx]
"""
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.workbook.defined_name import DefinedName

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "excel" / "HELVIA_szablony.xlsx"

HDR = PatternFill("solid", fgColor="1F3A5F")
HDR_FONT = Font(color="FFFFFF", bold=True)
INPUT = PatternFill("solid", fgColor="FFF6D5")
CALC = PatternFill("solid", fgColor="EEF3F8")
RED = PatternFill("solid", fgColor="F4C7C3")
AMB = PatternFill("solid", fgColor="FCE8B2")
GRN = PatternFill("solid", fgColor="B7E1CD")
THIN = Side(style="thin", color="C8CED6")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
BOLD = Font(bold=True)
TITLE = Font(bold=True, size=14, color="1F3A5F")
NOTE = Font(italic=True, color="666666")

wb = Workbook()


def name(n, ref):
    dn = DefinedName(n, attr_text=ref)
    try:
        wb.defined_names[n] = dn          # openpyxl >= 3.1
    except TypeError:
        wb.defined_names.append(dn)       # starsze openpyxl


def sheet(title, heading, note=None):
    ws = wb.create_sheet(title)
    ws["A1"] = heading
    ws["A1"].font = TITLE
    if note:
        ws["A2"] = note
        ws["A2"].font = NOTE
    return ws


def table(ws, row, headers, nrows, widths=None, input_cols=(), formulas=None, labels=None):
    """Nagłówek w wierszu `row`, potem nrows wierszy. formulas: {kolumna(1-based): lambda r: '=...'}"""
    for j, h in enumerate(headers, 1):
        c = ws.cell(row=row, column=j, value=h)
        c.fill, c.font, c.border = HDR, HDR_FONT, BOX
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for i in range(nrows):
        r = row + 1 + i
        for j in range(1, len(headers) + 1):
            c = ws.cell(row=r, column=j)
            c.border = BOX
            if labels and j == 1 and i < len(labels):
                c.value = labels[i]
            if j in input_cols:
                c.fill = INPUT
            if formulas and j in formulas:
                c.value = formulas[j](r)
                c.fill = CALC
    if widths:
        for j, w in enumerate(widths, 1):
            ws.column_dimensions[ws.cell(row=row, column=j).column_letter].width = w
    ws.row_dimensions[row].height = 32
    return row + 1, row + nrows  # pierwszy i ostatni wiersz danych


def rag_format(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Czerwony"'], fill=RED))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Żółty"'], fill=AMB))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Zielony"'], fill=GRN))


def kv(ws, row, label, value, nm=None, fmt=None, inp=False, note=None):
    ws.cell(row=row, column=1, value=label).border = BOX
    c = ws.cell(row=row, column=2, value=value)
    c.border = BOX
    c.fill = INPUT if inp else CALC
    if fmt:
        c.number_format = fmt
    if nm:
        name(nm, f"'{ws.title}'!$B${row}")
        ws.cell(row=row, column=3, value=nm).font = NOTE
    if note:
        ws.cell(row=row, column=4, value=note).font = NOTE


# ---------------------------------------------------------------- Start
ws = wb.active
ws.title = "Start"
ws["A1"] = "HELVIA — szablony z playbooka"
ws["A1"].font = TITLE
ws["A2"] = "Żółte = do wypełnienia, niebieskie = formuły. Excel jest jedynym źródłem prawdy dla liczb. Pliki robocze: HELVIA_E1_v1.xlsx …"
ws["A2"].font = NOTE
ws["A4"], ws["B4"], ws["C4"], ws["D4"] = "Liczby bazowe", "Wartość", "Nazwa", "Wzór / źródło"
for c in ("A4", "B4", "C4", "D4"):
    ws[c].fill, ws[c].font = HDR, HDR_FONT
kv(ws, 5, "Przychód LTM (mln zł)", 114.93, "Przychod", "0.00", inp=True, note="z opisu case'u")
kv(ws, 6, "Marża operacyjna", 0.084, "Marza", "0.0%", inp=True, note="z opisu case'u")
kv(ws, 7, "Pracownicy", 720, "Pracownicy", "0", inp=True, note="z opisu case'u")
kv(ws, 8, "Klienci", 14, "Klienci", "0", inp=True, note="z opisu case'u")
kv(ws, 9, "EBIT (mln zł)", "=Przychod*Marza", "EBIT", "0.00", note="przychód × marża")
kv(ws, 10, "Przychód / pracownik (tys. zł)", "=Przychod/Pracownicy*1000", None, "0.0")
kv(ws, 11, "EBIT / pracownik (tys. zł)", "=EBIT/Pracownicy*1000", None, "0.0")
kv(ws, 12, "Średni przychód / klient (mln zł)", "=Przychod/Klienci", None, "0.00")
kv(ws, 13, "1 pp rabatu (mln zł)", "=Przychod*0.01", "Rabat_1pp", "0.00")
kv(ws, 14, "1 pp rabatu jako % EBIT", "=Rabat_1pp/EBIT", None, "0.0%")
ws["A16"] = "Sanity-check"
ws["A16"].font = BOLD
kv(ws, 17, "Σ FTE działów (E1_Dzialy)", "=SUM(E1_Dzialy!B5:B12)", None, "0", note="musi = 720")
kv(ws, 18, "Σ przychodów klientów (E1_Klienci)", "=SUM(E1_Klienci!B5:B18)", None, "0.00", note="musi = 114,93")
kv(ws, 19, "Status", '=IF(AND(B17=Pracownicy,ABS(B18-Przychod)<0.01),"OK — sumy się domykają","SPRAWDŹ z mentorem")')
ws.column_dimensions["A"].width = 38
ws.column_dimensions["B"].width = 16
ws.column_dimensions["C"].width = 14
ws.column_dimensions["D"].width = 30
ws["A21"] = "Progi RAG [ZAŁOŻENIE] — zmieńcie tutaj, formuły w E1 się przeliczą"
ws["A21"].font = BOLD
kv(ws, 22, "SLA: czerwony gdy poniżej umowy o więcej niż (pp)", 3, "Prog_SLA_pp", "0.0", inp=True)
kv(ws, 23, "Rotacja: czerwony gdy > X × mediana", 1.5, "Prog_rot", "0.0", inp=True)
kv(ws, 24, "Udział klienta: czerwony gdy >", 0.15, "Prog_udz_R", "0%", inp=True)
kv(ws, 25, "Udział klienta: żółty gdy ≥", 0.07, "Prog_udz_Y", "0%", inp=True)

# ---------------------------------------------------------------- E1 działy
ws = sheet("E1_Dzialy", "Szablon A — 8 działów", "SLA vs umowa w pp (ujemne = poniżej umowy). Rotacja i obawa w % (np. 0,18).")
heads = ["Dział", "FTE", "Obciążenie (h/FTE)", "Wydajność", "SLA vs umowa (pp)", "Rotacja %", "Ankieta: obawa przed AI %",
         "Sygnał rotacja", "Sygnał SLA", "Sygnał łączny"]
f, l = 5, 12
first, last = table(ws, 4, heads, 8, [24, 8, 12, 11, 12, 10, 14, 13, 12, 13], input_cols=range(1, 8),
                    labels=["Finanse i księgowość", "HR i payroll", "Obsługa klienta", "IT", "Logistyka", "Administracja",
                            "[dział 7 z Excela]", "[dział 8 z Excela]"],
                    formulas={
                        8: lambda r: f'=IF(F{r}="","",IF(F{r}>Prog_rot*MEDIAN($F${f}:$F${l}),"Czerwony",IF(F{r}>MEDIAN($F${f}:$F${l}),"Żółty","Zielony")))',
                        9: lambda r: f'=IF(E{r}="","",IF(E{r}<-Prog_SLA_pp,"Czerwony",IF(E{r}<0,"Żółty","Zielony")))',
                        10: lambda r: f'=IF(AND(H{r}="",I{r}=""),"",IF(OR(H{r}="Czerwony",I{r}="Czerwony"),"Czerwony",IF(OR(H{r}="Żółty",I{r}="Żółty"),"Żółty","Zielony")))',
                    })
for r in range(first, last + 1):
    ws[f"F{r}"].number_format = ws[f"G{r}"].number_format = "0.0%"
ws.cell(row=13, column=1, value="Suma / średnia").font = BOLD
ws["B13"] = f"=SUM(B{f}:B{l})"
ws["C13"] = f"=AVERAGE(C{f}:C{l})"
ws["E13"] = f"=AVERAGE(E{f}:E{l})"
ws["F13"] = f"=MEDIAN(F{f}:F{l})"
ws["G13"] = f"=AVERAGE(G{f}:G{l})"
ws["F13"].number_format = ws["G13"].number_format = "0.0%"
ws["H13"] = "(F13 = mediana)"
ws["H13"].font = NOTE
ws["A15"], ws["B15"] = "Σ FTE = 720?", '=IF(B13=Pracownicy,"OK","SPRAWDŹ")'
ws["A16"], ws["B16"] = "Korelacja r: rotacja × SLA", f'=IFERROR(CORREL(F{f}:F{l},E{f}:E{l}),"")'
ws["A17"], ws["B17"] = "Działy w czerwieni", f'=COUNTIF(J{f}:J{l},"Czerwony")'
ws["A18"] = "Przy 8 działach r jest kruche — pokażcie wykres punktowy i potwierdźcie ankietą (triangulacja)."
ws["A18"].font = NOTE
ws["B16"].number_format = "0.00"
rag_format(ws, f"H{f}:J{l}")

# ---------------------------------------------------------------- E1 klienci
ws = sheet("E1_Klienci", "Szablon B — 14 klientów",
           "Przychód w mln zł, marża i udziały w %, SLA vs umowa w pp. Skumulowany % liczy się niezależnie od kolejności wierszy.")
f, l = 5, 18
heads = ["Klient", "Przychód (mln zł)", "Udział %", "Skumulowany % (Pareto)", "Ranking", "Marża %", "SLA vs umowa (pp)",
         "Presja cenowa / ryzyko odejścia", "Główny dział", "Sygnał"]
table(ws, 4, heads, 14, [10, 12, 10, 14, 9, 10, 12, 18, 18, 12], input_cols=(1, 2, 6, 7, 8, 9),
      labels=[f"K{i}" for i in range(1, 15)],
      formulas={
          3: lambda r: f'=IF(B{r}="","",B{r}/SUM($B${f}:$B${l}))',
          4: lambda r: f'=IF(B{r}="","",SUMIF($B${f}:$B${l},">="&B{r})/SUM($B${f}:$B${l}))',
          5: lambda r: f'=IF(B{r}="","",RANK(B{r},$B${f}:$B${l}))',
          10: lambda r: (f'=IF(B{r}="","",IF(OR(F{r}<0,F{r}<0.5*AVERAGE($F${f}:$F${l}),G{r}<-Prog_SLA_pp,C{r}>Prog_udz_R),"Czerwony",'
                         f'IF(OR(F{r}<Marza,G{r}<0,C{r}>=Prog_udz_Y),"Żółty","Zielony")))'),
      })
for r in range(f, l + 1):
    for col in "CDF":
        ws[f"{col}{r}"].number_format = "0.0%"
ws.cell(row=19, column=1, value="Suma").font = BOLD
ws["B19"] = f"=SUM(B{f}:B{l})"
ws["C19"] = f"=SUM(C{f}:C{l})"
ws["C19"].number_format = "0%"
ws["A21"], ws["B21"] = "Σ = 114,93?", '=IF(ABS(B19-Przychod)<0.01,"OK","SPRAWDŹ")'
ws["A22"], ws["B22"] = "Top 3 = % przychodu", f'=IFERROR((LARGE(B{f}:B{l},1)+LARGE(B{f}:B{l},2)+LARGE(B{f}:B{l},3))/B19,"")'
ws["A23"], ws["B23"] = "Klienci do 80% przychodu", f'=COUNTIF(D{f}:D{l},"<=0.8")'
ws["B22"].number_format = "0.0%"
rag_format(ws, f"J{f}:J{l}")
ws["A25"] = "Synteza: „HELVIA traci [X mln zł / pp marży], bo w [dział] rotacja [Y%] i SLA [Z% vs W% w umowie] uderzają w klientów generujących [N%] przychodu.”"
ws["A25"].font = NOTE

# ---------------------------------------------------------------- E2 pipeline
ws = sheet("E2_Pipeline", "Krok 1 — Pipeline i test pojemności",
           "Pytanie kontrolne: czy uwolnione przez AI FTE (E3) pokryją lukę FTE? Jeśli tak — „AI finansuje wzrost bez zwolnień”.")
f, l = 5, 14
heads = ["Kontrakt", "Wartość roczna (mln zł)", "Prawdop. %", "EV = wartość × p", "FTE potrzebne", "Dział realizujący",
         "Rotacja działu", "FTE dostępne w dziale", "Luka FTE"]
table(ws, 4, heads, 10, [12, 14, 11, 14, 12, 20, 12, 14, 10], input_cols=(1, 2, 3, 5, 6, 7, 8),
      labels=[f"P{i}" for i in range(1, 11)],
      formulas={4: lambda r: f'=IF(B{r}="","",B{r}*C{r})',
                9: lambda r: f'=IF(E{r}="","",E{r}-H{r})'})
for r in range(f, l + 1):
    ws[f"C{r}"].number_format = ws[f"G{r}"].number_format = "0%"
ws.cell(row=15, column=1, value="Suma").font = BOLD
ws["B15"] = f"=SUM(B{f}:B{l})"
ws["D15"] = f"=SUMPRODUCT(B{f}:B{l},C{f}:C{l})"
ws["E15"] = f"=SUM(E{f}:E{l})"
ws["I15"] = f"=SUM(I{f}:I{l})"
name("EV_pipeline", "'E2_Pipeline'!$D$15")
name("FTE_pipeline", "'E2_Pipeline'!$E$15")
ws["A17"], ws["B17"] = "FTE uwolnione przez AI (z E3)", "=FTE_uwolnione"
ws["A18"], ws["B18"] = "Luka FTE po AI", "=FTE_pipeline-FTE_uwolnione"
ws["A19"], ws["B19"] = "Wniosek", '=IF(B18<=0,"AI pokrywa lukę → AI finansuje wzrost bez zwolnień","Luka zostaje → rekrutacja / priorytetyzacja kontraktów")'

# ---------------------------------------------------------------- E2 macierz
ws = sheet("E2_Macierz", "Krok 2 — Macierz kierunków (ocena 1–5)",
           "Wagi to [ZAŁOŻENIE] — pokażcie je jury jawnie. Kolumna F sprawdza, czy zwycięzca wygrywa przy wagach 25/25/25/25.")
heads = ["Kryterium", "Waga", "Waga alt.", "A. Jakość: naprawa SLA w działach czerwonych",
         "B. Efektywność: automatyzacja back-office", "C. Wzrost: FTE do pipeline'u + oferta premium"]
table(ws, 4, heads, 4, [34, 9, 9, 24, 24, 24], input_cols=(2, 3, 4, 5, 6),
      labels=["Wpływ na EBIT w 12 mies.", "Ryzyko: SLA, kompetencje, opór (5 = niskie ryzyko)", "Wykonalność w 12 mies.",
              "Trójkąt Dobrostanu"])
for r, w in zip(range(5, 9), (0.30, 0.20, 0.25, 0.25)):
    ws[f"B{r}"], ws[f"C{r}"] = w, 0.25
    ws[f"B{r}"].number_format = ws[f"C{r}"].number_format = "0%"
ws["A9"] = "Wynik ważony (1–5)"
ws["A10"] = "Wynik przy wagach alt."
ws["A9"].font = ws["A10"].font = BOLD
for col in "DEF":
    ws[f"{col}9"] = f'=IFERROR(SUMPRODUCT({col}5:{col}8,$B$5:$B$8)/SUM($B$5:$B$8),"")'
    ws[f"{col}10"] = f'=IFERROR(SUMPRODUCT({col}5:{col}8,$C$5:$C$8)/SUM($C$5:$C$8),"")'
    ws[f"{col}9"].fill = ws[f"{col}10"].fill = CALC
    ws[f"{col}9"].number_format = ws[f"{col}10"].number_format = "0.00"
ws["A12"], ws["B12"] = "Zwycięzca (wagi bazowe)", '=IFERROR(INDEX($D$4:$F$4,MATCH(MAX(D9:F9),D9:F9,0)),"")'
ws["A13"], ws["B13"] = "Zwycięzca (wagi alt.)", '=IFERROR(INDEX($D$4:$F$4,MATCH(MAX(D10:F10),D10:F10,0)),"")'
ws["A14"], ws["B14"] = "Odporny na wagi?", '=IF(B12="","",IF(B12=B13,"TAK — pokażcie to jury","NIE — wybór zależy od wag, uzasadnijcie wagi"))'
ws["A16"] = "„Wybieramy [X] kosztem [Y], ponieważ [liczba z E1/E2]. Wracamy do [Y], gdy [warunek mierzalny, np. SLA ≥ umowa przez 2 kwartały].”"
ws["A16"].font = NOTE

# ---------------------------------------------------------------- E2 opcje cenowe
ws = sheet("E2_Opcje_cenowe", "Krok 3 — Warunki wobec klientów",
           "Przykłady to [ZAŁOŻENIE] — podstawcie dane z Excela. Utratę klienta liczcie marżą pokrycia, nie 8,4%.")
ws["A4"] = "Parametry"
ws["A4"].font = BOLD
kv(ws, 5, "Kary SLA unikane rocznie (mln zł)", None, "Kary_SLA", "0.00", inp=True, note="z Excela")
kv(ws, 6, "Zweryfikowana oszczędność AI (mln zł/rok)", 2.0, "Oszczednosc_AI", "0.00", inp=True, note="[ZAŁOŻENIE] przykład")
kv(ws, 7, "Udział klienta w oszczędności s", 0.5, "Udzial_klienta", "0%", inp=True, note="[ZAŁOŻENIE] przykład")
kv(ws, 8, "Rabat warunkowy d", 0.02, "Rabat_war", "0.0%", inp=True)
kv(ws, 9, "Przychód klienta z rabatem warunkowym (mln zł)", 8.2, "Przychod_klienta", "0.00", inp=True, note="średni klient")
kv(ws, 10, "Przychód premium AI (mln zł/rok)", None, "Przychod_premium", "0.00", inp=True, note="[ZAŁOŻENIE] wycena z mentorem")
kv(ws, 11, "Marża na premium", None, "Marza_premium", "0%", inp=True)
kv(ws, 12, "Rabat bezwarunkowy (antywzorzec)", 0.02, "Rabat_bezw", "0.0%", inp=True)
kv(ws, 13, "Marża pokrycia klienta", None, "Marza_pokrycia", "0%", inp=True, note="zapytać mentora o strukturę kosztów")
heads = ["Opcja", "Mechanizm", "Wpływ na EBIT (mln zł)", "% EBIT", "Dla klienta", "Ryzyko"]
first, _ = table(ws, 15, heads, 5, [34, 34, 14, 10, 26, 34])
rows = [
    ("a) Ceny bez zmian, wyższy SLA", "Ta sama cena, szybciej i lepiej", "=IF(Kary_SLA=\"\",0,Kary_SLA)", "Jakość, przewidywalność", "Klient czuje, że nie dzieli się korzyścią"),
    ("b) Gain-sharing", "Klient dostaje s% zweryfikowanej oszczędności po spełnieniu KPI", "=(1-Udzial_klienta)*Oszczednosc_AI", "Realny udział w AI", "Spór o metodę pomiaru"),
    ("c) Rabat warunkowy", "d% za dłuższy kontrakt / wolumen / zgodę na AI", "=-Rabat_war*Przychod_klienta", "Niższa cena teraz", "Efekt domina u innych klientów"),
    ("d) Usługi premium AI", "Nowa linia: analityka, raporty, 24/7", "=IF(Przychod_premium=\"\",0,Przychod_premium*Marza_premium)", "Nowa wartość", "Kompetencje, czas wdrożenia"),
    ("❌ Rabat bezwarunkowy (antywzorzec)", "−d pp na całej bazie", "=-Rabat_bezw*Przychod", "Krótka radość", "Niszczy marżę — pokażcie jako odrzuconą opcję"),
]
for i, (o, m, fx, k, ry) in enumerate(rows):
    r = first + i
    ws[f"A{r}"], ws[f"B{r}"], ws[f"C{r}"], ws[f"E{r}"], ws[f"F{r}"] = o, m, fx, k, ry
    ws[f"D{r}"] = f"=C{r}/EBIT"
    ws[f"C{r}"].number_format = "0.00"
    ws[f"D{r}"].number_format = "0.0%"
    ws[f"C{r}"].fill = ws[f"D{r}"].fill = CALC
    for col in "ABEF":
        ws[f"{col}{r}"].alignment = Alignment(wrap_text=True, vertical="top")
ws.conditional_formatting.add(f"C{first}:D{first+4}", CellIsRule(operator="lessThan", formula=["0"], fill=RED))
ws.conditional_formatting.add(f"C{first}:D{first+4}", CellIsRule(operator="greaterThan", formula=["0"], fill=GRN))
ws["A22"], ws["B22"] = "Próg: przychód, który rabat bezwarunkowy musiałby uratować (mln zł)", '=IFERROR(Rabat_bezw*Przychod/Marza_pokrycia,"podaj marżę pokrycia")'
ws["B22"].number_format = "0.00"

# ---------------------------------------------------------------- E3 scoring
ws = sheet("E3_Scoring", "Część I — scoring procesów (1–5)",
           "1 = bardzo nisko, 5 = bardzo wysoko. Granica ćwiartek [ZAŁOŻENIE] w B3 — przy dużym skupieniu wyników użyjcie mediany.")
ws["A3"], ws["B3"] = "Granica ćwiartek", 3.0
ws["B3"].fill = INPUT
name("Granica", "'E3_Scoring'!$B$3")
f, l = 6, 17
heads = ["Proces", "Wolumen", "Powtarzalność", "Ustrukturyzowanie danych", "Pracochłonność (FTE)", "Poziom błędów",
         "Potencjał śr.", "Wpływ błędu na klienta / SLA", "Dane osobowe", "Regulacje", "Nieodwracalność decyzji",
         "Potrzeba empatii / osądu", "Ryzyko śr.", "Ćwiartka"]
table(ws, 5, heads, 12, [22, 9, 11, 13, 13, 10, 10, 13, 9, 10, 13, 13, 10, 30],
      input_cols=(1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12), labels=[f"[proces {i}]" for i in range(1, 13)],
      formulas={
          7: lambda r: f'=IF(COUNT(B{r}:F{r})=0,"",AVERAGE(B{r}:F{r}))',
          13: lambda r: f'=IF(COUNT(H{r}:L{r})=0,"",AVERAGE(H{r}:L{r}))',
          14: lambda r: (f'=IF(OR(G{r}="",M{r}=""),"",IF(G{r}>=Granica,IF(M{r}<Granica,"① Pierwsza fala: automatyzuj","② AI wspiera, człowiek zatwierdza"),'
                         f'IF(M{r}<Granica,"③ Usprawnienia bez AI","④ Zostaw człowiekowi")))'),
      })
for r in range(f, l + 1):
    ws[f"G{r}"].number_format = ws[f"M{r}"].number_format = "0.0"
ws.conditional_formatting.add(f"N{f}:N{l}", FormulaRule(formula=[f'LEFT(N{f},1)="①"'], fill=PatternFill("solid", fgColor="CFE2F3")))
ws.conditional_formatting.add(f"N{f}:N{l}", FormulaRule(formula=[f'LEFT(N{f},1)="④"'], fill=AMB))
ws["A19"], ws["B19"] = "Mediana potencjału", f'=IFERROR(MEDIAN(G{f}:G{l}),"")'
ws["A20"], ws["B20"] = "Mediana ryzyka", f'=IFERROR(MEDIAN(M{f}:M{l}),"")'
ws["A22"] = "Wybór: 2 procesy z ① + 1 z ② (powiązany z priorytetem E2) + 1 z ④ jako „zostawiony człowiekowi”."
ws["A22"].font = NOTE

# ---------------------------------------------------------------- E3 HITL
ws = sheet("E3_HITL", "Część II — proces obecny i mapa HITL",
           "Przykład (faktury kosztowe) jest ilustracyjny — progi to [ZAŁOŻENIE] do kalibracji na danych.")
ws["A4"] = "Proces obecny (z karty źródłowej)"
ws["A4"].font = BOLD
table(ws, 5, ["Krok", "Kto", "Czas (min)", "Narzędzie", "Typowe błędy"], 8, [28, 16, 20, 22, 30],
      input_cols=range(1, 6), labels=list(range(1, 9)))
ws["A16"] = "Mapa HITL"
ws["A16"].font = BOLD
first, _ = table(ws, 17, ["Krok", "Wykonawca", "Punkt kontroli", "Próg eskalacji do człowieka", "Właściciel"], 10,
                 input_cols=range(1, 6))
przyklad = [("PRZYKŁAD: Odczyt i ekstrakcja danych z faktury", "AI", "Walidacja pól obowiązkowych", "Pewność odczytu < 90%", "Lider zespołu AP"),
            ("PRZYKŁAD: Dopasowanie do zamówienia", "AI", "Porównanie kwot", "Rozbieżność > 2% lub brak zamówienia", "Księgowy"),
            ("PRZYKŁAD: Dekretacja", "AI proponuje", "Próbka 10% sprawdzana dziennie", "Nowy kontrahent, kwota > [X] zł", "Księgowy"),
            ("PRZYKŁAD: Akceptacja płatności", "Człowiek", "Zawsze", "—", "Kierownik działu"),
            ("PRZYKŁAD: Raport błędów AI", "AI + człowiek", "Przegląd tygodniowy", "Wzrost błędów > 1 pp", "Ambasador AI")]
for i, row in enumerate(przyklad):
    for j, v in enumerate(row, 1):
        c = ws.cell(row=first + i, column=j, value=v)
        c.font = NOTE

# ---------------------------------------------------------------- E3 business case
ws = sheet("E3_Business_case", "Część III — mini business case",
           "Pokazujcie payback NETTO — uwzględnia stały koszt licencji i jury rzadziej go podważa. Kwoty w zł.")
ws["A4"], ws["B4"], ws["C4"], ws["D4"] = "Pozycja", "Wartość", "Nazwa", "Wzór / źródło"
for c in ("A4", "B4", "C4", "D4"):
    ws[c].fill, ws[c].font = HDR, HDR_FONT
kv(ws, 5, "Liczba użytkowników (n)", None, "n_uzytk", "0", inp=True, note="z mapy HITL")
kv(ws, 6, "Cena licencji / użytkownik / mies. (c)", None, "Cena_lic", "#,##0", inp=True, note="z Excela lub od mentora")
kv(ws, 7, "Koszt licencji / mies.", "=n_uzytk*Cena_lic", "Licencja_mies", "#,##0", note="n × c")
kv(ws, 8, "Wdrożenie i integracja (jednorazowo)", None, "Wdrozenie", "#,##0", inp=True, note="z Excela / [ZAŁOŻENIE]")
kv(ws, 9, "Szkolenia: liczba osób", None, "Szkol_osoby", "0", inp=True)
kv(ws, 10, "Szkolenia: godziny na osobę", None, "Szkol_godz", "0", inp=True)
kv(ws, 11, "Szkolenia: koszt godziny", None, "Koszt_godz", "#,##0", inp=True)
kv(ws, 12, "Szkolenia (jednorazowo)", "=Szkol_osoby*Szkol_godz*Koszt_godz", "Szkolenia", "#,##0", note="osoby × godziny × koszt godziny")
kv(ws, 13, "Koszt jednorazowy", "=Wdrozenie+Szkolenia", "Koszt_jednoraz", "#,##0", note="wdrożenie + szkolenia")
kv(ws, 14, "Godziny zaoszczędzone / mies. (h)", None, "Godz_zaoszcz", "#,##0", inp=True, note="z karty procesu: kroki AI × wolumen")
kv(ws, 15, "Oszczędność FTE", "=Godz_zaoszcz/160", "FTE_uwolnione", "0.0", note="h / 160")
kv(ws, 16, "Miesięczny koszt etatu", None, "Koszt_etatu", "#,##0", inp=True, note="z Excela")
kv(ws, 17, "Wartość uwolnionego czasu / mies.", "=FTE_uwolnione*Koszt_etatu", "Oszcz_mies", "#,##0", note="FTE × mies. koszt etatu")
kv(ws, 18, "Koszt całkowity (1. rok)", "=Koszt_jednoraz+12*Licencja_mies", "Koszt_calk", "#,##0", note="jednorazowy + 12 × licencja")
kv(ws, 19, "Payback prosty (mies.)", '=IFERROR(Koszt_calk/Oszcz_mies,"")', "Payback_prosty", "0.0", note="koszt całkowity / oszczędność mies.")
kv(ws, 20, "Payback netto (mies.)", '=IFERROR(IF(Oszcz_mies<=Licencja_mies,"nie zwraca się",Koszt_jednoraz/(Oszcz_mies-Licencja_mies)),"")', "Payback_netto", "0.0", note="koszt jednorazowy / (oszczędność mies. − licencja mies.)")
kv(ws, 21, "Test wrażliwości: payback netto przy oszczędności −30%", '=IFERROR(IF(0.7*Oszcz_mies<=Licencja_mies,"nie zwraca się",Koszt_jednoraz/(0.7*Oszcz_mies-Licencja_mies)),"")', None, "0.0")
kv(ws, 22, "Test wrażliwości: payback netto przy kosztach +30%", '=IFERROR(IF(Oszcz_mies<=1.3*Licencja_mies,"nie zwraca się",1.3*Koszt_jednoraz/(Oszcz_mies-1.3*Licencja_mies)),"")', None, "0.0")
ws["A24"] = "Uwaga jury: przy „zero zwolnień” wartość uwolnionego czasu to nie gotówka. Wskażcie, co ją niesie:"
ws["A24"].font = BOLD
kv(ws, 25, "Uniknięte rekrutacje pod pipeline (zł/mies.)", None, None, "#,##0", inp=True)
kv(ws, 26, "Mniej kar SLA (zł/mies.)", None, None, "#,##0", inp=True)
kv(ws, 27, "Mniej nadgodzin (zł/mies.)", None, None, "#,##0", inp=True)
kv(ws, 28, "Nieobsadzone wakaty z rotacji (zł/mies.)", None, None, "#,##0", inp=True)
kv(ws, 29, "Suma oszczędności gotówkowych / mies.", "=SUM(B25:B28)", None, "#,##0")
for c in ("A", "B", "C", "D"):
    ws.column_dimensions[c].width = (52, 16, 16, 48)["ABCD".index(c)]

# ---------------------------------------------------------------- E4 uwolnione FTE
ws = sheet("E4_Uwolnione_FTE", "Krok 1 — Gdzie trafia uwolniony czas",
           "Uwolnione FTE idą na pracę, która przynosi przychód lub chroni klientów — nie na zwolnienia.")
table(ws, 4, ["Źródło (proces z E3)", "Uwolnione FTE", "Kierunek", "Ile FTE", "Uzasadnienie liczbą"], 4, [24, 13, 38, 10, 30],
      input_cols=(1, 2, 4, 5),
      labels=["[proces 1]", "[proces 2]", "[proces 3]", "Naturalna rotacja"])
for r, k, u in ((5, "Realizacja kontraktów z pipeline'u", "Luka FTE z E2"), (6, "Poprawa SLA w działach czerwonych", "SLA vs umowa z E1"),
                (7, "Obsługa premium / nowe usługi", "Opcja d) z E2"), (8, "Brak zastępowania części odejść", "Rotacja % z E1")):
    ws[f"C{r}"], ws[f"E{r}"] = k, u
ws["A9"], ws["B9"], ws["D9"] = "Suma", "=SUM(B5:B7)", "=SUM(D5:D7)"
ws["A9"].font = BOLD
ws["A10"], ws["B10"] = "Kontrola", '=IF(B9=0,"",IF(ABS(B9-D9)<0.05,"OK — całe uwolnione FTE ma kierunek","SPRAWDŹ — FTE bez kierunku"))'

# ---------------------------------------------------------------- E4 KPI
ws = sheet("E4_KPI", "Krok 4 — 3 KPI po roku + progi bram", "KPI = baza + cel 12 mies. + źródło + właściciel. Jeden KPI na wierzchołek Trójkąta.")
heads = ["KPI", "Grupa", "Baza (z Excela)", "Cel po 12 mies.", "Źródło danych", "Właściciel", "Częstotliwość", "Kompletny?"]
table(ws, 4, heads, 6, [40, 12, 14, 14, 22, 20, 14, 12], input_cols=(3, 4),
      labels=["Marża operacyjna", "Adopcja AI (% aktywnych użytkowników w procesach fali 1)", "SLA dotrzymane u klientów kluczowych",
              "(zapas) Rotacja w działach czerwonych", "(zapas) Retencja klientów (% przychodu utrzymany)", "(zapas) EV pipeline'u zamieniona na kontrakty"],
      formulas={8: lambda r: f'=IF(COUNTA(A{r}:G{r})=7,"✔","brakuje")'})
for r, g, b, s, o in ((5, "Zarząd", "=Marza", "Raport finansowy", "CFO"), (6, "Pracownicy", None, "Logi narzędzi AI", "Dyrektor HR"),
                      (7, "Klienci", None, "System raportowania SLA", "Dyrektor operacyjny")):
    ws[f"B{r}"], ws[f"E{r}"], ws[f"F{r}"], ws[f"G{r}"] = g, s, o, "Miesięcznie"
    if b:
        ws[f"C{r}"] = b
        ws[f"C{r}"].number_format = "0.0%"
ws["A12"] = "Progi bram"
ws["A12"].font = BOLD
table(ws, 13, ["Brama", "Warunek", "Próg", "Pomiar"], 2, input_cols=(3, 4),
      labels=["Brama 1 (po mies. 3)", "Brama 2 (po mies. 6)"])
ws["B14"], ws["B15"] = "Pilot utrzymuje SLA", "Adopcja i payback w celu"

# ---------------------------------------------------------------- Rejestr ryzyk
ws = sheet("Rejestr_ryzyk", "Rejestr ryzyk (prawdop. × wpływ)", "W = 3, Ś = 2, N = 1. Ocena wstępna — potwierdźcie na danych. Top 5 na slajd.")
ryzyka = [("Spadek SLA w okresie przejściowym", "Ś", "W", "Pilot na 1 procesie, praca równoległa człowiek + AI przez 4–6 tygodni, Brama 1", "Dyrektor operacyjny"),
          ("Naruszenie RODO / danych klientów", "N", "W", "Aneks do umów powierzenia, minimalizacja danych, regulamin AI, DPIA", "Radca prawny + IOD"),
          ("AI w decyzjach kadrowych (AI Act)", "Ś", "W", "Decyzje kadrowe zostają u człowieka; AI tylko jako wsparcie informacyjne", "Dyrektor HR"),
          ("Opór pracowników, spadek adopcji", "W", "Ś", "Komunikacja przed pilotem, ambasadorzy, dialog z przedstawicielami pracowników, KPI adopcji", "Dyrektor HR"),
          ("Rotacja kluczowych osób przy rosnącym pipeline", "Ś", "W", "Ścieżki kariery, premie za transfer wiedzy, dokumentacja procesów", "Kierownicy działów"),
          ("Klienci żądają rabatu", "W", "Ś", "Oferta gain-sharing z mierzalnym KPI, rabat tylko warunkowy", "Dyrektor handlowy"),
          ("Koszty AI wyższe od planu", "Ś", "Ś", "Test wrażliwości ±30%, licencje etapami, Brama 2", "CFO"),
          ("Błędy AI (halucynacje, złe dopasowania)", "Ś", "Ś", "Progi eskalacji, próbkowanie, tygodniowy raport błędów", "Ambasador AI w dziale"),
          ("Uzależnienie od jednego dostawcy", "N", "Ś", "Klauzule wyjścia, eksport danych, standardowe integracje", "CIO")]
first, last = table(ws, 4, ["Ryzyko", "Prawd.", "Wpływ", "Wynik (P×W)", "Mitygacja", "Właściciel"], len(ryzyka) + 3,
                    [40, 8, 8, 11, 60, 22], input_cols=(1, 2, 3, 5, 6),
                    formulas={4: lambda r: f'=IF(OR(B{r}="",C{r}=""),"",(MATCH(B{r},{{"N","Ś","W"}},0))*(MATCH(C{r},{{"N","Ś","W"}},0)))'})
for i, (a, p, w, m, o) in enumerate(ryzyka):
    r = first + i
    ws[f"A{r}"], ws[f"B{r}"], ws[f"C{r}"], ws[f"E{r}"], ws[f"F{r}"] = a, p, w, m, o
ws.conditional_formatting.add(f"D{first}:D{last}", CellIsRule(operator="greaterThanOrEqual", formula=["6"], fill=RED))
ws.conditional_formatting.add(f"D{first}:D{last}", CellIsRule(operator="between", formula=["3", "5"], fill=AMB))

# ---------------------------------------------------------------- Rejestr decyzji
ws = sheet("Rejestr_decyzji", "Rejestr decyzji", "Wypełniany na koniec każdego etapu, po rozmowie z mentorem.")
table(ws, 4, ["Etap", "Decyzja", "Kosztem czego", "Kluczowa liczba", "Źródło (arkusz!komórka)", "Akceptacja mentora"], 5,
      [8, 44, 30, 18, 24, 18], input_cols=range(2, 7), labels=["E1", "E2", "E3", "E4", "E5"])
ws["A11"] = "Teza:"
ws["A11"].font = BOLD
ws["B11"] = "Wybieramy … kosztem …, ponieważ … — i to działa dla zarządu, pracowników i klientów."
ws["B11"].fill = INPUT

for s in wb.worksheets:
    s.freeze_panes = None
    s.sheet_view.zoomScale = 110

OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print(f"Zapisano: {OUT}")
