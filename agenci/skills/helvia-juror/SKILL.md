---
name: helvia-juror
description: Skill bazowy case'u HELVIA: kontekst case'u, liczby bazowe i kryteria jury. Orkiestrator ładuje go na starcie i wkleja sekcje do context każdego subagenta.
---
# helvia-juror — skill bazowy orkiestratora

> ⚠️ Uzupełnijcie ten plik pełną treścią `prompt_helvia_case.md` od organizatora (sekcje poniżej to minimum z playbooka).

## case_context
HELVIA Polska — firma BPO: 720 pracowników, 14 klientów, 8 działów, przychód LTM 114,93 mln zł, marża operacyjna 8,4% (EBIT ≈ 9,65 mln zł). 1 pp rabatu na całej bazie ≈ 1,15 mln zł ≈ 12% EBIT.
Etapy: E1 Diagnoza (40 min) → E2 Strategia (45) → E3 Człowiek + AI (70) → E4 Roczna zmiana (70) → E5 3 slajdy + 3:00.
Teza docelowa: „Wybieramy X kosztem Y, ponieważ [liczba z Excela] — i to działa dla zarządu, pracowników i klientów.”

## metrics
| Wskaźnik | Wartość | Wzór |
|---|---|---|
| Przychód LTM | 114,93 mln zł | z opisu |
| EBIT | ≈ 9,65 mln zł | 114,93 × 8,4% |
| Przychód / pracownik | ≈ 159,6 tys. zł | 114,93 mln / 720 |
| EBIT / pracownik | ≈ 13,4 tys. zł | 9,65 mln / 720 |
| Średni przychód / klient | ≈ 8,2 mln zł (≈ 7%) | 114,93 / 14 |
| 1 pp rabatu | ≈ 1,15 mln zł ≈ 12% EBIT | 114,93 × 1% |

## evaluation_criteria (10 przykazań = kryteria oceny)
1. Jedna teza, jedno zdanie — powtarzana na każdym slajdzie.
2. Liczba przy każdym twierdzeniu, źródło przy każdej liczbie; spoza Excela = [ZAŁOŻENIE].
3. Każde „wybieramy” ma swoje „kosztem”.
4. Każda decyzja ma argument dla zarządu, pracowników i klientów (Trójkąt Dobrostanu).
5. Uwolnione FTE idą na pipeline i SLA, nie na zwolnienia.
6. HITL konkretny: kto zatwierdza, w którym kroku, przy jakim progu.
7. KPI = baza + cel 12 mies. + źródło + właściciel.
8. Ryzyka nazwane po imieniu: SLA, RODO, AI Act, rotacja, opór.
9. Łańcuch E1 → E2 → E3 → E4 → E5 bez przeskoków.
10. 3:00 to 3:00.

## Rola orkiestratora
- Na etap: jedna fala 3 subagentów przez `delegate_task` (max 5 równolegle), potem `helvia-weryfikator`.
- Każdemu subagentowi przekazujesz: ROLA, DANE (nagłówki + agregaty), ZASADY, KRYTERIA JURY, FORMAT.
- Wynik do zespołu: opcje + rekomendacja + flagi [ZAŁOŻENIE]. Nie podejmujesz decyzji; proponujesz wpis do Rejestru decyzji (Etap · Decyzja · Kosztem czego · Kluczowa liczba · Źródło).
