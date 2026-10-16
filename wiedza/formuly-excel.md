# Formuły Excela (PL / EN)

W **polskim** Excelu argumenty oddziela **średnik**, obowiązuje **przecinek** dziesiętny; w **angielskim** — przecinek i kropka. Zakresy poniżej są przykładowe: 8 działów w wierszach 2–9, 14 klientów w wierszach 2–15. Zamieńcie dane w tabele (**Ctrl+T**), żeby używać nazw kolumn.

> Plik `excel/HELVIA_szablony.xlsx` ma formuły zapisane wewnętrznie (EN) — Excel PL automatycznie wyświetli je po polsku.

| Cel | Excel PL | Excel EN |
|---|---|---|
| FTE z godzin miesięcznych | `=B2/160` | `=B2/160` |
| Wartość uwolnionego czasu / mies. | `=(Godz_zaoszcz/160)*Koszt_etatu` | `=(Hours_saved/160)*FTE_cost` |
| Udział klienta w przychodzie | `=B2/SUMA($B$2:$B$15)` | `=B2/SUM($B$2:$B$15)` |
| Udział skumulowany (Pareto) | `=SUMA($C$2:C2)` | `=SUM($C$2:C2)` |
| Ranking klientów | `=POZYCJA.NAJW(B2;$B$2:$B$15)` | `=RANK.EQ(B2,$B$2:$B$15)` |
| Przychód per dział z tabeli klientów | `=SUMA.JEŻELI(Klienci[Dział];A2;Klienci[Przychód])` | `=SUMIF(Clients[Dept],A2,Clients[Revenue])` |
| Średnia SLA per dział | `=ŚREDNIA.JEŻELI(Klienci[Dział];A2;Klienci[SLA])` | `=AVERAGEIF(Clients[Dept],A2,Clients[SLA])` |
| Sygnał RAG dla rotacji | `=JEŻELI(F2>1,5*MEDIANA($F$2:$F$9);"Czerwony";JEŻELI(F2>MEDIANA($F$2:$F$9);"Żółty";"Zielony"))` | `=IF(F2>1.5*MEDIAN($F$2:$F$9),"Red",IF(F2>MEDIAN($F$2:$F$9),"Amber","Green"))` |
| Liczba działów w czerwieni | `=LICZ.JEŻELI(H2:H9;"Czerwony")` | `=COUNTIF(H2:H9,"Red")` |
| Korelacja rotacja × SLA | `=WSP.KORELACJI(F2:F9;E2:E9)` | `=CORREL(F2:F9,E2:E9)` |
| Top-2-box w ankiecie (oceny 4–5) | `=LICZ.JEŻELI(G2:G500;">=4")/ILE.NIEPUSTYCH(G2:G500)` | `=COUNTIF(G2:G500,">=4")/COUNTA(G2:G500)` |
| Wartość oczekiwana pipeline'u (suma) | `=SUMA.ILOCZYNÓW(B2:B10;C2:C10)` | `=SUMPRODUCT(B2:B10,C2:C10)` |
| Luka FTE | `=SUMA(FTE_pipeline)-SUMA(FTE_uwolnione)` | `=SUM(FTE_pipeline)-SUM(FTE_freed)` |
| Wpływ rabatu na EBIT (zł) | `=-Rabat*Przychód` | `=-Discount*Revenue` |
| Wpływ rabatu jako % EBIT | `=-Rabat*Przychód/EBIT` | `=-Discount*Revenue/EBIT` |
| Gain-sharing: zysk HELVII | `=(1-Udział_klienta)*Oszczędność` | `=(1-Client_share)*Savings` |
| Scoring ważony (wagi w wierszu 1) | `=SUMA.ILOCZYNÓW(B2:E2;$B$1:$E$1)/SUMA($B$1:$E$1)` | `=SUMPRODUCT(B2:E2,$B$1:$E$1)/SUM($B$1:$E$1)` |
| Payback prosty (mies.) | `=Koszt_całk/Oszcz_mies` | `=Total_cost/Monthly_savings` |
| Payback netto (mies.) | `=Koszt_jednoraz/(Oszcz_mies-Licencja_mies)` | `=One_off_cost/(Monthly_savings-Monthly_licence)` |
| Wyszukanie danych z innego arkusza | `=X.WYSZUKAJ(A2;Dzialy[Dział];Dzialy[Rotacja])` | `=XLOOKUP(A2,Depts[Dept],Depts[Turnover])` |

**Nazwane komórki** (np. `Koszt_etatu`): zaznaczcie komórkę i wpiszcie nazwę w polu nazwy po lewej od paska formuły. Dzięki temu formuła czyta się na głos przed jury.

> ⚠️ Nazwy z polskimi znakami (`Koszt_całk`, `Oszczędność`) działają w Excelu, ale bywają kłopotliwe przy przenoszeniu między wersjami językowymi — w szablonie używamy nazw bez ogonków (`Koszt_calk`).

## Sanity-check w 30 sekund

- suma FTE działów = **720**
- suma przychodów klientów = **114,93 mln zł**
- EBIT = przychód × **8,4%** ≈ 9,65 mln zł

Jeśli coś się nie domyka — pytajcie mentora, zanim zbudujecie na tym wnioski. Automat: `python3 narzedzia/sanity_check.py <plik.xlsx>`.
