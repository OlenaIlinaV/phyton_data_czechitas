'''# 1 part
zvire_list = ["Lenochod", "Bronislavomír", "Ovoce a zelenina", "Kluk"]
navstevnik_list =  ["Jana", 19, False]

# slovnik !!!
zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
}
navstevnik = {
    'jmeno'   : 'Jana',
    'vek'     : 19,
    'karticka': True,
    'deti'    : ['Pepik', 'Anicka'],
}
cisla = {
    1: 'jedna',
    2: 'dva',
    3: 'tri',
}

if navstevnik['karticka']:
    sleva = 'ma slevu'
else:
    sleva = 'nema slevu'

print(f'Prislel navstevnik {navstevnik["jmeno"]}, a {sleva}.')

# 2 part

zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
}

# vypis hodnoty
jmeno = zvire['jmeno']
print(jmeno)

# pridavam (proste zalozim novy klic)
zvire['barva'] = 'hnedo-sediva'
print(zvire)

# takhle prepisuji (prirazuji ke klici, ktery uz ve slovniku je)
zvire['pohlavi'] = 'holka'
print(zvire)

# mazani (dva druhy)
# pop
barva = zvire.pop('barva')  # pop nam hodnotu jeste vrati
print(barva)  # tady jsme ji mohli jeste vypsat
print(zvire)  # lenochod barvu uz nema

# del
del zvire['pohlavi']  # vypari se primo ze slovniku
print(zvire)  # lenochod uz neni kluk

# 3 part

zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
    # 'pohlavi': 'holka' # виведе останнє задане значення, ключем може бути лише те, що буде не змінним (унікальним)
    # 'karticka pojistence': 'VZP',
}

print(zvire)

print('a' in 'ahoj')
print(1 in [1, 2, 3])
print('kluk' in zvire) # шукає в ключі, а не в перечні данних

# Tohle nepujde, protoze tento klic ve slovniku neni.
# print(zvire['karticka pojistence'])

# get - ochrana proti KeyError
karticka = zvire.get('karticka pojistence', 'nenalezena')
print(karticka)

if 'potrava' in zvire:
    print(f'Zvire je najedene. Snedlo {zvire["potrava"]}')
else:
    print('Toto zvire nemusi jist. Poznamka: poridit jich vic')

# 4 part

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
    # 'karticka pojistence': 'VZP',
}

# to samé jako: slovnik.get(co, 'Neni to tam')

def vyndej_ze_slovniku(slovnik, co):
    if co in slovnik:
        return slovnik[co]
    else:
        return 'Neni to tam.'

cislo_listku = int(input('Zadej cislo listku: '))
vyhra = vyndej_ze_slovniku(tombola, cislo_listku)
print(vyhra)

vlastnost = input('Zadej vlastnost zvirete: ')
vysledek = vyndej_ze_slovniku(zvire, vlastnost)
print(f'Zvire {vlastnost} je {vysledek}.')

# 5 part - cykly

sales = {
    "Zkus mě chytit"     : 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh"      : 2565,
}

# funguje, ale neni idealni
for key in sales:
    print(f'Knihy {key} se prodalo {sales[key]}')

# tohle je mnohem lepsi, rychlejsi, pouziva se nejcasteji
for name, amount in sales.items():
    print(f'Knihy {name} se prodalo {amount}')

# prochazi jen hodnoty
for amount in sales.values():
    print(amount)

# prochazi jen klice
for key in sales:
    print(key)


# shrnuti
# slovnik          -> jen klice
# slovnik.keys()   -> jen klice (ale rikam to naprimo)
# slovnik.values() -> jen hodnoty
# slovnik.items()  -> klic i hodnota - super, pozivat


# chceme celkovy prodej
total_sales = 0
for name, amount in sales.items():
    total_sales += amount
print(total_sales)

# nebo :-)

print(sum(sales.values()))

# 6 part - Dvourozměrné tabulky

book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018} # словник для однієї книги

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

# celkem kusu
total_sales = 0
for book in books:
    total_sales += book['sold']

print(total_sales)

# prvni pismena nazvu
for book in books:
    title = book['title']
    first_letter = title[0]
    print(first_letter)

# celkem vydelek v roce 2019
cash = 0
for book in books:
    if book['year'] == 2019:
        amount = book['price'] * book['sold']
        cash += amount
print(cash)

# 7 part - Čtení ze souborů (mereni.txt)

with open('data/mereni_tyden1.txt', encoding='utf-8') as file: # 'utf-8' - Unicode Transformation Format, это система кодирования
    text = file.read()

print(text)

output = []

with open('data/mereni_tyden1.txt', encoding='utf-8') as file:
    for line in file:
        day, temp = line.split('\t')
        output.append([day, float(temp)])

print(output)'''

# 8 part - Zápis do souboru

text = "Tento text bude zapsán do souboru."

with open('data/soubor.txt', mode='w', encoding='utf-8') as output_file:
    print(text, file=output_file)


names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('data/uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)

names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('data/uzivatele.txt', mode='a', encoding='utf-8') as output_file: # хочемо додати новий вміст у кінець файлу
    for name in names:
        print(name, file=output_file)

# 8 part - Množiny

konicky = ["Python", "kung-fu", "Python", "Python", "SQL", "Netflix", 'Tenis', 'Zvire']
konicky = set(konicky)
konicky.add("python")
print(konicky)

konicky_1 = {"Python", "kung-fu", "Python", "Python", "SQL", "Netflix"}
konicky_2 = {"Python", 'Tenis', 'Zvire'}
vsechny_kinicky = konicky_1 | konicky_2
spolecne_konicky = konicky_1 & konicky_2
print(vsechny_kinicky)
print(spolecne_konicky)

