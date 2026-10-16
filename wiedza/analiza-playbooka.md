# Analiza playbooka — notatki asystenta

Przygotowane po lekturze całego playbooka (27 stron). Cel: wiedzieć, **co decyduje o wygranej**, gdzie są pułapki i czego jeszcze brakuje.

## 1. Logika wygranej w jednym akapicie

Jury ocenia **jakość uzasadnienia decyzji**, nie technologię. Cały proces jest lejkiem: E1 znajduje miejsce, gdzie rotacja, SLA i niska marża nakładają się na siebie → E2 zamienia to w jedno zdanie „Wybieramy X kosztem Y, ponieważ [liczba]” → E3 i E4 pokazują, że ta decyzja jest wykonalna (HITL, payback, ludzie, KPI) → E5 opowiada to w 3:00. **Najczęstszy błąd to przeskok** (np. procesy AI w E3 niepowiązane z priorytetem z E2). Każdy etap musi cytować liczbę z poprzedniego.

## 2. Liczby, które trzeba znać na pamięć (przeliczone)

| Liczba | Wartość | Rachunek |
|---|---|---|
| EBIT | 9,654 mln zł | 114,93 × 0,084 |
| 1 pp rabatu | 1,149 mln zł = **11,9% EBIT** (≈ 1/8) | 114,93 × 0,01 / 9,654 |
| 2 pp rabatu | 2,299 mln zł = **23,8% EBIT** | |
| Gain-sharing 50% × 2 mln | +1,0 mln zł = **+10,4% EBIT** (+0,87 pp marży) | `[ZAŁOŻENIE]` z playbooka |
| Różnica gain-sharing vs rabat 2 pp | **≈ 3,3 mln zł EBIT** | 1,0 − (−2,3) |
| +1 pp marży operacyjnej | +1,149 mln zł EBIT | czyli tyle samo co „oddany” 1 pp rabatu |
| Przychód / pracownik | 159,6 tys. zł | |
| EBIT / pracownik | 13,4 tys. zł | |
| Średni klient | 8,21 mln zł = 7,1% przychodu | 114,93 / 14 |

Narzędzie: `python3 narzedzia/kalkulator.py baza`.

## 3. Pułapki, na które jury może złapać (i odpowiedzi)

1. **„Skoro nikogo nie zwalniacie, skąd oszczędność w business case?”** — to najsłabszy punkt tezy „zero zwolnień”. Wartość uwolnionego czasu (`FTE × koszt etatu`) nie jest oszczędnością gotówkową, jeśli etaty zostają. Uczciwa odpowiedź: wartość = **uniknięte rekrutacje** pod kontrakty z pipeline'u (FTE, których nie trzeba zatrudnić) + **mniej kar SLA** + **mniej nadgodzin** + **nieobsadzane wakaty z naturalnej rotacji**. W business case podpiszcie, która z tych pozycji niesie oszczędność. → dopisane do banku pytań.
2. **Korelacja na 8 działach** jest krucha — 1 dział odstający potrafi zrobić r = 0,7. Mówcie „idzie w parze”, nie „powoduje”; pokażcie wykres punktowy; potwierdźcie ankietą (triangulacja).
3. **Utrata klienta liczona marżą 8,4%** zaniża jej koszt — koszty stałe zostają. Liczcie marżą pokrycia (zapytać mentora o strukturę kosztów). To samo działa w drugą stronę: dodatkowy przychód z pipeline'u też wnosi marżę pokrycia, nie 8,4%.
4. **Wagi macierzy** — jury zapyta „a przy innych wagach?”. Arkusz `E2_Macierz` liczy od razu wariant 25/25/25/25.
5. **Payback prosty vs netto** — pokazujcie netto (z licencją) i wariant −30% oszczędności.
6. **Payroll / HR w ćwiartce „automatyzuj”** — AI Act traktuje AI w decyzjach kadrowych jako wyższe ryzyko; payroll = „AI wspiera, człowiek zatwierdza”.
7. **Liczby „ilustracyjne” z playbooka** (s = 50%, 2 mln, progi HITL 90% / 2% / 10%) **nie mogą trafić na slajd** bez zastąpienia danymi z Excela.

## 4. Ścieżka krytyczna i czas

| Etap | Czas | Okno agentów | Kluczowy artefakt | Zależy od |
|---|---|---|---|---|
| E1 | 40 min | 10–25 | TOP 3 + zdanie diagnozy | dane organizatora, sanity-check |
| E2 | 45 min | 10–30 | Zdanie „Wybieramy X kosztem Y” + opcje cenowe | E1 (2–3 priorytety) |
| E3 | 70 min | 15–50 | 3+1 procesy, HITL, payback netto | E2 (priorytet → proces nr 3) |
| E4 | 70 min | 15–50 | 3 fazy, 2 bramy, 3 KPI, top 5 ryzyk | E2 (luka FTE), E3 (FTE uwolnione) |
| E5 | ? | — | 3 slajdy, skrypt ≤ 3:00 | Rejestr decyzji E1–E4 |

Łącznie 225 min pracy etapowej + E5. Limit czasu przygotowania E5 nie jest podany w playbooku — **zapytać organizatora**.

## 5. Luki do zamknięcia przed warsztatami

| Luka | Co zrobić | Kto |
|---|---|---|
| Brak `prompt_helvia_case.md` (opis case'u) w repo | Wrzucić do `docs/`, zaktualizować `agenci/skills/helvia-juror` | Strateg |
| Definicja „Trójkąta Dobrostanu” i 10 kryteriów jury | Przepisać z opisu case'u do `agenci/skills/helvia-juror/SKILL.md` | Strateg |
| Nazwy działów 7 i 8, nazwy klientów | Uzupełnić po otrzymaniu Excela | Analityk danych |
| Struktura kosztów / marża pokrycia | Mentor na starcie E2 | Analityk danych |
| Koszt licencji AI, koszt wdrożenia | Mentor / Excel w E3 | Analityk danych |
| Zgoda na wysyłanie danych do zewnętrznych modeli | Mentor na starcie | Decydent |
| Klucze `delegation` w `~/.hermes/config.yaml` | Sprawdzić w dokumentacji Hermesa przy setupie | Projektant |
| Limit czasu przygotowania E5, szablon slajdów organizatora | Organizator | Timekeeper |

## 6. Jak asystent (Claude) pomaga w każdym etapie

- **Przed etapem:** przypomnienie celu, hipotezy, decyzji do podjęcia; wklejenie szablonu tabeli.
- **W trakcie:** przeliczenia (kalkulator), formuły PL/EN, krytyka hipotez, szkice zdań syntezy.
- **Synteza:** zdanie wg wzoru etapu + 3 liczby + najsłabszy punkt + gotowy wiersz do rejestru decyzji.
- **Przed E5:** skrócenie skryptu do ≤ 390 słów, pre-mortem, 8 pytań jury z odpowiedziami z liczbą.
- **Zawsze:** zero wymyślonych liczb; brak danych = `[ZAŁOŻENIE]` + sposób weryfikacji.
