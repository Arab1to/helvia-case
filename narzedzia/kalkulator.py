#!/usr/bin/env python3
"""Kalkulator case'u HELVIA — szybkie przeliczenia do slajdów i pytań jury.

Każdy wynik pokazuje wzór, żeby dało się go odtworzyć w Excelu.
Kwoty w mln zł, chyba że zaznaczono inaczej.

Przykłady:
  python3 narzedzia/kalkulator.py baza
  python3 narzedzia/kalkulator.py rabat 2
  python3 narzedzia/kalkulator.py gain --oszczednosc 2 --udzial 0.5
  python3 narzedzia/kalkulator.py warunkowy --rabat 2 --przychod-klienta 8.2
  python3 narzedzia/kalkulator.py prog-rabatu --rabat 2 --marza-pokrycia 0.25
  python3 narzedzia/kalkulator.py payback --jednorazowy 300000 --oszcz-mies 60000 --licencja-mies 15000
  python3 narzedzia/kalkulator.py slowa 05_etap5_prezentacja/skrypt-3min.md
"""
import argparse
import re
import sys

PRZYCHOD = 114.93  # mln zł, z opisu case'u
MARZA = 0.084
PRACOWNICY = 720
KLIENCI = 14
EBIT = PRZYCHOD * MARZA


def pl(x, nd=2):
    """Liczba w zapisie polskim (przecinek dziesiętny, spacja tysięcy)."""
    s = f"{x:,.{nd}f}".replace(",", " ").replace(".", ",")
    return s


def cmd_baza(_):
    rows = [
        ("Przychód LTM", f"{pl(PRZYCHOD)} mln zł", "z opisu"),
        ("EBIT", f"{pl(EBIT)} mln zł", f"{pl(PRZYCHOD)} × {pl(MARZA * 100, 1)}%"),
        ("Przychód / pracownik", f"{pl(PRZYCHOD / PRACOWNICY * 1000, 1)} tys. zł", f"{pl(PRZYCHOD)} mln / {PRACOWNICY}"),
        ("EBIT / pracownik", f"{pl(EBIT / PRACOWNICY * 1000, 1)} tys. zł", f"{pl(EBIT)} mln / {PRACOWNICY}"),
        ("Średni przychód / klient", f"{pl(PRZYCHOD / KLIENCI)} mln zł ({pl(100 / KLIENCI, 1)}%)", f"{pl(PRZYCHOD)} / {KLIENCI}"),
        ("1 pp rabatu", f"{pl(PRZYCHOD * 0.01)} mln zł = {pl(PRZYCHOD * 0.01 / EBIT * 100, 1)}% EBIT", f"{pl(PRZYCHOD)} × 1%"),
    ]
    print("| Wskaźnik | Wartość | Wzór |\n|---|---|---|")
    for r in rows:
        print(f"| {r[0]} | {r[1]} | {r[2]} |")


def cmd_rabat(a):
    d = a.pp / 100
    wplyw = -d * PRZYCHOD
    print(f"Rabat bezwarunkowy {pl(a.pp, 1)} pp na całej bazie")
    print(f"  Wpływ na EBIT = −{pl(d, 3)} × {pl(PRZYCHOD)} = {pl(wplyw)} mln zł")
    print(f"  Jako % EBIT   = {pl(wplyw)} / {pl(EBIT)} = {pl(wplyw / EBIT * 100, 1)}%")
    print(f"  Marża po rabacie ≈ {pl((EBIT + wplyw) / (PRZYCHOD * (1 - d)) * 100, 2)}% (przy niezmienionych kosztach)")


def cmd_gain(a):
    zysk = (1 - a.udzial) * a.oszczednosc
    print(f"Gain-sharing: klient dostaje {pl(a.udzial * 100, 0)}% zweryfikowanej oszczędności {pl(a.oszczednosc)} mln zł")
    print(f"  Zysk HELVII = (1 − {pl(a.udzial, 2)}) × {pl(a.oszczednosc)} = +{pl(zysk)} mln zł")
    print(f"  Jako % EBIT = +{pl(zysk / EBIT * 100, 1)}%  |  +{pl(zysk / PRZYCHOD * 100, 2)} pp marży")
    print(f"  Klient dostaje {pl(a.udzial * a.oszczednosc)} mln zł  [ZAŁOŻENIE: oszczędność do potwierdzenia w Excelu]")


def cmd_warunkowy(a):
    d = a.rabat / 100
    wplyw = -d * a.przychod_klienta
    print(f"Rabat warunkowy {pl(a.rabat, 1)}% u klienta o przychodzie {pl(a.przychod_klienta)} mln zł")
    print(f"  Wpływ na EBIT = −{pl(d, 3)} × {pl(a.przychod_klienta)} = {pl(wplyw)} mln zł ({pl(wplyw / EBIT * 100, 1)}% EBIT)")
    print(f"  Porównanie: ten sam rabat na całej bazie = {pl(-d * PRZYCHOD)} mln zł")


