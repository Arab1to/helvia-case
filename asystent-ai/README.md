# Asystent AI — zespół ekspertów w Claude (bez Hermesa)

Pracujemy **bez Hermes Agent**. Ten sam podział ról co w playbooku prowadzimy w **Claude**: jeden projekt „HELVIA” z wiedzą (playbook + to repo) i kilka równoległych czatów — każdy z innym promptem eksperta. **Decyzję zawsze podejmują ludzie** (HITL) — i to jest argument dla jury: pracowaliśmy dokładnie tak, jak rekomendujemy HELVII.

```
              ┌──────────────────────────────────────────────┐
              │ ZESPÓŁ 5 OSÓB — zatwierdza każdą decyzję     │
              │ Decydent rozstrzyga spory w 1 min            │
              └───────▲───────────────────────┬──────────────┘
          opcje + rekomendacja         zadanie etapu + agregaty
              ┌───────┴───────────────────────▼──────────────┐
              │ PROJEKT CLAUDE „HELVIA”                       │
              │ instrukcje: CLAUDE.md + 00-kontekst-case.md   │
              │ wiedza: playbook, wiedza/, prompty/           │
              └──────────────────────┬───────────────────────┘
          równoległe czaty — każdy członek zespołu prowadzi swój
  ┌──────────────────┬───────────────┴────┬─────────────────────┐
  │ Analityk danych  │ Analityk ludzi     │ Strateg             │
  │ → finansowy,     │ → ekspert HR,      │ → strateg,          │
  │   operacji       │   prawny           │   copywriter        │
  └────────┬─────────┴──────────┬─────────┴──────────┬──────────┘
           │   ┌───────┐        ▼                    │
           └──►│ EXCEL │──► czat WERYFIKATORA ◄──────┘
               │jedyne │    przelicza liczby, ocenia wg 10 kryteriów,
               │źródło │    wskazuje najsłabszy punkt
               └───────┘
```

Żaden wynik czatu nie trafia do decyzji bez weryfikacji: **liczby przelicza Analityk danych w Excelu**, a tekst ocenia czat z promptem `helvia-weryfikator`.

## Zawartość

| Plik | Co |
|---|---|
| [`setup.md`](setup.md) | Założenie projektu Claude dzień wcześniej (20–30 min) + test |
| [`plan-pracy.md`](plan-pracy.md) | Kto prowadzi który czat w którym etapie, okna czasowe, weryfikacja |
| [`szablon-zadania.md`](szablon-zadania.md) | Szablon wiadomości do czatu eksperta + gotowe zadania na każdy etap |
| [`prompty/`](prompty/) | `00-kontekst-case` (baza) + 7 ról: finansowy, operacji, strateg, HR, prawny, copywriter, weryfikator |

## Eksperci (prompty)

| Prompt | Kto go prowadzi | Etapy | Wyjście |
|---|---|---|---|
| `helvia-analityk-finansowy` | Analityk danych | E1, E2, E3 | Tabela: wzór + wynik (EBIT, rabaty, EV, payback) |
| `helvia-analityk-operacji` | Analityk danych | E1, E3 | Sygnały RAG, scoring potencjał × ryzyko |
| `helvia-strateg` | Strateg | E2, E4, E5 | Kierunki, „wybieramy X kosztem Y”, komunikacja |
| `helvia-ekspert-hr` | Analityk ludzi i ryzyk | E1, E4 | Ankieta, ADKAR, plan zmiany |
| `helvia-ekspert-prawny` | Analityk ludzi i ryzyk | E3, E4 | Lista ryzyk RODO / AI Act (tylko sygnalizacja) |
| `helvia-copywriter` | Projektant | E5 | Nagłówki slajdów, skrypt ≤ 390 słów |
| `helvia-weryfikator` | Decydent | każdy | Błędy, flagi [ZAŁOŻENIE], ocena 1–5, najsłabszy punkt |

## Zasady HITL (powiedzcie o nich jury)

1. AI proponuje opcje, zespół decyduje; decyzja trafia do Rejestru decyzji.
2. Żadna liczba nie trafia na slajd bez przeliczenia w Excelu przez Analityka danych.
3. Do modelu idą zagregowane dane, nigdy dane osobowe (maile, odpowiedzi pojedynczych osób, koszty imienne).
4. Gdy czaty / ludzie się nie zgadzają, Decydent rozstrzyga w 1 minutę.
5. **Plan B (brak internetu / limitów):** Excel + `narzedzia/kalkulator.py` offline, prompty jako checklisty pracy dla ludzi.
