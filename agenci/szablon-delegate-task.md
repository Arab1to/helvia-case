# Szablon zadania dla subagenta

Subagent **nie zna case'u**, więc orkiestrator musi przekazać mu wszystko w `goal` i `context`.

```yaml
goal: [jedno zadanie, np. „Policz udział i sygnał RAG dla 14 klientów”]
context:
  ROLA: Jesteś [ekspert] w zespole case solvingu HELVIA Polska (BPO, 720 os., 14 klientów,
        przychód 114,93 mln zł, marża 8,4%).
  DANE: [nagłówki kolumn + zagregowane wiersze z Excela, bez danych osobowych]
  ZASADY: Nie wymyślaj liczb. Liczbę spoza danych oznacz [ZAŁOŻENIE] + sposób weryfikacji.
          Pokaż wzór i wynik.
  KRYTERIA JURY: teza w 1 zdaniu, liczby z Excela, trade-off, Trójkąt Dobrostanu, HITL, KPI z bazą.
  FORMAT: tabela markdown + max 3 zdania wniosku + 1 najsłabszy punkt.
```

**Skill bazowy:** cały prompt z `prompt_helvia_case.md` zapisany jako skill `helvia-juror` — orkiestrator ładuje go na starcie, a sekcje `case_context`, `metrics` i `evaluation_criteria` wkleja do `context` każdego subagenta.

---

## Gotowe `goal` na każdą falę

### E1 — Diagnoza
| Subagent | goal |
|---|---|
| `helvia-analityk-finansowy` | Policz dla 14 klientów: udział w przychodzie, udział skumulowany (Pareto), marżę vs 8,4%, sygnał RAG wg progów; podaj „top 3 = X%”. |
| `helvia-analityk-operacji` | Zbuduj tabelę 8 działów: FTE, obciążenie, SLA vs umowa, rotacja vs mediana; nadaj sygnał RAG; policz r(rotacja, SLA). |
| `helvia-ekspert-hr` | Z zagregowanych wyników ankiet policz top-2-box obawy przed AI per dział i wskaż działy, gdzie obawa i rotacja nakładają się. |
| `helvia-weryfikator` | Sprawdź: Σ FTE = 720, Σ przychodów = 114,93 mln zł, EBIT = 9,65 mln zł; wskaż najsłabszy punkt diagnozy. |

### E2 — Strategia
| Subagent | goal |
|---|---|
| `helvia-analityk-finansowy` | Policz EV pipeline'u (Σ wartość × p) oraz wpływ na EBIT opcji a)–d) i rabatu bezwarunkowego 1 i 2 pp. |
| `helvia-analityk-operacji` | Test pojemności: FTE potrzebne na kontrakty z pipeline'u vs dostępne w działach realizujących; luka FTE. |
| `helvia-strateg` | Oceń 3 kierunki (Jakość / Efektywność / Wzrost) w macierzy 30/20/25/25 i 25/25/25/25; zaproponuj zdanie „Wybieramy X kosztem Y” z warunkiem powrotu. |
| `helvia-weryfikator` | Oceń trade-off: czy „kosztem” jest realnym kosztem? Czy każdy wierzchołek Trójkąta ma argument z liczbą? |

### E3 — Człowiek + AI
| Subagent | goal |
|---|---|
| `helvia-analityk-operacji` | Oceń procesy z kart (1–5): potencjał (5 kolumn) i ryzyko (5 kolumn); przypisz ćwiartki; zaproponuj 2+1+1. |
| `helvia-analityk-finansowy` | Business case dla 3 procesów: koszt licencji, wdrożenie, szkolenia, FTE uwolnione, payback prosty i netto, wariant −30%. |
| `helvia-ekspert-prawny` | Dla 4 wybranych procesów zasygnalizuj ryzyka RODO / AI Act / umów powierzenia i wskaż kroki wymagające człowieka. |
| `helvia-weryfikator` | Przelicz business case; sprawdź, czy proces nr 3 wspiera priorytet z E2; czy HITL ma próg i właściciela w każdym kroku. |

### E4 — Roczna zmiana
| Subagent | goal |
|---|---|
| `helvia-ekspert-hr` | Harmonogram 3 faz × strumienie (HR, IT, Prawo, Finanse, Klienci, Motywacja) wg ADKAR; plan szkoleń w 3 poziomach. |
| `helvia-strateg` | Plan komunikacji: zarząd / pracownicy / klienci — przekaz, kanał, termin, kto mówi; mapa interesariuszy. |
| `helvia-ekspert-prawny` | Ryzyka zmiany: dialog z przedstawicielami pracowników, regulamin AI, AI Act w HR; mitygacja i właściciel. |
| `helvia-weryfikator` | Czy każdy KPI ma bazę z Excela, cel 12 mies., źródło i właściciela? Czy progi bram wynikają z KPI? |

### E5 — Prezentacja
| Subagent | goal |
|---|---|
| `helvia-copywriter` | Z rejestru decyzji napisz 3 nagłówki-tezy slajdów (≤ 30 słów treści na slajd). |
| `helvia-copywriter` | Uzupełnij skrypt 3:00 z rejestru decyzji; ≤ 390 słów; policz słowa per mówca. |
| `helvia-weryfikator` | Pre-mortem: 8 najtrudniejszych pytań jury + odpowiedź w 2–3 zdaniach z liczbą. |
