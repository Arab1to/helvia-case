#!/usr/bin/env python3
"""Sanity-check w 30 sekund dla pliku Excel od organizatora.

Szuka w każdym arkuszu kolumn wyglądających na FTE / przychód i sprawdza, czy sumy
domykają się z opisem case'u: Σ FTE = 720, Σ przychodów = 114,93 mln zł.
Drukuje TYLKO nagłówki i sumy (żadnych wierszy z danymi) — wynik można bezpiecznie
wkleić agentom.

Użycie:
  python3 narzedzia/sanity_check.py dane/organizator/HELVIA.xlsx
"""
import sys

try:
    import openpyxl
except ImportError:
    sys.exit("Brak openpyxl: pip install openpyxl")

FTE_OCZEKIWANE = 720
PRZYCHOD_OCZEKIWANY = 114.93  # mln zł
TOLERANCJA = 0.005  # 0,5%

FTE_KLUCZE = ("fte", "etat", "pracown", "zatrudn", "headcount")
PRZYCHOD_KLUCZE = ("przych", "revenue", "sprzeda", "obrót", "obrot")


def ocen(nazwa, suma, oczekiwane):
    for skala, opis in ((1, ""), (1e-3, " (tys. → mln)"), (1e-6, " (zł → mln)")):
        v = suma * skala
        if oczekiwane and abs(v - oczekiwane) / oczekiwane <= TOLERANCJA:
            return f"✅ {nazwa}: {v:,.2f}{opis} ≈ {oczekiwane}"
    return f"⚠️  {nazwa}: suma {suma:,.2f} ≠ {oczekiwane} — sprawdźcie z mentorem przed wnioskami"


def main(sciezka):
    wb = openpyxl.load_workbook(sciezka, data_only=True, read_only=True)
    for ws in wb.worksheets:
        wiersze = list(ws.iter_rows(values_only=True))
        if not wiersze:
            continue
        # wiersz nagłówka = pierwszy wiersz z ≥ 2 tekstami
        hdr_idx = next((i for i, r in enumerate(wiersze[:10])
                        if sum(isinstance(c, str) for c in r) >= 2), 0)
        naglowki = [str(c).strip() if c is not None else "" for c in wiersze[hdr_idx]]
        dane = wiersze[hdr_idx + 1:]
        print(f"\n## Arkusz: {ws.title}  ({len(dane)} wierszy danych)")
        print("Nagłówki:", " | ".join(h for h in naglowki if h))
        for j, h in enumerate(naglowki):
            hl = h.lower()
            liczby = [r[j] for r in dane if j < len(r) and isinstance(r[j], (int, float))
                      and not (isinstance(r[0], str) and r[0].strip().lower().startswith(("suma", "razem", "total")))]
            if not liczby:
                continue
            suma = sum(liczby)
            if "/" in hl or "koszt" in hl or "potrzeb" in hl:
                continue  # wskaźniki na FTE, koszty, pipeline — nie sumujemy
            if any(k in hl for k in FTE_KLUCZE):
                print(ocen(f"Σ {h}", suma, FTE_OCZEKIWANE))
            elif any(k in hl for k in PRZYCHOD_KLUCZE):
                print(ocen(f"Σ {h}", suma, PRZYCHOD_OCZEKIWANY))
    ebit = PRZYCHOD_OCZEKIWANY * 0.084
    print(f"\nEBIT z opisu = {PRZYCHOD_OCZEKIWANY} × 8,4% = {ebit:.2f} mln zł "
          f"(porównajcie z EBIT w danych, jeśli jest)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
