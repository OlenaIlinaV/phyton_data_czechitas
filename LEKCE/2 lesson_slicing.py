'''venecky = [1, 2, 4, 1, 6, 0, 1]
jmeno = 'Olena Ilina'

print(venecky[1:4])
print(jmeno[2:])

print(len(venecky))
print(len(jmeno))

print(sum(venecky))
print(min(venecky))
print(max(venecky))'''

'''serazene_venecky = sorted(venecky, reverse=True)
print(serazene_venecky)

serazene_jmeno = sorted(jmeno)
print(serazene_jmeno)

# tri nejvetsi cisla seznamu
tri_nejvetsi = serazene_venecky[3]
tri_nejmensi = serazene_venecky[-3]
print(tri_nejmensi)
print(tri_nejvetsi)



print(max([1,2,3]))

print(upper('ahoj')) #text
print(upper(3.14)) # tohle nejde

print('martin'.upper())
print([1, 2, 3, 1].count(1))

print('   \t ahoj      \n'.strip())


print('Olena, Ilina'.split(', '))


jmena = ['Kuba', 'Petr', 'Magda']
print('-'.join(jmena))

print('/'.join(['dokumenty', 'dapraha', 'python', 'priklady']))

rozdeleny_text = ' \t ahoj   Kubo   \n'.split()  # ['ahoj', 'Kubo']
slozeny = ' '.join(rozdeleny_text)  # 'ahoj Kubo'
print(slozeny)


import math

print(math.ceil(3.14))
print(math.floor(3.14))


import math
import random
import statistics

print(random.randint(1, 2))

print(statistics.mean([1, 2, 3, 4]))'''


'''def greet_user(jmeno, titul):
    '''Pozdrav uživatele
    zadane jmeno
    '''
    print(f'ahoj {titul} {jmeno}')

name = 'Martin"'
greet_user(name, 'GG')

def sum_two_numbers(a,b):
    ''' Secti dve cisla a vrat vysledek.'''
    result = a + b
    return result

c= sum_two_numbers (1,2)
print(c)



def get_mark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
mark = get_mark(points)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points)
print(f"Výsledná známka je {mark}.")'''

def compose_greeting_dr(jmeno, titul='Dr.'):
    """Vytvoří pozdrav
    
    pokud není zadaný titul, použije se "Dr."
    """
    if titul == None:
        pozdrav = f'ahoj{jmeno}'
    else:
        pozdrav = f'ahoj {titul} {jmeno}'
    return pozdrav


print(compose_greeting_dr('Kuba'))
print(compose_greeting_dr('Markéta', 'CSc.'))