# Etap 2 · 45 min · Strategia: dokąd zmierza HELVIA?

**Cel:** jedno zdanie „Wybieramy X kosztem Y, ponieważ …” oraz tabela opcji cenowych z policzonym wpływem na EBIT. **Wybór jednego kierunku jest ważniejszy niż wybór „najlepszego”.**

**Hipotezy:** [H2 — AI finansuje wzrost](../wiedza/hipotezy.md) (luka FTE pipeline'u), [H3 — rabat bezwarunkowy niszczy wartość](../wiedza/hipotezy.md).

**Excel:** `E2_Pipeline`, `E2_Macierz`, `E2_Opcje_cenowe`. **Kalkulator:** `python3 narzedzia/kalkulator.py rabat|gain|warunkowy …`

**Czaty Claude (min 10–30):** `analityk-finansowy`: EV pipeline + opcje cenowe · `analityk-operacji`: test pojemności · `strateg`: macierz 3 kierunków → `weryfikator`: trade-off i Trójkąt.

## Krok 1 — Pipeline i test pojemności (min 0–15)

| Kontrakt | Wartość roczna (mln zł) | Prawdop. % | EV = wartość × p | FTE potrzebne | Dział realizujący | Rotacja działu | Luka FTE |
|---|---|---|---|---|---|---|---|
| P1 | | | | | | | |
| … | | | | | | | |
| **Suma** | | | **Σ EV** | **Σ FTE** | | | |

**Pytanie kontrolne:** czy uwolnione przez AI FTE (Etap 3) pokryją lukę FTE pipeline'u? Jeśli tak — macie historię **„AI finansuje wzrost bez zwolnień”**.

## Krok 2 — Macierz kierunków (min 15–30)

Przykładowe trzy kierunki — nazwijcie własne na bazie Etapu 1. Ocena 1–5.

| Kryterium (waga) | A. Jakość: naprawa SLA w działach czerwonych | B. Efektywność: automatyzacja back-office | C. Wzrost: FTE do pipeline'u + oferta premium |
|---|---|---|---|
| Wpływ na EBIT w 12 mies. (30%) | | | |
| Ryzyko: SLA, kompetencje, opór (20%) | | | |
| Wykonalność w 12 mies. (25%) | | | |
| Trójkąt Dobrostanu (25%) | | | |
| **Wynik ważony (1–5)** | | | |

Wagi to `[ZAŁOŻENIE]` — pokażcie je jury jawnie, to dowód świadomego wyboru.
**Analiza wrażliwości:** czy zwycięzca wygrywa także przy wagach 25/25/25/25? (arkusz liczy to automatycznie)

Pomocniczo: **SWOT → TOWS** (2–3 kierunki łączące mocne strony z szansami), **scenariusze pesym./bazowy/optym.**

## Krok 3 — Warunki wobec klientów (min 30–40)

Punkt odniesienia: **EBIT ≈ 9,65 mln zł; 1 pp rabatu na całej bazie ≈ 1,15 mln zł.**

| Opcja | Mechanizm | Wpływ na EBIT (wzór) | Przykład liczbowy `[ZAŁOŻENIE]` | Dla klienta | Ryzyko |
|---|---|---|---|---|---|
| a) Ceny bez zmian, wyższy SLA | Ta sama cena, szybciej i lepiej | 0 do + (mniej kar SLA) | +[kary SLA z Excela] | Jakość, przewidywalność | Klient czuje, że nie dzieli się korzyścią |
| b) Gain-sharing | Klient dostaje s% zweryfikowanej oszczędności po spełnieniu KPI | + (1 − s) × oszczędność | s = 50%, oszczędność 2 mln → EBIT +1,0 mln | Realny udział w AI | Spór o metodę pomiaru |
| c) Rabat warunkowy | d% za dłuższy kontrakt / wolumen / zgodę na AI | − d × przychód klienta + utrzymana marża | d = 2% u klienta 8,2 mln → −0,16 mln | Niższa cena teraz | Efekt domina u innych klientów |
| d) Usługi premium AI | Nowa linia: analityka, raporty, 24/7 | + przychód premium × marża | `[ZAŁOŻENIE]` do wyceny z mentorem | Nowa wartość | Kompetencje, czas wdrożenia |
| ❌ Rabat bezwarunkowy (antywzorzec) | −2 pp na całej bazie | − 0,02 × 114,93 | −2,30 mln = **−24% EBIT** | Krótka radość | Niszczy marżę — pokażcie jako odrzuconą opcję |

Utrata klienta liczona jest **marżą pokrycia** (przychód − koszty zmienne), a nie marżą 8,4% — koszty stałe zostają. Poproście mentora o strukturę kosztów, jeśli jej nie ma w danych.

## Krok 4 — Decyzja i warunek powrotu (min 40–45)

> „Wybieramy **[X]** kosztem **[Y]**, ponieważ **[liczba z E1/E2]**. Wracamy do **[Y]**, gdy **[warunek mierzalny, np. SLA ≥ umowa przez 2 kwartały]**.”

**Zdanie:** …

**Najsłabszy punkt (weryfikator):** …

---

### ✅ DECYZJA DO PODJĘCIA PRZEZ ZESPÓŁ
Jeden priorytet, odłożona alternatywa z warunkiem powrotu, wybrana opcja (lub kombinacja) warunków dla klientów → wpis E2 w [`rejestr-decyzji.md`](../rejestr-decyzji.md).
