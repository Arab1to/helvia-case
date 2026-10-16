# Deck HELVIA — szkic v1 (dokładnie 3 slajdy)

Plik: [`slajdy/HELVIA_deck_v1.pptx`](slajdy/HELVIA_deck_v1.pptx) · generator: `python3 narzedzia/generuj_deck.py` · skrypt mówcy w notatkach prelegenta.

Mapowanie wg organizatora: **1C → slajd 1**, **2B → slajd 2**, **Etap 3 + Etap 4 („A co z ludźmi”) → slajd 3**.

| Slajd | Nagłówek-teza | Exhibit | Status |
|---|---|---|---|
| 1. Diagnoza | HELVIA traci 2/3 zysku operacyjnego na karach SLA — problemem jest jakość obsługi, nie cena | 3 KPI (6,27 mln = 65% EBIT · 94% kar od NORDY i Lumei · rotacja OK 24,5%) + łańcuch przyczyn + 3 priorytety | 1C w pliku pusty → priorytety do potwierdzenia |
| 2. Decyzja | Nie kupujemy lojalności NORDY rabatem — naprawiamy jakość i rośniemy tam, gdzie etat zarabia najwięcej | Tabela scenariuszy NORDY (0% / 4% / 4,6% / 12%) + kierunek S-03, S-20, S-14 + marża na etat 87 / 41 / 17 tys. zł | Zgodne z 2B (plik Etapu 2) |
| 3. Człowiek + AI + ludzie | AI przygotowuje, człowiek decyduje — przez rok zero zwolnień z powodu AI, a 36 etatów zdolności idzie w SLA i wzrost | Lewa: tabela 3+1 procesów, mini HITL P-014, kontrola i koszt 222 / 300 tys. zł. Prawa (E4): 96 et. objętych zmianą, 3 fazy z bramami, tabela 3 KPI (dziś → cel) | Zgodne z 3B/3C i 4A–4C; 36 et. do weryfikacji (3A w pliku E4) |

## Narracja
Kary SLA zjadają zysk (jakość, nie cena) → dlatego nie dajemy NORDZIE rabatu za darmo i rośniemy tam, gdzie etat zarabia najwięcej → AI zabiera rutynę tam, gdzie powstają kary i nadgodziny, a uwolniony czas idzie w jakość i wzrost, nie w zwolnienia.

## Do decyzji / weryfikacji przed finałem
- [ ] Slajd 1: potwierdzić 3 priorytety w 1C (propozycja: S1, S3, S8 z 1B).
- [ ] Slajd 2: data startu S-03 (24.12.2027 vs decyzja 15.11.2026); komórka 2B C24 pokazuje #NAME? (MINIFS).
- [x] Slajd 3: pierwsza fala (decyzja zespołu, 3B): **P-014** HITL/Hybryda, **P-012** HITL/Asystent, **P-001** automatyzacja/Hybryda; **P-015** zostaje u człowieka; mapa HITL w 3C dla **P-014**.
- [ ] Slajd 3: hipotezy −30% / −30% / −50% to założenie zespołu — przygotować 1 zdanie uzasadnienia na pytanie jury „skąd te procenty?”.
- [x] Slajd 3 / E4: fazy, bramy i 3 KPI z 4B/4C (decyzja zespołu).
- [ ] Slajd 3: **36 vs 16,4 etatu** — arkusz 3A w pliku E4 liczy godziny inaczej niż w pliku E3 (szczegóły: [`decyzje-E4.md`](../04_etap4_zmiana/decyzje-E4.md)). Potwierdzić z mentorem przed finałem; po decyzji usunąć tag w stopce slajdu 3.
- [ ] Slajd 3: odpowiedź na „SLA 95% powyżej maksimum z 12 mies. (94,5%)” i „wakaty z rotacji po mies. 6”.
- [ ] Skrypt: 378 słów ([`skrypt-3min.md`](skrypt-3min.md)), ale część 1:50–2:40 ma 138 słów na 50 s (≈ 165 słów/min) — przesunąć ~30 słów do Decydenta albo ciąć.
