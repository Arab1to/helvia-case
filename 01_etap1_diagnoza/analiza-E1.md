# Analiza danych E1 — propozycja asystenta (do decyzji zespołu)

Źródło: `HITL_Etap_1.xlsx` od organizatora (dane 01.10.2025–30.09.2026). Każdą liczbę odtwarza `python3 narzedzia/analiza_e1.py dane/organizator/HITL_Etap_1.xlsx`.
Wypełniona propozycja arkuszy 1A/1B/1C: `dane/organizator/HITL_Etap_1_propozycja.xlsx` (poza gitem — zawiera dane osobowe organizatora).

> **Status:** to propozycja do decyzji zespołu (HITL). Przed oddaniem: Analityk danych sprawdza liczby w Excelu, zespół wybiera 3 priorytety, mentor ocenia najsłabszy punkt.

## Diagnoza w jednym zdaniu (propozycja)

> „HELVIA traci **6,27 mln zł rocznie (65% EBIT)** na karach SLA, bo w **Obsłudze Klienta** rotacja **24,5%** i SLA **92,1%** uderzają w klientów, którzy dają **29% przychodu** — a kontrakt NORDY (**23%**) kończy się **31.12.2026**.”

## 5 liczb, które trzeba znać

| Liczba | Wartość | Źródło |
|---|---|---|
| Kary SLA vs EBIT | 6,27 mln zł = **65% EBIT** (9,64 mln); bez kar marża 13,8% zamiast 8,4% | Dashboard!A8, Klienci!H |
| Koncentracja kar | NORDA 4,93 mln (**79%**) + Lumea 0,99 mln → razem **94%** kar | Klienci!N2, N9 |
| Odnowienia w 6 mies. | NORDA (31.12.2026), Sørvik, Ibera (31.03.2027) = **32,6 mln zł (28,4%)** | Klienci!E, Dashboard!D8 |
| Obsługa Klienta | rotacja **24,5%** (2,7× mediany 9,0%), SLA **92,1%**, **53%** wszystkich błędów, eNPS **−64** | Działy!E19, D41, C41; ankieta |
| Pipeline (ukryty arkusz) | **22 szanse, EV 27,1 mln zł, 113 FTE** — dashboard pokazuje tylko 9 (13,1 mln, 50 FTE) | Pipeline, Dashboard!J8, M8 |

## Łańcuch przyczyn (5 × Dlaczego)

```
EBIT tylko 8,4%  ←  kary SLA 6,27 mln (65% EBIT)  ←  SLA poniżej umów u NORDY (91,0%) i Lumei (92,4%)
   ←  obsługuje je głównie Obsługa Klienta (NORDA 61 FTE-ekw., Lumea 27)  ←  rotacja 24,5%, 34% juniorów,
      23% ze stażem < 1 rok, 1 420 błędów  ←  przeciążenie (Q09: 12% „do udźwignięcia”), niska automatyzacja 22%,
      brak szkoleń AI (9%), lęk o etat (82%)
```

Przyczyna źródłowa: **przeciążony, rotujący i nieprzeszkolony zespół Obsługi Klienta przy ręcznych, powtarzalnych procesach** (82% deklaruje ≥ 60% zadań powtarzalnych) — nie cena i nie klient.

## Hipotezy z playbooka — weryfikacja

| # | Hipoteza | Wynik na danych |
|---|---|---|
| H1 | Problemy skoncentrowane w 1–2 działach z najwyższą rotacją, które obsługują największych klientów | ✅ **Potwierdzona.** Obsługa Klienta: najwyższa rotacja, najniższe SLA, 53% błędów; obsługuje NORDĘ (23% przychodu) i Lumeę → 94% kar. r(rotacja, SLA) = −0,86 dla 8 działów (bez Obsługi Klienta −0,61 — jeden dział ciągnie korelację; mówić „idzie w parze”) |
| H2 | Pipeline nie do zrealizowania obecnymi zasobami; back-office ma największy potencjał AI | ✅ **Wstępnie potwierdzona.** Pipeline wymaga 113 FTE (54 ważone), działy już z nadgodzinami; procesy faktur (P-001 + P-002) = 63 FTE-ekw. → do policzenia w E2/E3 |
| H3 | Rabat bezwarunkowy niszczy więcej, niż chroni | ⏳ E2. Punkt wyjścia: 1 pp rabatu u NORDY = 0,26 mln zł, a jej kary to 4,93 mln — rabat nie rozwiązuje przyczyny |

## 1A — flagi (propozycja; flagi z list organizatora)

### Klienci

