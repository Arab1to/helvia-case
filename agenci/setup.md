# Setup Hermesa — dzień wcześniej (60–90 min)

- [ ] Instalacja według **oficjalnej dokumentacji** (Linux, macOS lub WSL2), test modelu i klucza API
- [ ] Skill `helvia-juror` + 7 skilli ekspertów (rola, wejście, format wyjścia, zakaz wymyślania liczb) — z folderu [`skills/`](skills/)
- [ ] Tańszy model dla subagentów i limit równoległości (5) w `~/.hermes/config.yaml` — dokładne klucze w dokumentacji delegacji (szkic: [`config.example.yaml`](config.example.yaml))
- [ ] Podłączenie bramki do komunikatora zespołu (Telegram / Discord / Slack / WhatsApp)
- [ ] Próba generalna na danych syntetycznych: `python3 narzedzia/generuj_dane_syntetyczne.py` → fikcyjna HELVIA (8 działów, 14 klientów), zespół przechodzi E1–E2 na czas
- [ ] Uruchomienie w izolowanym środowisku (np. Docker), bez dostępu do prywatnych plików; **żadnych skilli z niezweryfikowanych źródeł**

Pełna instrukcja od zakupu VPS przez Telegram i Claude Max po konfigurację agentów: dokument „Setup Hermesa” (link w playbooku).

## Instalacja skilli z repo

```bash
# z katalogu repo
mkdir -p ~/.hermes/skills/helvia
cp -r agenci/skills/* ~/.hermes/skills/helvia/
ls ~/.hermes/skills/helvia
```

Każdy skill to folder z plikiem `SKILL.md` (frontmatter `name` + `description`, potem instrukcje). Jeśli wasza wersja Hermesa oczekuje innej struktury katalogów — sprawdźcie w dokumentacji „Skills” i przenieście pliki; treść pozostaje ta sama.

## Test dymny (5 min)

1. Do orkiestratora: „Załaduj skill helvia-juror i podaj liczby bazowe case'u.” → oczekiwane: 114,93 / 9,65 / 1,15 mln = 12% EBIT.
2. „Deleguj do helvia-analityk-finansowy: policz wpływ rabatu 2 pp na EBIT.” → oczekiwane: −2,30 mln zł ≈ −24% EBIT, wzór pokazany.
3. „Deleguj do helvia-weryfikator: oceń zdanie ‘Wybieramy AI wszędzie’.” → oczekiwane: brak „kosztem”, brak liczby, ocena ≤ 2.

## Źródła
- Hermes Agent — dokumentacja: Subagent Delegation
- Hermes Agent — About (hermes-agent.org)
- The Next Web: Nous Research raises $90M to take its Hermes AI agent to businesses
- RuntimeWire: Hermes Agent v0.20.0 — voice and agent-to-agent links