def cmd_prog_rabatu(a):
    d = a.rabat / 100
    koszt = d * PRZYCHOD
    prog = koszt / a.marza_pokrycia
    print(f"Kiedy rabat bezwarunkowy {pl(a.rabat, 1)} pp się opłaca? (marża pokrycia {pl(a.marza_pokrycia * 100, 0)}% [ZAŁOŻENIE])")
    print(f"  Koszt rabatu       = {pl(d, 3)} × {pl(PRZYCHOD)} = {pl(koszt)} mln zł/rok")
    print(f"  Próg opłacalności  = {pl(koszt)} / {pl(a.marza_pokrycia, 2)} = {pl(prog)} mln zł przychodu, który rabat MUSIAŁBY uratować")
    print(f"  To ≈ {pl(prog / PRZYCHOD * 100, 1)}% przychodu ≈ {pl(prog / (PRZYCHOD / KLIENCI), 1)} średniego klienta")
    print("  Jeśli realne ryzyko odejścia (p × przychód) jest mniejsze — rabat niszczy wartość (H3).")


def cmd_payback(a):
    netto_mies = a.oszcz_mies - a.licencja_mies
    calkowity = a.jednorazowy + 12 * a.licencja_mies
    print("Business case (zł)")
    print(f"  Koszt jednorazowy (wdrożenie + szkolenia) = {pl(a.jednorazowy, 0)}")
    print(f"  Licencja / mies.                          = {pl(a.licencja_mies, 0)}")
    print(f"  Oszczędność / mies.                       = {pl(a.oszcz_mies, 0)}")
    print(f"  Payback prosty = koszt 1. roku / oszczędność mies. = ({pl(a.jednorazowy, 0)} + 12 × {pl(a.licencja_mies, 0)}) / {pl(a.oszcz_mies, 0)} = {pl(calkowity / a.oszcz_mies, 1)} mies.")
    if netto_mies <= 0:
        print("  Payback netto: ⚠ oszczędność ≤ licencja — wdrożenie się NIE zwraca")
        return
    print(f"  Payback netto  = {pl(a.jednorazowy, 0)} / ({pl(a.oszcz_mies, 0)} − {pl(a.licencja_mies, 0)}) = {pl(a.jednorazowy / netto_mies, 1)} mies.  ← pokazujcie ten")
    for nazwa, o, l in (("oszczędność −30%", a.oszcz_mies * 0.7, a.licencja_mies),
                        ("koszty +30%", a.oszcz_mies, a.licencja_mies * 1.3)):
        jedn = a.jednorazowy * (1.3 if "koszty" in nazwa else 1)
        n = o - l
        wynik = f"{pl(jedn / n, 1)} mies." if n > 0 else "nie zwraca się"
        print(f"  Wrażliwość ({nazwa}): payback netto = {wynik}")
    if a.koszt_etatu:
        fte = a.oszcz_mies / a.koszt_etatu
        print(f"  Ekwiwalent FTE = {pl(a.oszcz_mies, 0)} / {pl(a.koszt_etatu, 0)} = {pl(fte, 1)} FTE")


def cmd_slowa(a):
    tekst = open(a.plik, encoding="utf-8").read()
    cytaty = [c for c in re.findall(r"„([^”]+)”", tekst) if len(c.split()) >= 5]
    if not cytaty:
        cytaty = [tekst]
    razem = 0
    for i, c in enumerate(cytaty, 1):
        n = len(c.split())
        razem += n
        print(f"  blok {i}: {n} słów")
    print(f"Razem: {razem} słów ≈ {pl(razem / 130, 2)} min przy 130 słowach/min (limit 3:00 ≈ 390 słów)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("baza", help="liczby bazowe case'u").set_defaults(f=cmd_baza)
    r = s.add_parser("rabat", help="wpływ rabatu bezwarunkowego (pp) na EBIT")
    r.add_argument("pp", type=float)
    r.set_defaults(f=cmd_rabat)
    g = s.add_parser("gain", help="gain-sharing")
    g.add_argument("--oszczednosc", type=float, required=True, help="zweryfikowana oszczędność, mln zł")
    g.add_argument("--udzial", type=float, default=0.5, help="udział klienta s (0–1)")
    g.set_defaults(f=cmd_gain)
    w = s.add_parser("warunkowy", help="rabat warunkowy u jednego klienta")
    w.add_argument("--rabat", type=float, required=True, help="%%")
    w.add_argument("--przychod-klienta", type=float, required=True, help="mln zł")
    w.set_defaults(f=cmd_warunkowy)
    pr = s.add_parser("prog-rabatu", help="ile przychodu musiałby uratować rabat, żeby się opłacał")
    pr.add_argument("--rabat", type=float, default=1.0, help="pp")
    pr.add_argument("--marza-pokrycia", type=float, required=True, help="0–1, np. 0.25")
    pr.set_defaults(f=cmd_prog_rabatu)
    pb = s.add_parser("payback", help="payback prosty i netto + wrażliwość")
    pb.add_argument("--jednorazowy", type=float, required=True, help="zł")
    pb.add_argument("--oszcz-mies", type=float, required=True, help="zł / mies.")
    pb.add_argument("--licencja-mies", type=float, required=True, help="zł / mies.")
    pb.add_argument("--koszt-etatu", type=float, help="mies. koszt etatu, zł (opcjonalnie)")
    pb.set_defaults(f=cmd_payback)
    sl = s.add_parser("slowa", help="licznik słów w skrypcie (bloki w cudzysłowach „…”)")
    sl.add_argument("plik")
    sl.set_defaults(f=cmd_slowa)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    sys.exit(main())
