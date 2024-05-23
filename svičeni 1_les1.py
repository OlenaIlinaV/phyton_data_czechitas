# 1
'''cislo = 100
cislo = cislo - 1
print(cislo)'''


#3
'''far = float(input("Write far degree:")) #потому что с точкой
c = (far - 32) * 5/9
print(f"This {far} mean that you have {c} C")'''



#1 Součet čísel v seznamu

list = [5, 1, 2, 10, 3]

for number in list:
    print()

#2 Největší prvek v seznamu

'''list = [5, 1, 2, 10, 3]

for number2 in list:
     if number2[0] > number2[1]: 
          print(number2)'''

#3 Sudá čísla

'''list = [5, 1, 2, 10, 3]
print()

for number3 in list:
    #if number3 / 2 == int(number):
        print(number3)'''


user_info = {"ім'я": "Олена", "вік": 30}
for key, value in user_info.items():
    print(f"{key}: {value}")