# Závod

import json

# Відкриваємо файл та завантажуємо дані
with open('zavod.json', 'r', encoding='utf-8') as file:
    race_data = json.load(file)

# Створюємо порожній список для учасників, які закінчили гонку
finishers = []

# Переглядаємо кожного учасника
for participant in race_data:
    # Перевіряємо, чи учасник закінчив гонку
    if participant['casy']['oficialni'] != "DNF": # вказуємо обоє, бо списко в списку в списку
    # Якщо так, додаємо його до списку finishers
        finishers.append([participant['jmeno'], participant['casy']['oficialni']])


# Виводимо вміст списку finishers
print("Учасники, які закінчили гонку:")
for finisher in finishers:
    print(finisher)

# Вибираємо учасника з другим найкращим часом (срібний медаліст)
if len(finishers) >= 2:
    # Сортуємо список за офіційними часами
    finishers.sort(key=lambda x: x[1])
    # Виводимо ім'я та час срібного медаліста
    print("\n Срібний медаліст:")
    print(f"Ім'я: {finishers[1][0]}")
    print(f"Час: {finishers[1][1]}")
else:
    print("\n Недостатньо учасників, щоб визначити срібного медаліста.")


# words
    
import json

words = []

with open('words.txt', 'r', encoding='utf8') as file_in:
    for line in file_in:
        word = line.strip()
        words.append(word)

dictionary = {}

# tady jsme si pre-sortovali slova, budou tak serazena i v listech
words.sort()

for word in words:  
    first_letter = word[0]
    if first_letter in dictionary:
        dictionary[first_letter].append(word)
    else:
        dictionary[first_letter] = [word]

with open('vysledny_dict.json', 'w', encoding='utf-8') as file_out:
    json.dump(dictionary, file_out, indent=4, ensure_ascii=False, sort_keys=True)