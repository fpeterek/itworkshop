# Matematické operace
1 + 1
3 - 1
2 * 2
4 / 3
4 // 3
4 % 3
3 ** 3

# Deklarace proměnné
random_number = 4

# Volání funkce
max(1, 2, 3)

# Výpis na obrazovku
print(f'Random number: {random_number}')

# Vytvoření objektu dané třídy
ac = Aircraft()

# Přístup k atributu
ac.engine

# Volání metody
ac.fly('WSSS', 'OMDB')

# Import modulu
import turtle

# Logické hodnoty
x = True
y = False
x and y
x or y
not x

# Porovnání hodnot
2 > 1
2 >= 2
2 != 4
2 == (4 - 2)

# Převod řetězce na čísla
int('1234')
float('123.456')

# Formátování řetězců
f'2 ** 13 = {2 ** 13}'

# List
l = [1, 2, 3, 4]
l.append(5)

# Délka kolekce
len(l)

# Přistup k prvku kolekce
'Airbus A350-1000'[4]

# Kontrola, zda je prvek v kolekci
3 in l
'350' in 'Airbus A350'

# Podmínky
if a == b:
    print('A equals B')
elif a < b:
    print('A is less than B')
else:
    print('A is greater than B')

# Cyklus while
i = 0
while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i)

# Cyklus for
lst = [1, 3, 5, 7, 9]
for i in lst:
    print(i)
    if i == 7:
        break

# Rozsahy range
for i in range(0, 10):
    print(i)

# Vytvoření listu z range
lst = list(range(0, 10))

# Definice funkce
def multiply(x, y)
    result = x * y
    return result