| Klient | Flaga | Kluczowy dowód |
|---|---|---|
| NORDA Logistics | **Wysokie ryzyko odejścia** | 23% przychodu, kontrakt do 31.12.2026, NPS 18, wolumen −3,2%, kary 4,93 mln (79%), marża 4,6% vs 23,3% przed karami |
| Brumark Retail Group | Potencjał na zmniejszenie kosztów obsługi | 72 FTE-ekw. (2. miejsce), 112 zł przychodu/h vs 126 średnio, 316 reklamacji |
| Velmont Insurance | Potencjał do zwiększenia marży | Marża 13%, NPS 55, +9,1%, udział w portfelu 40%, S-04 4,6 mln |
| Kastella Pharma | Potencjał do zwiększenia marży | Marża 14,5%, +12,3%, NPS 62, S-01 = największa EV 2,93 mln |
| Orvis Energy | Potencjał na zmniejszenie kosztów obsługi | Najniższy przychód/h 88 zł, marża 7,6%, kontrakt do 30.06.2027 |
| Delfino Foods | Klient niskomarżowy | Marża 5,9%, kary 232 tys., SLA 92,5%, NPS 25 |
| Hartberg Manufacturing | Potencjał do zwiększenia marży | Marża 10,8%, NPS 48, 185 zł/h, S-10 1,5 mln |
| Lumea Telecom | **Wysokie ryzyko odejścia** | NPS 12, wolumen −6,3%, kary 0,99 mln = 14,9% przychodu, marża 3,2%; ale SLA rośnie (IX: 95,7%, 0 kar) |
| Pilawa Banking Services | Potencjał do zwiększenia marży | SLA 97,4%, marża 13,5%, 315 zł/h, udział w portfelu 30%, S-14 80% |
| Sørvik Marine | Klient niskomarżowy | Marża 2,1%, kontrakt do 31.03.2027, 1,86 reklamacji/1000 operacji (najwięcej) |
| Trelia Home | Potencjał do zwiększenia marży | +7,9%, NPS 45, S-05 + S-19 EV 1,93 mln |
| Quenta Analytics | Potencjał do zwiększenia marży | Marża 17,9%, +34,2%, 233 zł/operację, 938 zł/h |
| Ibera Travel | **Wysokie ryzyko odejścia** | Jedyna ujemna marża −1,8%, NPS −15, wolumen −18,4%, SLA 90,1%, kontrakt do 31.03.2027 |
| Nordkap Ventures | Potencjał do zwiększenia marży | Marża 18,6%, +41,5%, NPS 70, 337 zł/operację |

### Działy

| Dział | Flaga | Kluczowy dowód |
|---|---|---|
| Finanse i Księgowość | Niski poziom dobrostanu | 140,2 h nadgodzin/mies. (najwięcej), Q09 18%, eNPS −39; 63% pracy powtarzalnej; P-001 + P-002 = 63 FTE-ekw. |
| HR i Payroll | Dział wysokowydajny | SLA 98,5%, 120 błędów, rotacja 8,2% |
| IT i Wsparcie Techniczne | Dział o zbyt wysokich kosztach | 14,0 tys. zł/etat vs 9,0 średnio, marża działu 21,4%; **ale** najwyższa gotowość AI (34% codziennie, 73% po szkoleniu) |
| Marketing | Dział wysokowydajny | SLA 99,0%, 45 błędów, rotacja 6,7% |
| Obsługa Klienta | **Dział o wysokiej rotacji** | 24,5% (2,7× mediany), SLA 92,1%, 53% błędów, eNPS −64, 38% chce odejść |
| Operacje i Logistyka | Dział zacofany technicznie | Automatyzacja 28%, AHT 47,5 min, SLA 94,5%, 59% nigdy nie używa AI; pipeline 35,5 FTE |
| Sprzedaż i Key Account | Dział o wysokich zyskach | Marża działu 48%, SLA 98,2%; oferty 157 min/szt. (17,8 FTE-ekw.) |
| Zarząd i Administracja | Dział o zbyt wysokich kosztach | 5,06 mln OPEX, 17,6 tys./etat (2× średniej), automatyzacja 15%; 0% widzi jasną komunikację AI |

## 1B — 8 głównych wniosków (oceniany arkusz)

| ID | Wniosek | Rodzaj |
|---|---|---|
| S1 | Kary SLA zjadają 65% EBIT (6,27 vs 9,64 mln); bez kar marża 13,8% zamiast 8,4% — problem jakości, nie ceny | Problem |
| S2 | 28,4% przychodu (32,6 mln) do odnowienia w 6 mies., w tym NORDA (23%) 31.12.2026 przy NPS 18 | Problem |
| S3 | Obsługa Klienta = źródło problemów: rotacja 24,5%, SLA 92,1%, 53% błędów — i obsługuje klientów płacących 94% kar | Problem |
| S4 | Pipeline 2× większy niż na dashboardzie: 22 szanse, EV 27,1 mln, ale 113 FTE, których nie ma | Szansa |
| S5 | Finanse: największy potencjał automatyzacji (nadgodziny 140 h, 63% powtarzalnej pracy, faktury = 63 FTE) + 25 FTE popytu z pipeline'u | Szansa |
| S6 | 88% chce szkoleń AI, przeszkolonych 30%, jasną komunikację AI widzi 7% — opór to brak komunikacji, nie niechęć | Mieszany |
| S7 | Ogon nierentownych klientów (Ibera, Sørvik, Lumea): 12,9 mln przychodu przy marży 2,1%; 2 kontrakty kończą się w III 2027 | Problem |
| S8 | Usługi analityczne/premium (Quenta, Nordkap): marże 18–19%, wzrost 34–42%, 10–14× wyższy przychód/h niż NORDA | Szansa |

