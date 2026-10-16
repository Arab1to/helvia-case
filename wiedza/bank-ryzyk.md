# Bank ryzyk

Prawdopodobieństwo i wpływ: **W** = wysokie, **Ś** = średnie, **N** = niskie — ocena wstępna do potwierdzenia na danych.

| Ryzyko | Prawd. | Wpływ | Mitygacja | Właściciel |
|---|---|---|---|---|
| Spadek SLA w okresie przejściowym | Ś | W | Pilot na 1 procesie, praca równoległa człowiek + AI przez 4–6 tygodni, Brama 1 | Dyrektor operacyjny |
| Naruszenie RODO / danych klientów | N | W | Aneks do umów powierzenia, minimalizacja danych, regulamin AI, DPIA dla procesów z danymi osobowymi | Radca prawny + IOD |
| AI w decyzjach kadrowych (AI Act) | Ś | W | Decyzje kadrowe zostają u człowieka; AI tylko jako wsparcie informacyjne | Dyrektor HR |
| Opór pracowników, spadek adopcji | W | Ś | Komunikacja przed pilotem, ambasadorzy, dialog z przedstawicielami pracowników, KPI adopcji | Dyrektor HR |
| Rotacja kluczowych osób przy rosnącym pipeline | Ś | W | Ścieżki kariery, premie za transfer wiedzy, dokumentacja procesów | Kierownicy działów |
| Klienci żądają rabatu | W | Ś | Oferta gain-sharing z mierzalnym KPI, rabat tylko warunkowy | Dyrektor handlowy |
| Koszty AI wyższe od planu | Ś | Ś | Test wrażliwości ±30%, licencje etapami, Brama 2 | CFO |
| Błędy AI (halucynacje, złe dopasowania) | Ś | Ś | Progi eskalacji, próbkowanie, tygodniowy raport błędów | Ambasador AI w dziale |
| Uzależnienie od jednego dostawcy | N | Ś | Klauzule wyjścia, eksport danych, standardowe integracje | CIO |

**Ryzyka prawne tylko sygnalizujcie** — jury nie oczekuje opinii prawnej, ale oczekuje, że wiecie, gdzie są granice.

## Macierz (do slajdu / Excela)

```
 Wpływ W │ RODO (N)              │ SLA przejściowe, AI Act, │
         │                       │ rotacja kluczowych (Ś)   │
 Wpływ Ś │ Vendor lock-in (N)    │ Koszty AI, błędy AI (Ś)  │ Opór, żądania rabatu (W)
         └──── Prawd. N ─────────┴──── Prawd. Ś ────────────┴──── Prawd. W ────
```
