# Etap 3 — decyzje zespołu (plik „FINAL_HIL - ETAP 3”, wersja AIvengers 3)

Źródło: arkusze 3B i 3C. Plik organizatora leży lokalnie w `dane/organizator/` i nie jest commitowany.

| Proces | Tryb · model AI | Godz./m (3A) | Hipoteza | Uwolnione h/m | Etaty (÷160) | Rok 1 (zł) |
|---|---|---|---|---|---|---|
| P-014 Rejestracja i kwalifikacja reklamacji | HITL · Hybryda (10 kont, 100% op.) | 2 361,9 | −30% | 708,57 | 4,4 | 67 515 |
| P-012 Odpowiedzi na e-maile klientów | HITL · Asystent (45 kont) | 7 062,1 | −30% | 2 118,63 | 13,2 | 72 160 |
| P-001 Rejestracja faktur zakupowych | Automatyzacja · Hybryda (10 kont, 80% op.) | 5 924 | −50% | 2 962 | 18,5 | 82 038 |
| P-015 Rozpatrywanie reklamacji złożonych | **zostaje u człowieka** | — | — | — | — | — |
| **Razem** | | **15 348** (D22) | | **5 789,2** (H22) | **36,2** (L22) | **221 713** z 300 000 (B39) |

**Wzory (Excel):** uwolnione h/m = `G × H` (np. P-014: 2 361,9 × 0,3 = 708,57) · etaty = `H22 / 160` = 36,18 · Hybryda rok 1 = `(konta × 89 + operacje × 0,4 + 1 200) × 12 + 14 000` (P-014: (890 + 2 369,6 + 1 200) × 12 + 14 000 = 67 515,2) · Asystent rok 1 = `konta × 129 × 12 + 2 500` (45 × 129 × 12 + 2 500 = 72 160).

## Mapa HITL — P-014 (3C)

| Krok | Kto | Co | Próg / eskalacja |
|---|---|---|---|
| 1 Start | System | zgłoszenie do jednej kolejki, start zegara SLA | — |
| 2 Analiza | AI | rozpoznaje klienta, zamówienie, produkt; karta + lista braków | brak pewnego dopasowania → konsultant |
| 3 Działanie | AI + człowiek | prośba o uzupełnienie, konsultant zatwierdza wysyłkę | NORDA lub spór → kontakt osobisty |
| 4 Analiza | AI | kategoria + priorytet SLA z poziomem pewności | pewność < 80% → kwalifikacja ręczna |
| 5 **Decyzja** | **Konsultant** | zatwierdza lub zmienia kategorię i priorytet | bezpieczeństwo produktu, wysoka wartość, po gwarancji, brak dowodu, spór → krok 6 |
| 6 Wyjątek | Specjalista ds. reklamacji | przejęcie z podsumowaniem AI → P-015 | ryzyko prawne / wysoki koszt → przełożony / dział prawny |
| 7 Działanie | System | rejestracja w CRM Helios, przypisanie zespołu | < 24 h do SLA → alert do lidera |
| 8 Kontrola | Kierownik OK | próbka 10% tygodniowo | trafność < 90% lub wzrost reklamacji NORDY → wstrzymanie AI |

**Efekt (3C D20):** czas kwalifikacji −30% (2 362 → ok. 1 650 h/m), błędy 6,9% → < 4%.

## Przekazanie do Etapu 4 (3B B44–B46, skrót)
- **Kogo dotyczy:** OK ok. 59 etatów w procesach objętych zmianą (44 e-mail + 15 reklamacje), 55 kont AI; Finanse ok. 37 etatów w rejestracji faktur, 10 kont AP; IT — konfiguracja i nadzór.
- **Szkolenia:** weryfikacja propozycji AI, ocena pewności, korekta, kategorie i priorytety SLA; dla liderów kontrola próbki. Dziś przeszkolonych z AI: OK 9%, Finanse 17%.
- **Ryzyko nr 1:** lęk o pracę → odejścia przed wdrożeniem (OK: 82% boi się o stanowisko, 38% nie widzi się w firmie za rok; r = −0,68). Zabezpieczenie: „odciążenie, nie redukcja” przed pilotażem, gwarancja ról, szkolenia przed startem, liderzy zmian z OK.

## Najsłabszy punkt
36 etatów to **zdolność z hipotezy** (−30/−30/−50%), a nie zmierzony efekt. Do tego koszt 222 tys. zł nie obejmuje szkoleń ani czasu nadzoru (3B A41). Jury zapyta „skąd 30%?” — w E4 potrzebny pilotaż z bazą i bramą decyzyjną.
