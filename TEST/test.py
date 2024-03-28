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

print('Hello, Olena!')