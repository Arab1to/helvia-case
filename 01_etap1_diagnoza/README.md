# Etap 1 · 55 min · Diagnoza strategiczna: jak jest?

**Wg organizatora:** przejść od rozproszonych informacji do priorytetów strategicznych. Liczą się **dowody, interpretacja i końcowa decyzja**; nie ma klucza odpowiedzi. **Oceniany jest tylko arkusz 1B (główne wnioski)** — 1A i 1C są pomocnicze, ale 1C trafia na 1. slajd.

| Arkusz organizatora | Zadanie | Wynik |
|---|---|---|
| **1A Oceny ryzyka** | 1 najważniejsza flaga (z listy rozwijanej) dla każdego z 14 klientów i 8 działów + liczba, arkusz/komórka, interpretacja | 22 flagi z dowodami |
| **1B Główne wnioski — OCENIANY** | 6–8 problemów lub szans; każdy: fakt 1, fakt 2, interpretacja, rodzaj (Problem/Szansa/Mieszany), co sprawdzić | S1–S8 |
| **1C Diagnoza dla zarządu** | 3 priorytety (ID z 1B) + dlaczego, dowody, co zbadać; który sygnał świadomie pomijacie; diagnoza w 1 zdaniu | Slajd 1 |

📊 **Gotowa analiza danych i propozycja 1A/1B/1C:** [`analiza-E1.md`](analiza-E1.md) · plik `dane/organizator/HITL_Etap_1_propozycja.xlsx` · liczby odtwarza `python3 narzedzia/analiza_e1.py dane/organizator/HITL_Etap_1.xlsx`

**Hipoteza do sprawdzenia:** [H1 — problemy są skoncentrowane](../wiedza/hipotezy.md) → na danych **potwierdzona** (Obsługa Klienta × NORDA/Lumea).

## Gdzie co jest w pliku organizatora

| Arkusz | Co zawiera | Do której flagi |
|---|---|---|
| Dashboard | KPI firmy: przychód, marża, kary SLA, kontrakty do 31.03.2027, pipeline (tylko S-01…S-09!) | wszystkie |
| Klienci (+ Info do tabeli) | 14 klientów: przychód, koszt, marża, kontrakt, kary SLA, reklamacje, dynamika, udział w portfelu, NPS | 1A klienci |
| Historia miesięczna | 12 mies. × 14 klientów: przychód, wolumen, SLA, reklamacje, kary | trendy SLA |
| **Pipeline (ukryty!)** | 22 szanse: wartość, szansa %, FTE, dział | S4, E2 |
| Wolumeny klient proces | 46 procesów × klienci: wolumen i godziny / mies. | FTE-ekw., kandydaci do AI (E3) |
| Działy | 4 bloki: finanse, HR (FTE, rotacja, nadgodziny), technika (automatyzacja, AHT), jakość (błędy, SLA) | 1A działy |
| Analiza ankiety wg działów, Pytania ankietowe | Średnie Q01–Q23, rozkłady Q15/Q16/Q24/Q25/Q26 | dobrostan, AI |
| Ankieta szczegółowo, Lista pracowników | ⚠️ **dane osobowe (maile)** — tylko do agregacji per dział, nigdy do czatu AI | — |

## Przebieg minuta po minucie (55 min)

| Min | Analityk danych | Analityk ludzi i ryzyk | Strateg | Projektant / timekeeper | Decydent |
|---|---|---|---|---|---|
| 0–8 | Sanity-check: Σ przychodów 114,93 / FTE 720 / marża 8,39%; odkryj arkusz Pipeline | Otwiera Działy + ankietę | Czyta polecenie, rozpisuje 1A na osoby | Kopia pliku `HELVIA_E1_v1.xlsx` | Pilnuje: oceniany jest 1B |
| 8–25 | 1A klienci (14 flag) | 1A działy (8 flag) | Czat `analityk-operacji`: działy × procesy | Zbiera flagi do 1A | Czat `weryfikator`: przelicza sumy |
| 25–40 | Liczby do 1B (kary, koncentracja, pipeline) | Ankieta: eNPS, Q20, Q21, Q22 per dział | Szkic S1–S8 w 1B | Wpisuje 1B | Wybiera kandydatów na 3 priorytety |
| 40–48 | Sprawdza każdą liczbę w 1B w Excelu | Dopisuje „co sprawdzić” | 1C: 3 priorytety + zdanie diagnozy | Szkic slajdu 1 | Rozstrzyga w 1 min |
| 48–55 | — | — | Mentor: hipoteza + 3 liczby | Wpis do Rejestru decyzji | Akceptacja, „co pomijamy” |

## Wzór zdania do 1C / slajdu 1

> „HELVIA traci **[X mln zł / % EBIT]**, bo w **[dział]** rotacja **[Y%]** i SLA **[Z%]** uderzają w klientów generujących **[N%]** przychodu.”

## Pułapki E1

- **Arkusz Pipeline jest ukryty**, a Dashboard liczy tylko 9 z 22 szans — znalezienie tego to mocny dowód „czytaliśmy dane”.
- **Kary SLA:** 6,27 mln (Klienci/Dashboard) vs 8,36 mln (suma Historii) — używamy 6,27 i nazywamy rozbieżność w „co sprawdzić”.
- **Marże działów (21–53%) ≠ marża firmy 8,4%** — OPEX działów to tylko koszty osobowe.
- Korelacja rotacja × SLA (r = −0,86) jest ciągnięta przez jeden dział — mówimy „idzie w parze”, nie „powoduje”.
- W 1B nie wpisujcie samej nazwy klienta — oceniana jest **pełność wniosku** (fakt + fakt + interpretacja).

---

### ✅ DECYZJA DO PODJĘCIA PRZEZ ZESPÓŁ
Które **3 priorytety** z 1B przenosimy dalej i który sygnał świadomie pomijamy → arkusz 1C + wpis E1 w [`rejestr-decyzji.md`](../rejestr-decyzji.md).
