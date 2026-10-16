# Etap 4 — decyzje zespołu (plik „FINAL_HIL - ETAP 4”, wersja AIvengers 1)

Źródło: arkusze 4A, 4B, 4C. Plik organizatora leży lokalnie w `dane/organizator/` i nie jest commitowany. Dane z ankiety wyłącznie jako średnie per dział (skala 1–5) lub odsetki działu.

## 4A — kogo dotyczy zmiana i co z uwolnionym czasem

| Proces | Kogo dotyczy | Jak zmienia się praca | Uwolniony czas → | Nowa rola | Ryzyko → ochrona |
|---|---|---|---|---|---|
| P-014 reklamacje (HITL, Hybryda, 10 kont) | ok. 15 et. konsultantów (w tym zespół NORDY) | sprawdzają propozycję AI, decydują o kategorii i priorytecie SLA | 709 h/m (4,4 et.) → szczyty XI–XII NORDY + wsparcie P-015 | lider jakości kwalifikacji (próbka 10%) | Q19 = 4,4 → ochotnicy, AI tylko proponuje, błąd AI nie obciąża pracownika |
| P-012 e-maile (HITL, Asystent, 45 kont) | ok. 44 et. konsultantów e-mail | redagują i zatwierdzają szkic AI; skargi i wyjątki samodzielnie | 2 119 h/m (13,2 et.) → telefony, szczyty NORDY, mniej nadgodzin | specjalista bazy wiedzy (2–3 os.) | bezrefleksyjne zatwierdzanie → „odpowiedź podpisuje człowiek”, próbka |
| P-001 faktury (automat, Hybryda, 10 kont) | ok. 37 et. w rejestracji faktur | obsługa wyjątków i kontrola reguł automatu | 2 962 h/m (18,5 et.) → 6,5 et. do S-01, reszta: nadgodziny + 2. fala (P-002) | koordynator wyjątków AP | 50% Finansów boi się o stanowisko (Q20 ≥ 4) → eksperci współprojektują reguły, ścieżka do AP DE |
| **Razem** | **96 et. = 13% firmy** (15 + 44 + 37; 96 / 720) | | **5 789 h/m = 36,2 et.** (hipoteza E3) | **3 role, z wewnątrz** | |

## 4B — rok zmiany

| Faza | Działanie → rezultat | Kto odpowiada | Brama (akceptacja / korekta) |
|---|---|---|---|
| Mies. 1–3 | Komunikat zarządu, **gwarancja: 0 zwolnień z powodu AI przez 12 mies.**, polityka AI | Zarząd + HR | Q21 ≥ 3,0 (dziś 2,3) w ankiecie pulsowej |
| Mies. 1–3 | Pilotaż P-014 i P-012 w zespole NORDY (ochotnicy, ok. 15 os. + 2 mentorów IT), pomiar bazowy | Kierownik OK | trafność AI ≥ 90%, SLA NORDY nie spada; < 85% → poprawa reguł przed rozszerzeniem |
| Mies. 4–6 | P-014 i P-012 na całą OK (55 kont) | Kierownik OK + liderzy zmian | SLA NORDY ≥ 93% (dziś 91,0%), kary w dół; jeśli nie → powrót do pilotażu |
| Mies. 4–6 | Automat P-001, przygotowanie 6,5 et. do S-01 | Kierownik Finansów | ≥ 75% faktur automatycznie, błędy ≤ 3,1% |
| Mies. 7–12 | Start S-01, zespół na szczyty XI–XII 2027, 2. fala (P-002, P-033) | Zarząd + HR | 0 zwolnień z powodu AI, SLA Finansów ≥ 96,2% |
| Mies. 7–12 | 3 nowe role obsadzone z wewnątrz, pełna ankieta | HR | Q20 w OK ≤ 3,5 (dziś 4,2) |

**Szkolenia (4B A6–A8):** konsultanci OK (ok. 59 et.): pilotaż z mentorami IT (73% IT przeszkolonych), potem warsztaty w parach i „godzina AI”. Księgowi AP: projektują reguły, potem szkolenie AP DE dla 6,5 et. Liderzy (12 os.): rozmowy 1:1 z HR w mies. 1–2.

## 4C — 3 rezultaty po 12 miesiącach

| Rezultat | KPI | Baza (źródło) | Cel 12 mies. | Pomiar pośredni | Właściciel | Korekta |
|---|---|---|---|---|---|---|
| Wynik | SLA NORDY · kary NORDA + Lumea · błędy P-014 | 91,0% (Historia_miesieczna) · 5,92 mln zł (Klienci: 4,93 + 0,99) · 6,9% (3A) | ≥ 95% · −50% (≈ 2,96 mln zł) · < 4% | co miesiąc, punkty kontrolne mies. 3 i 6 | Kierownik OK + KAM NORDY | brak poprawy po 3 mies. lub błędy > 6% → stop rozszerzania |
| Adopcja AI | aktywne konta · przeszkoleni · % faktur automatycznie | pomiar w mies. 1 · OK 9%, Finanse 17% (Q16) · — | ≥ 80% · 100% · ≥ 75% | logi tygodniowe, ankieta pulsowa mies. 3 i 6 | Lider zmiany OK + IT | aktywność < 50% po 3 mies. → sesje z mentorami |
| Ludzie | Q20 (obawa o pracę) · Q09 · Q21 · rotacja OK | 4,2 · 2,4 · 2,3 · 24,5% (ankieta, Działy) | ≤ 3,5 · ≥ 3,0 · ≥ 3,0 · ≤ 20% | ankieta pulsowa co kwartał, rotacja co miesiąc | HR + kierownicy OK i Finansów | rotacja rośnie 2 mies. z rzędu → wstrzymanie rozszerzania |

**Głos pracowników:** anonimowa ankieta pulsowa co kwartał (Q09, Q14, Q20, Q21, Q23), skrzynka pytań o AI (odpowiedź ≤ 5 dni), retrospektywy co 2 tygodnie w pilotażu, komitet zmiany co miesiąc (z przedstawicielem pracowników).

## Do weryfikacji przed finałem

1. **36 etatów a arkusz 3A w pliku E4.** Plik E3 miał w 3A wpisane godziny: P-001 5 924, P-012 7 062,1, P-014 2 361,9 h/m. W pliku E4 arkusz 3A liczy je formułą `SUMA.JEŻELI` z „Wolumeny klient proces” i daje 1 656,5 / 4 470,1 / 1 494,9 h/m. Przy tych samych hipotezach (−50% / −30% / −30%): 828,3 + 1 341,0 + 448,5 = **2 617,8 h/m = 16,4 etatu** (zamiast 36,2). Za wersją E4 przemawia czas na operację: P-001 = 1 656,5 × 60 / 14 200 = 7,0 min (AHT Finansów w „Działy” 8,5 min), a wersja E3 daje 31,8 min. **Potwierdźcie z mentorem, który 3A obowiązuje.**
2. **SLA NORDY ≥ 95%** jest powyżej maksimum z ostatnich 12 mies. (94,5%, 4B J14). To cel bez precedensu w danych — jury może zapytać, skąd pewność.
3. **Wakaty z rotacji (4A G19):** decyzja o ich obsadzaniu po mies. 6 (ok. 50 odejść/rok w OK = 24,5% × 208). Przygotujcie odpowiedź na „czy to redukcja przez rotację?”.
4. **Kary −50%** opisane jako „spójne z 2B” — sprawdźcie, która komórka 2B to pokazuje.
5. Arkusz „REJESTR SYGNAŁÓW (exc)” w pliku E4 ma w S1 wpis „lalaalla” — usuńcie przed oddaniem.
