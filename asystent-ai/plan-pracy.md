# Plan pracy z Claude na etapy

Jedna „fala” = **3 osoby, każda w swoim czacie z innym promptem**, potem czat weryfikatora. Liczby zawsze wracają do Excela.

| Etap | Równolegle (osoba → prompt → zadanie) | Weryfikacja | Okno dla AI |
|---|---|---|---|
| E1 · 55 min | Analityk danych → `analityk-finansowy`: klienci · Strateg → `analityk-operacji`: działy · Analityk ludzi → `ekspert-hr`: ankieta | Decydent → `weryfikator`: czy sumy FTE i przychodów się domykają, najsłabszy wniosek w 1B | min 10–35 |
| E2 · 45 min | Analityk danych → `analityk-finansowy`: EV pipeline + opcje cenowe · Analityk ludzi → `analityk-operacji`: test pojemności · Strateg → `strateg`: macierz 3 kierunków | `weryfikator`: trade-off i Trójkąt | min 10–30 |
| E3 · 70 min | Analityk danych → `analityk-operacji`: scoring procesów · Strateg → `analityk-finansowy`: business case · Analityk ludzi → `ekspert-prawny`: ryzyka procesów | `weryfikator` + przeliczenie w Excelu | min 15–50 |
| E4 · 70 min | Analityk ludzi → `ekspert-hr`: harmonogram i szkolenia · Strateg → `strateg`: komunikacja · Decydent → `ekspert-prawny`: ryzyka zmiany | `weryfikator`: czy każdy KPI ma bazę | min 15–50 |
| E5 | Projektant → `copywriter`: slajdy · Strateg → `copywriter`: skrypt · Decydent → `weryfikator`: 8 pytań jury | Timekeeper (człowiek, stoper) | — |

## Rytm w etapie

1. **0–15% czasu** — Analityk danych przygotowuje agregaty (tabele per klient / dział) do wklejenia; każdy otwiera swój czat.
2. **15–75%** — praca równoległa; ludzie liczą to samo w Excelu (AI przyspiesza, nie zastępuje).
3. **75–90%** — czat weryfikatora: przeliczenie, flagi `[ZAŁOŻENIE]`, najsłabszy punkt, ocena 1–5.
4. **90–100%** — zespół decyduje, mentor, wpis do [`rejestr-decyzji.md`](../rejestr-decyzji.md).

Treści zadań: [`szablon-zadania.md`](szablon-zadania.md).