Pełne fakty, interpretacje i „co sprawdzić” — w pliku propozycji (arkusz 1B).

## 1C — 3 priorytety (propozycja)

| Ranga | ID | Dlaczego |
|---|---|---|
| 1 | S1 (+S2) | Największa dźwignia EBIT (65%) i warunek odnowienia NORDY |
| 2 | S3 | Przyczyna źródłowa kar — bez naprawy Obsługi Klienta nie naprawimy SLA |
| 3 | S5 | Najszybsze uwolnienie FTE na pipeline (H2: „AI finansuje wzrost bez zwolnień”) |

**Świadomie pomijamy:** S7 (wrócimy przy odnowieniach w III 2027), S8 (rozwiniemy w E2 jako kierunek wzrostu). S4 i S6 to warunki realizacji, nie osobne priorytety.

Alternatywa do rozważenia przez zespół: S2 (NORDA) jako osobny priorytet nr 1 — mocniejsza narracja „pilne”, ale słabsza „przyczynowa”.

## ⚠️ Niespójności w danych — zapytać mentora

| # | Co | Liczby | Znaczenie |
|---|---|---|---|
| 1 | Kary SLA | Klienci: **6,27 mln** vs Historia miesięczna: **8,36 mln** | Jeśli 8,36 — kary = 87% EBIT; używamy 6,27 (dashboard) i mówimy o rozbieżności |
| 2 | Przychód, reklamacje | Historia: 115,87 mln / 3 153 vs Klienci: 114,93 mln / 2 739 | Historia ≠ dane roczne; cytujemy Klienci |
| 3 | Dashboard pipeline | Liczy S-01…S-09, arkusz Pipeline (ukryty) ma 22 szanse | Pipeline niedoszacowany o połowę |
| 4 | OPEX działów | Σ OPEX = 78,08 mln = koszty osobowe (6,51 mln × 12) | Marże działów (21–53%) to marża na kosztach osobowych, nie porównywalna z 8,4% |
| 5 | Nadgodziny | Finanse 140,2 h/mies. | Na osobę nierealne — pewnie suma działu lub inna jednostka |
| 6 | FTE w pipeline | 509 tys. zł przychodu/FTE vs 160 tys. dziś | Zapotrzebowanie na FTE prawdopodobnie zaniżone (3,2×) |
| 7 | Ankieta | Zwrot w Obsłudze Klienta 57% (najniższy) | Niezadowolenie może być niedoszacowane |
| 8 | Format | AHT zarządu „67,3 min” jako tekst (Działy!D33); segment „Strategiczny” w Historii vs „Duży” w Klientach | Drobne — pokazuje, że czytaliśmy dane |
| 9 | Brakujące kolumny | „Ryzyko odejścia” i „FTE zaangażowane” opisane w „Info do tabeli klienci”, ale nie ma ich w tabeli | Ryzyko odejścia ocenialiśmy sami (NPS, wolumen, kontrakt) |

## Ludzie — fakty pomocnicze

- 720 osób, **76% poniżej 35 lat**, tylko 4% powyżej 45 — firma bardzo młoda (przy rotacji brakuje doświadczenia).
- Zgoda na tezę „AI może mi pomóc” (Q18): IT 93%, Marketing 95%, Zarząd 95% vs Obsługa Klienta 22%, Operacje 33%.
- Bariery AI (Q25): brak szkoleń 23%, brak jasnych zasad 21%, brak czasu 20%, obawa o stanowisko 18%.
- Co zostawić człowiekowi (Q26): kontrola jakości 21%, trudne rozmowy z klientem 19%, decyzje finansowe 17%, decyzje kadrowe 16% → gotowe argumenty do E3 („zostawiamy człowiekowi”).

## Propozycja wpisu E1 do Rejestru decyzji

| Etap | Decyzja | Kosztem czego | Kluczowa liczba | Źródło | Akceptacja mentora |
|---|---|---|---|---|---|
| E1 | Priorytety: (1) jakość SLA u NORDY i Lumei, (2) Obsługa Klienta — ludzie i procesy, (3) automatyzacja back-office Finansów pod pipeline | Odkładamy ogon nierentownych klientów i usługi premium | Kary 6,27 mln = 65% EBIT | Dashboard!A8 | _zespół wpisuje_ |
