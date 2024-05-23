'''print("hello world")
pocet_jablek = 10 # int
teplota = 37.8 # float
jmeno = 'Kuba' # string

pravda = True # boolean
lez = False # boolean

zbozi = [
    "hrnek", 
    "sklenička",
    ] # list '''

'''PRICE_PER_TICKET = 250 #великимі означаємо константу
DISCOUNT_AMT = 0.1
DISCOUNT_THRESH = 500

number_of_tickets = int(input('Zadej počet listkú: '))
total_price = number_of_tickets * PRICE_PER_TICKET

if total_price >= 500:
    total_price = total_price * (1 - DISCOUNT_AMT)
else:
    to_discount = DISCOUNT_THRESH - total_price

print(f"You have {number_of_tickets}, so you will have total price {total_price} $.") '''
    
# 2

'''age = int(input("Jaký je Váš věk? "))

if age < 13:
    print("Představení je bohužel přístupné až od 13 let.")
    exit()

number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 1500:
    discount = 0.2
    total_price = total_price * (1 - discount)
    ¬print(f"Získáváte slevu {discount * 100}.")
elif total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
else:
    to_discount = total_price - 500
    print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")'''


# 3

# flight_number = input("Zadejte číslo letuc [napr: BA345]: ")

'''flight_number = "LN345"
prefix = flight_number [0] + flight_number[1]

prefix = flight_number [0:2]
prefix = flight_number [:2]
# prefix = flight_number [-2:]
# prefix = flight_number [:-2]
if prefix == "BA":
    company = "British Airways"
elif prefix == "LH":
    company = "Lufthansa"
else:
    company = "Neznámá společnost"
print(f"Letíte se společností {company}") '''


#4

"""guest_list = ["Jirka", "Klára", "Natálie"]

name = input("Zadej Jmeno: ")

if name[0] == "K":
    #добавляем
    guest_list.append(name)

print(guest_list)

guest = input("Write name guest: ")
if guest in guest_list:
    print("Hi!")
else:
    print('By!')"""

#5
'''grades = ['Alena', 1, 2, 3, 4, 5, True]

school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]
print(school_marks[1][0][-1])'''


#6
'''school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]
names_only = []
for row in school_marks:
    name = row[0]
    names_only.append(name)
    print(names_only)'''

#6
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3, 5, 6, 7],
    ["Tereza", 1, 1, 2, 1],
]
#хто має 3
names_only = []
top_performers =[]
mid_performers = []

for row in school_marks:
    name = row[0]
    grades = row[1:] #все одно скільки буде оцінок
    if 3 not in grades:
        names_only.append(name)

    if 1 in grades:
        top_performers.append(name)

print(top_performers)