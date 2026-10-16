# Dane

| Folder | Co | Git |
|---|---|---|
| `organizator/` | Pliki od organizatora (Excel, karty procesów, ankiety) | **ignorowany** — dane poufne |
| `syntetyczne/` | Fikcyjna HELVIA do próby generalnej (`python3 narzedzia/generuj_dane_syntetyczne.py --seed N`) | commitowany |

**Zasady bezpieczeństwa danych**
- Pliki od organizatora traktujemy jak poufne. Do zewnętrznych modeli wysyłamy najpierw **nagłówki i zagregowane liczby**, nie surowe arkusze — chyba że organizator wprost na to pozwala (zapytać mentora na starcie; to też dobry argument „RODO” na pytania jury).
- Nigdy nie wysyłamy odpowiedzi osobowych z ankiet.
- `python3 narzedzia/sanity_check.py <plik>` drukuje tylko nagłówki i sumy — wynik można bezpiecznie wkleić agentom.

**Dane syntetyczne** służą tylko do treningu tempa E1–E2. Nigdy na slajd.
