# Checklista przed warsztatami

## Dzień wcześniej
- [ ] Role przydzielone ([`role-zespolu.md`](role-zespolu.md) — wpisane imiona)
- [ ] Projekt Claude „HELVIA” założony i przetestowany ([`asystent-ai/setup.md`](../asystent-ai/setup.md)) — 20–30 min
- [ ] Próba generalna E1–E2 na danych syntetycznych (`python3 narzedzia/generuj_dane_syntetyczne.py`)
- [ ] Skrypt 3:00 przeczytany na głos z zegarem (szkielet w [`05_etap5_prezentacja/skrypt-3min.md`](../05_etap5_prezentacja/skrypt-3min.md))
- [ ] Sprawdzony język Excela na obu laptopach: **PL czy EN** (formuły: [`wiedza/formuly-excel.md`](../wiedza/formuly-excel.md))

## Co zabrać
- [ ] 2 laptopy z Excelem
- [ ] Ładowarki, przedłużacz, hotspot w telefonie (Wi-Fi na wydarzeniach bywa przeciążone)
- [ ] Plik [`excel/HELVIA_szablony.xlsx`](../excel/HELVIA_szablony.xlsx) z pustymi tabelami
- [ ] Konto Canva lub szablon PPT, gotowa paleta 2 kolorów + 1 akcent
- [ ] Dostęp do projektu Claude „HELVIA” na każdym laptopie (prompty ekspertów w wiedzy projektu)
- [ ] Wydrukowana strona [„Zasady gry”](zasady-gry.md) i [bank pytań jury](../05_etap5_prezentacja/bank-pytan-jury.md)
- [ ] Timer widoczny dla wszystkich (telefon na statywie lub online)
- [ ] Dyktafon w telefonie (nagranie próby, sprawdzenie 3:00)

## Na starcie warsztatów (pierwsze 10 min)
- [ ] Zapytać mentora: czy wolno wysyłać dane do zewnętrznych modeli AI? (RODO — też dobry argument na pytania jury)
- [ ] Pliki organizatora → `dane/organizator/` (nie commitujemy)
- [ ] Sanity-check: `python3 narzedzia/sanity_check.py dane/organizator/<plik>.xlsx`
- [ ] Wspólny folder (OneDrive / Google Drive), jedna wersja pliku: `HELVIA_E1_v1.xlsx`
- [ ] Grupa zespołu na komunikatorze (szybkie przekazywanie wyników z czatów)

## Stos narzędzi

| Warstwa | Narzędzie | Do czego | Wskazówka |
|---|---|---|---|
| Dane | Excel: tabele (Ctrl+T), pivoty | Agregacja po działach i klientach w 2 min | Najpierw formatowanie jako tabela, potem pivot |
| Dane | Power Query | Łączenie plików, czyszczenie nagłówków | Gdy plików > 3 |
| Dane | Formatowanie warunkowe | Heatmapa RAG | Progi z Etapu 1 |
| Dane | Python / pandas (opcjonalnie) | Korelacje, sanity-check sum | Wynik zawsze przepisany do Excela |
| AI | Claude (projekt z playbookiem) | Szkice zdań, krytyka hipotez, formuły | Wgrać prompt i playbook jako wiedzę projektu |
| AI | Równoległe czaty w projekcie Claude | Zespół ekspertów: każdy w zespole prowadzi 1 czat z promptem roli | [`asystent-ai/`](../asystent-ai/) |
| Wizualizacja | Wykresy Excela | Pareto, wodospad EBIT, słupki | Kopiować jako obraz do slajdu |
| Diagramy | Excalidraw / draw.io / Mermaid | Mapa HITL, swimlane, harmonogram | Mermaid generuje Claude z tekstu |
| Slajdy | Canva / PowerPoint | 3 slajdy | Max ~30 słów na slajd |
| Czas | Timer | Limity 55/45/70/70 min | Alarm 5 min przed końcem |
| Prezentacja | Dyktafon | Próba, sprawdzenie 3:00 | 2 próby na głos minimum |
