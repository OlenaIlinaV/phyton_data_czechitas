
#1 Pohyby na účtu
pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])
print(pohyby[2:])
print(sum(pohyby))
print(max(pohyby))
print(min(pohyby))

#2 Průměr
s = [1, 3, 4, 7, 10, 20]

summa = sum(s)
delka = len(s)
print(summa/delka)

# 3 Rozpětí

s = [1, 3, 4, 7, 10, 20]

minimum = min(s)
print(minimum)
maximum = max(s)
print(maximum)
rozpet = minimum - maximum
print(rozpet)


#4 Násobení - Напишіть функцію mult, яка буде мати два числові параметри. Функція множить обидва параметри та повертає результат.

def mult(a,b):
    result = a * b
    return result

first = 10
second = 5
print(mult(first, second))

#5 kilometry_na_mile(kilometry)

def kilometry_na_mile(kilometry):
    
    mile = kilometry * 1,609344
    return(mile)

print(kilometry_na_mile)

#6 mily_na_kilometry(mile)

def mily_na_kilometry(mile):

    kilometry = mile * 0.62137119609836
    return(kilometry)

print(mily_na_kilometry)