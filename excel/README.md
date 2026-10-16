# Excel — jedyne źródło prawdy dla liczb

`HELVIA_szablony.xlsx` — wszystkie tabele z playbooka z gotowymi formułami (żółte = wypełniacie, niebieskie = formuły).
Odtworzenie: `python3 narzedzia/generuj_szablony.py`.

| Arkusz | Etap | Co liczy |
|---|---|---|
| `Start` | — | Liczby bazowe (nazwane: `Przychod`, `Marza`, `EBIT`, `Rabat_1pp`), sanity-check sum, progi RAG |
| `E1_Dzialy` | E1 | Szablon A: sygnały RAG rotacja / SLA / łączny, Σ FTE, korelacja r, liczba działów w czerwieni |
| `E1_Klienci` | E1 | Szablon B: udział, Pareto (niezależne od kolejności), ranking, sygnał, „top 3 = X%” |
| `E2_Pipeline` | E2 | EV pipeline'u, luka FTE, czy AI pokrywa lukę (z `FTE_uwolnione` z E3) |
| `E2_Macierz` | E2 | Wynik ważony 3 kierunków + test odporności na wagi 25/25/25/25 |
| `E2_Opcje_cenowe` | E2 | Wpływ opcji a)–d) i rabatu bezwarunkowego na EBIT; próg opłacalności rabatu |
| `E3_Scoring` | E3 | Potencjał / ryzyko (średnie), automatyczna ćwiartka ①–④ |
| `E3_HITL` | E3 | Proces obecny + mapa HITL (przykład faktur jako wzór) |
| `E3_Business_case` | E3 | Licencje, wdrożenie, szkolenia, FTE, payback prosty i netto, wrażliwość −30% / +30% |
| `E4_Uwolnione_FTE` | E4 | Gdzie trafia uwolniony czas + kontrola |
| `E4_KPI` | E4 | 3 KPI + zapasowe, kontrola kompletności, progi bram |
| `Rejestr_ryzyk` | E4 | Bank ryzyk z wynikiem P×W i kolorowaniem |
| `Rejestr_decyzji` | E1–E5 | Decyzja · kosztem czego · liczba · źródło · akceptacja mentora |

**Konwencja plików roboczych:** kopiujcie szablon do wspólnego folderu jako `HELVIA_E1_v1.xlsx`, `HELVIA_E2_v1.xlsx` … (jedna wersja, jeden właściciel — Analityk danych).

Formuły są zapisane w notacji EN; Excel PL wyświetla je automatycznie po polsku. Przy pisaniu formuł ręcznie — ściąga PL/EN: [`wiedza/formuly-excel.md`](../wiedza/formuly-excel.md).
