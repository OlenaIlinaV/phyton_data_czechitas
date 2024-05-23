
# 1 TASK Útočící rody

SL_UTOCNIK_1 = 5
SL_UTOCNIK_2 = 6
SL_UTOCNIK_3 = 7
SL_UTOCNIK_4 = 8

# Імпортуємо необхідний модуль
import os

# Встановлюємо шлях до файлу battles.tsv у папці DATA
file_path = os.path.join('DATA', 'battles.tsv')

radky = []
with open(file_path, encoding="utf-8") as soubor:
    for radek in soubor:
        radky.append(radek.split("\t"))
utocnici = {}
# for radek in radky:
     # Započítáme útočícímu rodu ze sloupečku SL_UTOCNIK_1 jeden útok navíc
     # po prvnim radku
     # utocnici = {"lannister": 1}
     # po druhem radku
     # utocnici = {"lannister": 2}
     # po tretim radku
     # utocnici = {"lannister": 3}
     # po ctvertem radku
     # utocnici = {"lannister": 3, "Stark 1"}

# Vytvořím si záložku
iterator = iter(radky)
# Posunu záložku dopředu
next(iterator)

# for radek in iterator:
#     # Zjistím si útočící rod
#     utocnik = radek[SL_UTOCNIK_1]
#     utocnici[utocnik] = utocnici.get(utocnik, 0) + 1
# print(utocnici)

for radek in iterator:
    # Za in chci vybrat 4 sloupečky, které obsahují 4 útočící rody
    # Chci vybrat hodnoty od sloupečku SL_UTOCNIK_1 do sloupečku SL_UTOCNIK_4 
    for utocnik in radek [SL_UTOCNIK_1:SL_UTOCNIK_4+1]:
        if utocnik != "":
            if utocnik in utocnici:
                utocnici[utocnik] = utocnici.get(utocnik, 0) + 1
            else:
                utocnici[utocnik] = 1
print(utocnici)
