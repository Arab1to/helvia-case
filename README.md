# HELVIA — case solving · Dni Przedsiębiorczości Poznań 2026

> **Wygrywa najlepiej uzasadniona decyzja, nie najlepsza technologia.**
> „Wybieramy **X** kosztem **Y**, ponieważ **[liczba z Excela]** — i to działa dla **zarządu, pracowników i klientów**.”

To repo jest jedynym miejscem pracy zespołu: playbook rozbity na etapy, szablony Excela, skille agentów AI, rejestr decyzji i materiały do prezentacji. Pełny playbook (PDF): [`docs/Playbook_HELVIA_jak_wygrac_case.pdf`](docs/Playbook_HELVIA_jak_wygrac_case.pdf).

---

## Gdzie co jest

| Folder | Kiedy otwierasz | Co tam jest |
|---|---|---|
| [`00_start/`](00_start/) | dzień wcześniej i na starcie | [zasady gry (1 strona do druku)](00_start/zasady-gry.md), [role zespołu](00_start/role-zespolu.md), [checklista](00_start/checklista-przed-warsztatami.md), [praca z mentorem](00_start/praca-z-mentorem.md) |
| [`01_etap1_diagnoza/`](01_etap1_diagnoza/) | Etap 1 · 40 min | Gdzie firma jest dziś? TOP 3 problemy + zdanie diagnozy |
| [`02_etap2_strategia/`](02_etap2_strategia/) | Etap 2 · 45 min | Dokąd zmierza HELVIA? „Wybieramy X kosztem Y” + opcje cenowe |
| [`03_etap3_czlowiek-ai/`](03_etap3_czlowiek-ai/) | Etap 3 · 70 min | 3 procesy do AI, 1 zostawiony człowiekowi, mapa HITL, payback |
| [`04_etap4_zmiana/`](04_etap4_zmiana/) | Etap 4 · 70 min | Harmonogram 3 faz, komunikacja, 3 KPI, ryzyka |
| [`05_etap5_prezentacja/`](05_etap5_prezentacja/) | Etap 5 · 3 slajdy + 3:00 | Szkielet slajdów, skrypt, bank pytań jury, pre-mortem |
| [`wiedza/`](wiedza/) | cały czas | metody, formuły Excela PL/EN, bank argumentów, bank ryzyk, hipotezy H1–H3 |
| [`excel/`](excel/) | cały czas | `HELVIA_szablony.xlsx` — wszystkie puste tabele z formułami + Rejestr decyzji |
| [`agenci/`](agenci/) | dzień wcześniej (setup) + każdy etap | Hermes Agent: 8 skilli, szablon `delegate_task`, plan fal, zasady HITL, plan B |
| [`narzedzia/`](narzedzia/) | w trakcie | kalkulator rabat / gain-sharing / payback, sanity-check Excela, generator danych próbnych |
| [`dane/`](dane/) | w trakcie | `organizator/` — pliki od organizatora (**nie commitujemy**), `syntetyczne/` — dane na próbę generalną |
| [`rejestr-decyzji.md`](rejestr-decyzji.md) | koniec każdego etapu | E1–E5: decyzja · kosztem czego · liczba · źródło · akceptacja mentora |

## Łańcuch etapów (bez przeskoków)

```
E1 Diagnoza ──► E2 Strategia ──► E3 Człowiek + AI ──► E4 Roczna zmiana ──► E5 3 slajdy / 3:00
 TOP 3 problemy   Wybieramy X       3 procesy AI          3 fazy, 2 bramy       teza w 1. zdaniu
 + liczby         kosztem Y         1 dla człowieka        3 KPI, ryzyka         + bank pytań jury
```

**Rytm każdego etapu:** 0–15% czasu dane i podział pracy → 15–75% analiza równoległa (ludzie + agenci) → 75–90% synteza (1 zdanie + 3 liczby) → 90–100% mentor (2–3 min), decyzja, wpis do [Rejestru decyzji](rejestr-decyzji.md).

## Liczby bazowe (do weryfikacji w Excelu w pierwszych 10 min)

| Wskaźnik | Wartość | Wzór |
|---|---|---|
| Przychód LTM | 114,93 mln zł | z opisu |
| EBIT | ≈ 9,65 mln zł | 114,93 × 8,4% |
| Przychód / pracownik | ≈ 159,6 tys. zł | 114,93 mln / 720 |
| EBIT / pracownik | ≈ 13,4 tys. zł | 9,65 mln / 720 |
| Średni przychód / klient | ≈ 8,2 mln zł (≈ 7%) | 114,93 / 14 |
| **1 pp rabatu** | **≈ 1,15 mln zł ≈ 12% EBIT** | 114,93 × 1% |

Najmocniejsza broń: **każdy punkt procentowy rabatu „za AI” zjada ok. 1/8 rocznego zysku.**

## Zasady pracy z repo

- **Excel jest jedynym źródłem prawdy dla liczb.** Każda liczba w `.md`/na slajdzie musi dać się odtworzyć w arkuszu. Liczba spoza Excela = `[ZAŁOŻENIE]`.
- Pliki od organizatora → `dane/organizator/` (folder jest w `.gitignore` — dane poufne, RODO).
- Do modeli AI idą **nagłówki i zagregowane liczby**, nigdy surowe arkusze ani odpowiedzi osobowe z ankiet.
- Nazewnictwo plików roboczych: `HELVIA_E1_v1.xlsx`, `HELVIA_E2_v1.xlsx`, …
- Decyzja zapada w zespole (HITL) i trafia do [`rejestr-decyzji.md`](rejestr-decyzji.md) oraz zakładki „Rejestr decyzji” w Excelu.

## Szybki start

```bash
pip install openpyxl                         # jedyna zależność
python3 narzedzia/sanity_check.py dane/organizator/HELVIA.xlsx   # czy sumy się domykają (720 FTE, 114,93 mln)
python3 narzedzia/kalkulator.py rabat 2      # wpływ rabatu 2 pp na EBIT
python3 narzedzia/kalkulator.py --help       # gain-sharing, payback, wrażliwość
python3 narzedzia/generuj_szablony.py        # odtwarza excel/HELVIA_szablony.xlsx
python3 narzedzia/generuj_dane_syntetyczne.py   # fikcyjna HELVIA do próby generalnej
```

Asystent AI (Claude) pracuje według [`CLAUDE.md`](CLAUDE.md).
