# Narzędzia (Python 3, jedyna zależność: `pip install openpyxl`)

| Skrypt | Do czego |
|---|---|
| `kalkulator.py` | `baza`, `rabat <pp>`, `gain`, `warunkowy`, `prog-rabatu`, `payback`, `slowa` — wynik zawsze ze wzorem do odtworzenia w Excelu |
| `sanity_check.py` | Czy Σ FTE = 720 i Σ przychodów = 114,93 mln zł; drukuje tylko nagłówki i sumy (bezpieczne dla agentów) |
| `generuj_szablony.py` | Odtwarza `excel/HELVIA_szablony.xlsx` |
| `generuj_dane_syntetyczne.py` | Fikcyjna HELVIA do próby generalnej (`--seed N` = nowy wariant) |

Wyniki z Pythona **zawsze przepisujemy do Excela** — slajd cytuje komórkę, nie terminal.
