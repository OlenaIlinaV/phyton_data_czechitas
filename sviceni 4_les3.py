# 1 Vysvědčení 2

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# 1.1 Напишіть програму, яка обчислює середній бал з усіх предметів.

aver_mark = 0
sum_mark = 0
amount_course = 0
for course, mark in school_report.items():
    sum_mark += mark 
    amount_course = len(school_report)
    aver_mark = sum_mark / amount_course

print(aver_mark) # результат вірний, але рішення довге

print(sum(school_report.values())/len(school_report)) # записала одною строкою, результат той самий

# 1.2 Змініть програму, щоб перелічити всі предмети, з яких учень отримав 1 оцінку.

courses_list = {}
courses_array = []
amount_1 = 0
for course, mark in school_report.items():
    if mark == 1:
        courses_list[course] = mark # результат у списку {'Český jazyk': 1, 'Anglický jazyk': 1, 'Matematika': 1, 'Dějepis': 1}
        courses_array.append(course) # результат у масиву ['Český jazyk', 'Anglický jazyk', 'Matematika', 'Dějepis']
        amount_1 += mark # знайшла по скільком предметам учень отримав 1
print(courses_list)
print(courses_array)
print(amount_1)


# 2 Čtenářský deník

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

# 2.1 Напишіть програму, яка підраховує загальну кількість сторінок, прочитаних Густавом.

total_amount = 0
for book in books:
    total_amount += book['pages']
print(total_amount)

# 2.2 Додайте в програму підрахунок кількості книг, які Густав оцінив не менше 8.

rate_8 = 0
for book in books:
    if book['rating']>=8:
        # amount = 1
        # rate_8 += amount
        
        rate_8 += 1

print(rate_8)

# 3 Poznávací značky (Номерні знаки)

#У наступних словниках є запис автомобілів. Ключ - це номерний знак, а значення - ім'я власника автомобіля. 
# Напишіть програму, яка містить список усіх власників, транспортні засоби яких зареєстровані в регіоні Пльзень, тобто літера P стоїть на другому місці (індекс 1!) ланцюжка в ключі.

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

owner_from_pilzen_list = {} #list
owner_from_pilzen_array = [] #array
for number, name in plates.items():
    if number[1] == 'P':
        owner_from_pilzen_list[name] = number
        owner_from_pilzen_array.append(name)
print(owner_from_pilzen_list)
print(owner_from_pilzen_array)

# 4 Recepty (реецепти)

# Збережіть цю структуру в змінній рецепта на початку нової програми. Скористайтеся цією функцією, щоб написати, print скільки коштуватиме вся їжа в кронах, округлених до цілих крон.

recipe = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

total_sum = 0
for key, value in recipe.items():
    if key == 'ingredience':
        total_sum += value[2]
print(total_sum)