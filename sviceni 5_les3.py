
# Soubory: čtení a zápis

# PART 1 - Čtení ze souborů

# 1 Výplata přesněji (Платіть точніше)

# Поки що ми розраховували свою зарплату, припускаючи, що ми працюємо однакову кількість годин щомісяця, що не дуже реалістично. 
# Завантажте текстовий файл report.txt , який містить 12 рядків і в кожному рядку кількість відпрацьованих годин за кожен місяць за останній рік.

# Відкрийте цей файл у своїй програмі та завантажте значення в рядках у список vykaz. Роздрукуйте цей список у функціональному терміналі, print()щоб переконатися, що ви правильно завантажили файл.
# Попросіть користувача ввести погодинну оплату в командному рядку. Розрахувати та вивести загальну заробітну плату за весь рік та середню заробітну плату за один місяць.

'''with open('data/vykaz.txt', encoding='utf-8') as file: # 'utf-8' - Unicode Transformation Format
    text = file.read()

print(text)

hours = []

with open('data/vykaz.txt', encoding='utf-8') as file:
      #file.read() - можно не писати, бо достатньо прочитати один раз
      for line in file:
        hour = int(line)
        hours.append(hour)
print(hours)

hourly_rate = int(input('Write your rate: '))
total_salary = hourly_rate * sum(hours)
print(total_salary)
print(total_salary/len(hours))'''


# 2 Počet slov
# Завантажте подану стильову роботу . Завданням було написати текст не менше 150 слів про нашу столицю. Напишіть програму, яка підраховує кількість слів у цьому тексті, щоб ми знали, чи було формально виконано завдання. Дозвольте собі керуватися наступними інструкціями.

# Попросіть вашу програму відкрити файл і прочитати кожен рядок у списку
# Перетворіть кожен рядок на список слів. Слово означає все, що розділене пробілом або новим рядком
# Виведіть кількість слів у кожному рядку
# Виведіть загальну кількість усіх слів у файлі

rows_words = []
with open('data/praha.txt', encoding='utf-8') as file:
      for line in file:
           words = line.split()
           print(words)
           words_count = len(words)
           print(words_count)
           rows_words.append(words_count)
print(sum(rows_words))

# 3 Půjčovna

# Компанія з прокату автомобілів має один автомобіль із заданим номером у кожному регіоні Чехії. В кінці року він хоче дізнатися, скільки кілометрів проїхали всі машини разом. 
# У файлі auta.txt для кожного номерного знака записується кількість кілометрів, пройдених автомобілем за певний рік. Значення в тисячах кілометрів. 
# На жаль, вони тупо скоординували в окремих регіонах і хтось користувався комою, хтось крапкою.
# Увага! У файлі даних є ще одна проблема, яка не помітна на перший погляд!
# Напишіть програму, яка виводить суму всіх пройдених кілометрів. Ви обов’язково знайдете рядковий метод під назвою replace().

total_distance = 0

with open('data/auta.txt', encoding='utf-8') as file:
      for line in file:
            if len(line.strip()) > 0: # видалити нульові символи з початку та кінця (strip) строчки та працюємо не ез нульовими строчками (>0)
                 spz, km = line.split()
                 #_, km = line.split() - якщо ми не будемо використовувати змінну, то краще не придумивати назву а просто написати '_'
                 km = km.replace(',', '.')
                 km = float(km)
                 total_distance += km
print(total_distance)


# PART 2 - Zápis do souboru

# 1 Dny v měsíci

# Напишіть програму, яка матиме кількість днів у кожному місяці, записану безпосередньо в коді таким чином:
# Нехай ваша програма запише цей список у файл з назвою kalendar.txt, кожне число в одному рядку.

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('data/kalendar.txt', mode='w', encoding='utf-8') as output_file:
      for day in pocty_dni:
           print(day, file=output_file)

# 2 Vytvoření souboru (Створення файлу)
           
# Напишіть програму, яка під час запуску запитує назву файлу для створення (або перезапису, якщо файл уже існує), а потім запитує рядок тексту для запису у файл.

'''with open(file = str(input('Write file name: ')), mode='w', encoding='utf-8') as output_file:
    text = input('Write text:')
    print(text, file = output_file)

name = input('Write file name: ')
with open(f'data/{name}', mode='w', encoding='utf-8') as output_file:
      text = input('Write text:')
      print(text, file=file)'''

# 3 Rozepsaná výplata (Оплата за графіком)

# Змініть програму розрахунку зарплати з попереднього розділу, щоб вона не друкувала середню зарплату за рік, а друкувала конкретну суму, виплачену за кожен місяць окремо.

# Спочатку введіть цю інформацію в термінал
# Потім змініть програму, щоб записати ці результати у файл

monthly_salary_list = []
hourly_rate = int(input('Write your rate: '))

with open('data/vykaz.txt', encoding='utf-8') as file:
      for line in file:
        hour = int(line)
        monthly_salary = hour * hourly_rate
        monthly_salary_list.append(monthly_salary)
with open('data/vykaz_output.txt', 'w', encoding='utf-8') as output_file:
     for item in monthly_salary_list:
          print(item, file=output_file)
