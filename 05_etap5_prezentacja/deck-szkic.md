# Deck HELVIA — szkic v1 (dokładnie 3 slajdy)

Plik: [`slajdy/HELVIA_deck_v1.pptx`](slajdy/HELVIA_deck_v1.pptx) · generator: `python3 narzedzia/generuj_deck.py` · skrypt mówcy w notatkach prelegenta.

Mapowanie wg organizatora: **1C → slajd 1**, **2B → slajd 2**, **Etap 3 + Etap 4 („A co z ludźmi”) → slajd 3**.

| Slajd | Nagłówek-teza | Exhibit | Status |
|---|---|---|---|
| 1. Diagnoza | HELVIA traci 2/3 zysku operacyjnego na karach SLA — problemem jest jakość obsługi, nie cena | 3 KPI (6,27 mln = 65% EBIT · 94% kar od NORDY i Lumei · rotacja OK 24,5%) + łańcuch przyczyn + 3 priorytety | 1C w pliku pusty → priorytety do potwierdzenia |
| 2. Decyzja | Nie kupujemy lojalności NORDY rabatem — naprawiamy jakość i rośniemy tam, gdzie etat zarabia najwięcej | Tabela scenariuszy NORDY (0% / 4% / 4,6% / 12%) + kierunek S-03, S-20, S-14 + marża na etat 87 / 41 / 17 tys. zł | Zgodne z 2B (plik Etapu 2) |
| 3. Człowiek + AI + ludzie | AI przygotowuje, człowiek decyduje: 3 procesy z AI, reklamacje złożone zostają u ludzi — 36 etatów zdolności idzie w SLA i wzrost, nie w zwolnienia | Tabela 3+1 procesów (P-014, P-012, P-001 + P-015), mini HITL P-014, kontrola 10% / próg 90%, koszt 222 / 300 tys. zł; panel E4: 36 etatów, gdzie trafia czas, szkolenia, ryzyko nr 1, KPI | Zgodne z 3B/3C (plik Etapu 3, wersja AIvengers 3); panel E4 do uzupełnienia |

## Narracja
Kary SLA zjadają zysk (jakość, nie cena) → dlatego nie dajemy NORDZIE rabatu za darmo i rośniemy tam, gdzie etat zarabia najwięcej → AI zabiera rutynę tam, gdzie powstają kary i nadgodziny, a uwolniony czas idzie w jakość i wzrost, nie w zwolnienia.

## Do decyzji / weryfikacji przed finałem
- [ ] Slajd 1: potwierdzić 3 priorytety w 1C (propozycja: S1, S3, S8 z 1B).
- [ ] Slajd 2: data startu S-03 (24.12.2027 vs decyzja 15.11.2026); komórka 2B C24 pokazuje #NAME? (MINIFS).
- [x] Slajd 3: pierwsza fala (decyzja zespołu, 3B): **P-014** HITL/Hybryda, **P-012** HITL/Asystent, **P-001** automatyzacja/Hybryda; **P-015** zostaje u człowieka; mapa HITL w 3C dla **P-014**.
- [ ] Slajd 3: hipotezy −30% / −30% / −50% to założenie zespołu — przygotować 1 zdanie uzasadnienia na pytanie jury „skąd te procenty?”.
- [ ] Slajd 3 / E4: cele KPI, plan szkoleń, podział 36 etatów (szczyty i SLA / S-01 6,5 et. / projekty kierunku 8,6 et. / rotacja).
- [ ] Skrypt: obecnie ok. 394 słowa w notatkach (limit ~390) — po dopisaniu E4 trzeba ciąć — przeczytać na głos z zegarem.
