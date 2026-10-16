# Etap 1 · 40 min · Diagnoza: gdzie firma jest dziś?

**Cel:** TOP 3 problemy z liczbą przy każdym i jedno zdanie „diagnoza na slajd”. Nie oceniajcie wszystkiego — szukajcie miejsca, gdzie **rotacja, SLA i niska marża klienta nakładają się na siebie**.

**Hipoteza do sprawdzenia:** [H1 — problemy są skoncentrowane](../wiedza/hipotezy.md) (1–2 działy z najwyższą rotacją = większość naruszeń SLA = klienci o największym udziale w przychodzie).

**Excel:** arkusze `E1_Dzialy`, `E1_Klienci`, `E1_Progi_RAG` w [`excel/HELVIA_szablony.xlsx`](../excel/HELVIA_szablony.xlsx).

## Przebieg minuta po minucie

| Min | Analityk danych | Analityk ludzi i ryzyk | Strateg | Projektant / timekeeper | Agenci |
|---|---|---|---|---|---|
| 0–10 | Otwiera pliki, sprawdza sumy z opisu (przychód, 720 os.) | Otwiera ankiety i dane o rotacji | Wypisuje nagłówki kolumn dla agentów | Zakłada folder i Rejestr decyzji | Orkiestrator dostaje nagłówki i rozdziela fale |
| 10–30 | Tabela 14 klientów + Pareto | Ankiety: top-2-box, rotacja per dział | Tabela 8 działów + RAG | Szkic slajdu 1 z miejscem na liczby | Finanse / Operacje / HR liczą równolegle |
| 30–35 | Korelacje: rotacja × SLA × marża | Potwierdza sygnały danymi z ankiet | Drzewo problemu | Szkic zdania diagnozy | Data-checker przelicza sumy |
| 35–40 | — | — | Mentor: hipoteza + 3 liczby | Wpis do Rejestru | Juror: najsłabszy punkt diagnozy |

**Fala agentów (min 10–25):** Finanse: klienci · Operacje: działy · HR: ankiety → weryfikacja Data-checker: czy sumy FTE i przychodów się domykają.

## Metody (każda daje liczbę na slajd)

| Metoda | Pytanie | Wynik do slajdu |
|---|---|---|
| Analiza wskaźnikowa (benchmark wewnętrzny) | Który dział / klient odstaje od średniej firmy? | Odchylenie od mediany w % |
| Pareto 80/20 i ABC klientów | Ilu klientów robi 80% przychodu i marży? | Krzywa koncentracji, „top 3 = X%” |
| Heatmapa RAG | Gdzie kumulują się sygnały ostrzegawcze? | Tabela 8 działów w kolorach |
| Korelacja (WSP.KORELACJI / CORREL) | Czy rotacja idzie w parze ze spadkiem SLA? | Współczynnik r + 1 zdanie |
| Analiza ankiet (top-2-box, eNPS) | Gdzie ludzie są najbardziej zaniepokojeni AI? | % odpowiedzi 4–5 |
| Drzewo problemu / 5×Dlaczego | Co jest przyczyną, a co objawem? | 1 przyczyna źródłowa |

**Triangulacja:** każdy wniosek z E1 potwierdzony co najmniej dwoma źródłami (np. dane operacyjne + ankieta).

## Szablon A — 8 działów

| Dział | FTE | Obciążenie (h/FTE) | Wydajność | Błędy / SLA vs umowa | Rotacja % | Ankieta: obawa przed AI % | Sygnał |
|---|---|---|---|---|---|---|---|
| Finanse i księgowość | | | | | | | |
| HR i payroll | | | | | | | |
| Obsługa klienta | | | | | | | |
| IT | | | | | | | |
| Logistyka | | | | | | | |
| Administracja | | | | | | | |
| [dział 7 z Excela] | | | | | | | |
| [dział 8 z Excela] | | | | | | | |
| **Suma / średnia** | **= 720?** | | | | | | |

## Szablon B — 14 klientów

| Klient | Przychód (mln zł) | Udział % | Skumulowany % | Marża % | SLA vs umowa | Presja cenowa / ryzyko odejścia | Główny dział | Sygnał |
|---|---|---|---|---|---|---|---|---|
| K1 | | | | | | | | |
| … | | | | | | | | |
| K14 | | | | | | | | |
| **Suma** | **= 114,93?** | **100%** | | | | | | |

## Progi sygnałów RAG `[ZAŁOŻENIE]`

Domyślne — dopasujcie do rozkładu danych, nazwijcie je na slajdzie, zweryfikujcie z mentorem.

| Wskaźnik | 🔴 Czerwony | 🟡 Żółty | 🟢 Zielony |
|---|---|---|---|
| SLA vs umowa | > 3 pp poniżej | 0–3 pp poniżej | ≥ umowa |
| Rotacja | > 1,5 × mediana firmy | 1–1,5 × mediana | < mediana |
| Marża klienta | < 0% lub < połowa średniej | poniżej 8,4% | ≥ 8,4% |
| Udział w przychodzie | > 15% (ryzyko koncentracji) | 7–15% | < 7% |

## Synteza — wzór zdania na slajd

> „HELVIA traci **[X mln zł / pp marży]**, bo w **[dział]** rotacja **[Y%]** i SLA **[Z% vs W% w umowie]** uderzają w klientów generujących **[N%]** przychodu.”

## TOP 3 problemy (problem · liczba · źródło · kogo dotyczy w Trójkącie)

1. …
2. …
3. …

**Zdanie diagnozy:** …

**Najsłabszy punkt (Juror):** …

---

### ✅ DECYZJA DO PODJĘCIA PRZEZ ZESPÓŁ
Które **2–3 priorytety strategiczne** przenosimy do Etapu 2? → wpis E1 w [`rejestr-decyzji.md`](../rejestr-decyzji.md).
