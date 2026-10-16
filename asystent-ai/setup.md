# Setup Claude — dzień wcześniej (20–30 min)

- [ ] Projekt w Claude (claude.ai → Projects) o nazwie **HELVIA**, udostępniony całemu zespołowi (lub każdy zakłada własny z tą samą zawartością)
- [ ] **Instrukcje projektu:** treść [`CLAUDE.md`](../CLAUDE.md) + [`prompty/00-kontekst-case.md`](prompty/00-kontekst-case.md)
- [ ] **Wiedza projektu:** `docs/Playbook_HELVIA_jak_wygrac_case.pdf`, cały folder [`wiedza/`](../wiedza/), folder [`prompty/`](prompty/), [`01_etap1_diagnoza/analiza-E1.md`](../01_etap1_diagnoza/analiza-E1.md), [`05_etap5_prezentacja/bank-pytan-jury.md`](../05_etap5_prezentacja/bank-pytan-jury.md)
- [ ] **Nie wgrywamy** surowych plików organizatora z danymi osobowymi (arkusze „Ankieta szczegółowo” i „Lista pracowników szczegółowo” zawierają maile) — chyba że mentor wprost pozwoli. Wklejamy agregaty.
- [ ] Każdy członek zespołu sprawdza dostęp z własnego laptopa i telefonu
- [ ] Próba generalna na danych syntetycznych: `python3 narzedzia/generuj_dane_syntetyczne.py` → zespół przechodzi E1–E2 na czas, każdy w swoim czacie

## Test dymny (5 min)

1. Nowy czat: „Podaj liczby bazowe case'u.” → oczekiwane: 114,93 / 9,65 / 1 pp rabatu = 1,15 mln = 12% EBIT.
2. „Działaj wg promptu helvia-analityk-finansowy: policz wpływ rabatu 2 pp na EBIT.” → −2,30 mln zł ≈ −24% EBIT, wzór pokazany.
3. „Działaj wg promptu helvia-weryfikator: oceń zdanie ‘Wybieramy AI wszędzie’.” → brak „kosztem”, brak liczby, ocena ≤ 2.

## Dlaczego bez Hermesa to OK

Hermes dawał równoległość i pamięć sesji. W Claude: **równoległość = 3–4 osoby, każda z własnym czatem**, **pamięć = Rejestr decyzji + wiedza projektu** (po każdym etapie wklejacie decyzję do czatu weryfikatora i aktualizujecie `rejestr-decyzji.md`). Mniej konfiguracji, zero ryzyka awarii VPS/API na sali.
