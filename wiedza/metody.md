# Metody badawcze i analityczne

Każda metoda ma jedno zadanie: wyprodukować liczbę lub ranking, który da się pokazać jury. **Nie używajcie metody, której wyniku nie wstawicie na slajd.**

| Etap | Metoda | Pytanie | Wynik do slajdu |
|---|---|---|---|
| E1 | Analiza wskaźnikowa (benchmark wewnętrzny) | Który dział / klient odstaje od średniej firmy? | Odchylenie od mediany w % |
| E1 | Analiza Pareto 80/20 i ABC klientów | Ilu klientów robi 80% przychodu i marży? | Krzywa koncentracji, „top 3 = X%” |
| E1 | Heatmapa RAG | Gdzie kumulują się sygnały ostrzegawcze? | Tabela 8 działów w kolorach |
| E1 | Korelacja (WSP.KORELACJI / CORREL) | Czy rotacja idzie w parze ze spadkiem SLA? | Współczynnik r + 1 zdanie |
| E1 | Analiza ankiet (top-2-box, eNPS) | Gdzie ludzie są najbardziej zaniepokojeni AI? | % odpowiedzi 4–5 na skali |
| E1 | Drzewo problemu / 5×Dlaczego | Co jest przyczyną, a co objawem? | 1 przyczyna źródłowa |
| E2 | SWOT → TOWS | Jakie strategie łączą mocne strony z szansami? | 2–3 kierunki do macierzy |
| E2 | Wartość oczekiwana pipeline'u | Ile realnie jest wart pipeline? | Suma EV w mln zł |
| E2 | Test pojemności (capacity check) | Czy mamy FTE na nowe kontrakty? | Luka FTE |
| E2 | Macierz wielokryterialna z wagami | Który kierunek wybrać? | Ranking z punktacją |
| E2 | Analiza wrażliwości / scenariusze | Co jeśli założenie się nie sprawdzi? | Scenariusz pesym./bazowy/optym. |
| E3 | Scoring potencjał AI × ryzyko | Które procesy automatyzować najpierw? | Macierz 2×2 |
| E3 | Mapowanie procesu (SIPOC / swimlane) | Gdzie dokładnie wchodzi AI, a gdzie człowiek? | Mapa HITL |
| E3 | Business case: NPV-lite i payback | Kiedy wdrożenie się zwraca? | Payback w miesiącach |
| E4 | Mapa interesariuszy (siła × zainteresowanie) | Kogo trzeba przekonać, kogo informować? | Plan komunikacji |
| E4 | Model ADKAR (Świadomość → Pragnienie → Wiedza → Umiejętność → Utrwalenie) | Jak przeprowadzić ludzi przez zmianę? | Działania w 3 fazach |
| E4 | Rejestr ryzyk (prawdop. × wpływ) | Co może wykoleić plan? | Top 5 ryzyk + mitygacja |
| E5 | Zasada piramidy Minto (wniosek najpierw) | Jak ułożyć historię? | Teza w 1. zdaniu skryptu |
| E5 | Pre-mortem | „Przegraliśmy — dlaczego?” | Lista pytań jury |

## Trzy metody, które najczęściej odróżniają zwycięzców

- **Analiza wrażliwości.** Pokażcie, że rekomendacja wytrzymuje gorszy scenariusz (np. oszczędność FTE o 30% niższa). Jury rzadko to widzi, a pyta o to często.
- **Pre-mortem przed Etapem 5.** 5 minut: każdy pisze jeden powód porażki. To najszybszy generator pytań jury.
- **Triangulacja.** Każdy wniosek z E1 potwierdzony co najmniej dwoma źródłami (np. dane operacyjne + ankieta).

## Ściąga: interpretacja korelacji r

| |r| | Opis na slajd |
|---|---|
| < 0,3 | słaby związek — nie budujcie na tym tezy |
| 0,3–0,6 | umiarkowany związek |
| > 0,6 | silny związek (przy 8 działach nadal ostrożnie: „idzie w parze”, nie „powoduje”) |

Przy n = 8 działów korelacja jest wrażliwa na 1 punkt odstający — pokażcie też wykres punktowy.
