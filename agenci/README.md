# Zespół ekspertów AI — orkiestracja Hermes Agent

Hermes Agent zamienia 5-osobowy zespół w **5 osób + 7 wirtualnych ekspertów**: orkiestrator rozdziela zadanie etapu na subagentów, weryfikator przelicza ich wyniki, a **decyzję zawsze podejmują ludzie**. To ten sam HITL, który pokazujecie jury — sposób pracy staje się dodatkowym argumentem w prezentacji.

```
                 ┌──────────────────────────────────────┐
                 │ ZESPÓŁ 5 OSÓB — zatwierdza każdą     │
                 │ decyzję (HITL)                       │
                 └───────▲──────────────────┬───────────┘
          opcje + rekomendacja       zadanie etapu + dane
                 ┌───────┴──────────────────▼───────────┐
                 │ ORKIESTRATOR: Hermes Agent           │◄──────────────┐
                 │ skill helvia-juror · pamięć · rejestr│               │
                 └──────────────────┬───────────────────┘               │
            delegate_task · izolowany kontekst · do 5 naraz             │ raport + flagi
  ┌────────────────────┬────────────┴────────┬────────────────────┐     │ [ZAŁOŻENIE]
  │ Analityk finansowy │ Analityk operacji   │ Strateg            │     │
  │ EBIT, rabaty,      │ BPO: FTE, SLA,      │ TOWS, macierz      │     │
  │ payback            │ scoring procesów    │ kierunków          │     │
  ├────────────────────┼─────────────────────┼────────────────────┤     │
  │ Ekspert HR i zmiany│ Ekspert prawny      │ Copywriter i trener│     │
  │ ADKAR, szkolenia   │ RODO, AI Act, umowy │ slajdy, skrypt 3:00│     │
  └────────────────────┴──────────┬──────────┴────────────────────┘     │
         ┌───────┐     ┌──────────▼───────────────────────────────┐     │
         │ EXCEL │────►│ WERYFIKATOR: Data-checker + Juror        │─────┘
         │jedyne │     │ przelicza liczby, ocenia wg 10 kryteriów │
         │źródło │     └──────────────────────────────────────────┘
         └───────┘
```

Pętla wraca do orkiestratora, zanim cokolwiek trafi do zespołu: **żaden wynik eksperta nie omija weryfikacji.**

## Czym jest Hermes Agent

Otwartoźródłowy (MIT) agent od Nous Research (luty 2026), działa na laptopie lub serwerze, z trwałą pamięcią i skillami w Markdown. Kluczowe narzędzie: **`delegate_task`** — uruchamia subagentów z izolowanym kontekstem (domyślnie do 10 równolegle, u nas **max 5**); subagent zna wyłącznie pola `goal` i `context` i nie może dopytać użytkownika. Subagentom można przypisać tańszy, szybszy model. Hermes odpowiada też przez Telegram, Discord, Slack i WhatsApp.

**Architektura: eksperci = skill × model, nie osobne „osobowości”.** Każdy ekspert to skill (Markdown w `~/.hermes/skills/`) wywoływany przez `delegate_task`. Osobny profil (pełna instancja z własną pamięcią) ma sens tylko na granicy zaufania — np. gdy jeden agent ma dostęp do surowych danych, a reszta nie.

## Zawartość folderu

| Plik | Co |
|---|---|
| [`skills/`](skills/) | 8 skilli: `helvia-juror` (bazowy) + 7 ekspertów |
| [`szablon-delegate-task.md`](szablon-delegate-task.md) | Szablon `goal` / `context` dla subagenta + gotowe zadania na każdy etap |
| [`plan-delegacji.md`](plan-delegacji.md) | Fale subagentów na etapy, okna czasowe, weryfikacja |
| [`setup.md`](setup.md) | Przygotowanie dzień wcześniej (60–90 min) + instalacja skilli |
| [`config.example.yaml`](config.example.yaml) | Szkic konfiguracji — **klucze do potwierdzenia w dokumentacji** |

## Eksperci

| Ekspert (skill) | Wnosi | Etapy | Wejście | Wyjście |
|---|---|---|---|---|
| `helvia-analityk-finansowy` | EBIT, wpływ rabatów, payback, wrażliwość | E1, E2, E3 | Przychody, marże, koszty etatów | Tabela: wzór + wynik |
| `helvia-analityk-operacji` | FTE, obciążenie, SLA, scoring procesów | E1, E3 | Dane działów, karty procesów | Heatmapa RAG, macierz potencjał × ryzyko |
| `helvia-strateg` | TOWS, macierz kierunków, teza | E2, E5 | Wnioski E1, pipeline | 2–3 kierunki + „wybieramy X kosztem Y” |
| `helvia-ekspert-hr` | ADKAR, szkolenia, ankiety, rotacja | E1, E4 | Ankiety, rotacja | Plan zmiany, plan komunikacji |
| `helvia-ekspert-prawny` | RODO, AI Act, umowy powierzenia, dialog z przedstawicielami pracowników (**tylko sygnalizacja**) | E3, E4 | Mapa HITL | Lista ryzyk + mitygacja |
| `helvia-copywriter` | ≤ 30 słów na slajd, skrypt 3:00 | E5 | Rejestr decyzji | Slajdy, skrypt, mierzenie czasu |
| `helvia-weryfikator` | Data-checker + Juror: przelicza liczby, ocenia wg 10 kryteriów, wskazuje najsłabszy punkt | każdy | Outputy ekspertów + Excel | Lista błędów, flagi `[ZAŁOŻENIE]`, ocena 1–5 |

## Zasady HITL dla agentów (powiedzcie o nich jury)

1. Agent proponuje opcje, zespół decyduje; decyzja trafia do Rejestru decyzji.
2. Żadna liczba nie trafia na slajd bez przeliczenia w Excelu przez Analityka danych.
3. Do modeli idą zagregowane dane, nigdy odpowiedzi osobowe z ankiet.
4. Gdy agenci się nie zgadzają, Decydent rozstrzyga w 1 minutę.
5. **Plan B:** gdy Hermes nie działa (Wi-Fi, limity API), ten sam podział ról prowadzicie w zwykłym czacie Claude z tym repo / playbookiem (skille z `skills/` wklejacie jako prompty).
