# 3 hipotezy wyjściowe do weryfikacji

To są **hipotezy, nie wnioski**. Każdą potwierdzacie albo obalacie danymi w pierwszych minutach etapu, którego dotyczy — obalona hipoteza też jest wynikiem, który warto pokazać.

| # | Hipoteza | Jak sprawdzić (etap, formuła) | Jeśli się potwierdzi | Jeśli się nie potwierdzi | Status |
|---|---|---|---|---|---|
| **H1** | Problemy są skoncentrowane: 1–2 działy z najwyższą rotacją odpowiadają za większość naruszeń SLA i obsługują klientów o największym udziale w przychodzie. | E1: `WSP.KORELACJI` rotacja × SLA, `SUMA.JEŻELI` przychodu per dział | Kierunek „Jakość” — naprawa SLA tam, gdzie wisi największy przychód | Problem rozproszony → kierunek „Efektywność” w całym back-office | ✅ potwierdzona na danych E1 ([analiza](../01_etap1_diagnoza/analiza-E1.md)) |
| **H2** | Pipeline'u nie da się zrealizować obecnymi zasobami, a procesy back-office mają największy potencjał AI — więc AI może „sfinansować” wzrost uwolnionymi FTE. | E2: luka FTE; E3: suma oszczędności FTE z pierwszej fali | Teza „AI finansuje wzrost bez zwolnień” | Brak luki → uwolnione FTE na SLA i ofertę premium | ◐ wstępnie: pipeline 113 FTE (54 ważone) — policzyć w E2 |
| **H3** | Rabat bezwarunkowy niszczy więcej wartości niż ryzyko odejścia klientów; gain-sharing lub wyższe SLA dominują. | E2: koszt 1–2 pp rabatu vs marża pokrycia klientów z wysokim ryzykiem odejścia | Odrzucona opcja rabatu jako jawny trade-off na slajdzie | Rabat warunkowy dla 1–2 kluczowych klientów, z ceną za dłuższy kontrakt | ⏳ |

## Test H3 — szybki rachunek

Rabat bezwarunkowy jest uzasadniony tylko, jeśli **koszt rabatu < oczekiwana utracona marża pokrycia**:

```
koszt rabatu    = d × 114,93 mln zł                     (np. 2 pp → 2,30 mln zł)
utracona marża  = Σ (p_odejścia_i × przychód_i × marża_pokrycia_i)   dla klientów zagrożonych
```

`python3 narzedzia/kalkulator.py prog-rabatu --marza-pokrycia 0.25` → przy jakiej skali odejść rabat zaczyna się opłacać.
