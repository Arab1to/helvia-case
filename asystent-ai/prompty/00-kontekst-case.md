# 00 — kontekst case'u HELVIA (baza dla każdego czatu)

> **Jak użyć:** ten plik + `CLAUDE.md` wklejacie do **instrukcji projektu** Claude „HELVIA” (albo jako wiedzę projektu). Każdy czat w projekcie startuje wtedy z tym kontekstem, a prompty ról (`helvia-*.md`) tylko dokładają specjalizację.
> ⚠️ Gdy dostaniecie pełny `prompt_helvia_case.md` od organizatora — dopiszcie go poniżej.

## case_context
HELVIA Polska — firma BPO: **720 pracowników (FTE), 14 klientów, 8 działów**, przychód 12M **114,93 mln zł**, marża operacyjna **8,4%** (EBIT ≈ 9,65 mln zł; w danych E1: 9,64 mln zł = 8,39%). Okres danych: 01.10.2025–30.09.2026.

- **Działy:** Finanse i Księgowość (158 FTE), HR i Payroll (61), IT i Wsparcie Techniczne (98), Marketing (30), Obsługa Klienta (208), Operacje i Logistyka (90), Sprzedaż i Key Account (51), Zarząd i Administracja (24).
- **Klienci (przychód 12M):** NORDA Logistics 26,4 mln · Brumark Retail Group 15,5 · Velmont Insurance 12,1 · Kastella Pharma 10,1 · Orvis Energy 9,2 · Delfino Foods 7,8 · Hartberg Manufacturing 7,1 · Lumea Telecom 6,7 · Pilawa Banking Services 5,7 · Sørvik Marine 4,5 · Trelia Home 3,7 · Quenta Analytics 3,0 · Ibera Travel 1,7 · Nordkap Ventures 1,4.
- **Etapy (wg organizatora):** E1 Diagnoza „Jak jest?” — **55 min**, oceniany arkusz 1B (6–8 wniosków) → E2 Strategia → E3 Człowiek + AI → E4 Roczna zmiana → E5 3 slajdy + 3:00.
- Teza docelowa: „Wybieramy X kosztem Y, ponieważ [liczba z Excela] — i to działa dla zarządu, pracowników i klientów.”

## metrics
| Wskaźnik | Wartość | Wzór / źródło |
|---|---|---|
| Przychód 12M | 114,93 mln zł | Dashboard!A5 |
| EBIT | ≈ 9,65 mln zł (dane: 9,64) | 114,93 × 8,4% / Σ Klienci!H |
| Przychód / pracownik | ≈ 159,6 tys. zł | 114,93 mln / 720 |
| 1 pp rabatu | ≈ 1,15 mln zł ≈ 12% EBIT | 114,93 × 1% |
| Kary SLA 12M | 6,27 mln zł = 65% EBIT | Dashboard!A8 |
| Koszty osobowe | 6,51 mln zł/mies. = 78,1 mln zł/rok | Lista pracowników, Σ kosztów |
| Pipeline (22 szanse) | EV 27,06 mln zł, 113,2 FTE | arkusz Pipeline (ukryty) |

## Wnioski z E1 (po decyzji zespołu — aktualizujcie)
Patrz `01_etap1_diagnoza/analiza-E1.md` i `rejestr-decyzji.md`.

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

## Zasady pracy z Claude
- Claude proponuje opcje + rekomendację + flagi [ZAŁOŻENIE]; **decyzję podejmuje zespół**, a wpis trafia do Rejestru decyzji.
- Do czatu wklejamy **nagłówki i agregaty** (np. tabele per dział / klient), nigdy maili ani odpowiedzi pojedynczych osób z ankiety i listy pracowników.
- Format odpowiedzi: tabela markdown + max 3 zdania wniosku + 1 najsłabszy punkt.
