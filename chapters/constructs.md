# Základní konstrukce jazyka Python

Nyní již umíme napsat jednotlivé řádky kódu. Umíme volat funkce, přiřazovat
hodnoty proměnným, vytvářet objekty. Možná bychom zvládli napsat jednoduchý
program, který by postupně vykonal sérii příkazů v pořadí, v jakém jsou zapsány.
Bohužel, toto nám nestačí k vytvoření komplexních programů. Ne vždy chceme, aby
byly instrukce vykonávány sekvenčně. V takovém případě je třeba využít skoků.

Skoky jsme nevědomě využili již dříve při volání funkcí. Když totiž voláme
funkci, počítač musí skočit v kódu na místo, kde se daná funkce nachází.
Následně vykoná kód funkce a nakonec se vrátí zpět na místo původního skoku.
Dále jsou skoky využívány při rozhodování podmínek nebo v implementaci cyklů.
A právě skokům, ale hlavně konstrukcím, jež skoky využívají, se věnuje tato
kapitola. Nejprve si ale budeme muset povědět něco o odsazování kódu, které
je v jazyce Python velmi důležité.

V této kapitole již opustíme prostředí IDLE a využijeme **textového editoru**
nebo **IDE**. Dále začneme názvy proměnných uvádět v angličtině.

## Odsazování

Ve většině ostatních jazyků se odsazování používá pouze z estetického hlediska
 - správně odsazený kód vypadá lépe a je čitelnější. V jazyce Python má ovšem
odsazování speciální význam. Využívá se k denotaci bloků, je součást syntaxe
jazyka Python a musíme tedy dodržovat přesně daná pravidla. To se sice může
novým programátorům zdát zbytečně náročné a komplikované, ve skutečnosti díky
striktním požadavkům na dodržování odsazování ovšem můžeme předejít řadě chyb
způsobených nečitelně napsaným kódem, a také se naučíme kód správně formátovat.

Při odsazování platí pravidlo, že jedna úroveň odsazení odpovídá čtyřem mezerám.
Úrovní odsazení přitom může být více, nebo nemusí být ani jedna. Platí, že
pokud část kódu patří do jednoho bloku, musí být všechny výrazy odsazeny stejně.
Příklad odsazení si ukážeme později. Z textu samotného využití a důležitost
odsazení příliš nevyplývá. Na příkladu ale vše bude vidět daleko lépe.

## Jeden příkaz na řádek

Pravidlo, kterého jsme se zatím celou dobu drželi, a které částečně vyplývá i
z předchozího odstavce. Je jej třeba zmínit, když už mluvíme o syntaxi jazyka
Python, ale jak již z nadpisu vyplývá, na jeden řádek můžeme psát maximálně
jeden příkaz. Naopak to ale neplatí. Pokud bychom měli příliš dlouhý výraz,
můžeme si jej rozložit na více řádků. Na jednom řádku by však více než jeden
příkaz být neměl. Stejně tak můžeme využít prázdných řádků, abychom kód
'zředili' a oddělili od sebe části kódu. Prázdné řádky nenarušují odsazení.

## Konstrukce `if`/`elif`/`else`

Konstrukci `if` využijeme, pokud chceme blok kódu provést pouze za předpokladu,
že je splněna určitá podmínka. Pokud podmínka splněná není, kód se neprovede,
počítač skočí na konec bloku `if` a pokračuje dál v exekuci programu.

Syntax konstrukce `if` je velmi jednoduchá. Za klíčové slovo `if` zapíšeme svou
podmínku (podmínkou může být jakýkoliv výraz, jehož výsledkem je hodnota typu
`bool`). Za podmínku napíšeme znak `:`. Dále od nového řádku zapisujeme kód,
který chceme provést pouze pokud bude podmínka pravdivá. Všimněte si, že zde již
musí být kód odsazen čtyřmi mezerami. Jakmile chceme blok `if` ukončit, snížíme
úroveň odsazení. Řetězec `'konec'` se tedy vypíše nezávisle na vstupu.

```Python
i = int(input('Číslo: '))
if i == 5:
    print('Vstup je roven pěti.')
    print(f'i**2 = {i**2}')
print('Konec')

# Výstup pro vstup '5'
#
# Vstup je roven pěti.
# i**2 = 25
# Konec

# Výstup pro jiný vstup
#
# Konec
```

Blok `elif` využijeme, jestliže potřebujeme alternativní podmínku k bloku `if`.
Větví `elif` může být více, zapisujeme je hned za větev `if`. Pokud se neprovede
větev `if`, začnou se kontrolovat alternativní podmínky v blocích `elif`.
Jestliže počítač narazí na pravdivou podmínku, danou větev provede, skočí na
konec `if`/`elif` konstrukce a pokračuje v programu dále. Pokud by počítač
nevyhodnotil ani jednu podmínku jako pravdivou, neprovede se žádný blok
a počítač pokračuje v programu za poslední `elif` větví. Blok `elif` je
nepovinný, zapsání `elif` bloku jinam než za `if` blok je ovšem chybou, která
zabrání spuštění programu. `elif` je zkratka pro 'else if'.

Blok `elif` se zapisuje stejně jako blok `if`, pouze místo klíčového slova `if`
využijeme klíčové slovo `elif`. Odsazujeme stejně jako u bloku `if`.

```Python
aircraft = input('Letadlo: ').lower()

if 'boeing' in aircraft:
    print('Výrobcem letadla je americká firma Boeing')
elif 'airbus' in aircraft:
    print('Výrobcem letadla je evropská firma Airbus')
elif 'comac' in aircraft:
    print('Výrobcem letadla je čínská firma COMAC')

print('Konec')
```

Blok `else` použijeme, pokud chceme, aby se provedl určitý kus kódu v případě,
že žádná z podmínek v předcházejících `if`/`elif` větvích není pravdivá. Pokud
je jedna z těchto podmínek evaluována jako pravdivá, a provede se větev `if`
nebo `elif`, větev `else` je ignorována. Větev `else` je nepovinná, můžeme ji
ale zapsat pouze za `if` nebo `elif` blok. V opačném případě nám počítač vypíše
chybu.

Blok `else` zapisujeme podobně jako blok `if`. Větev `else` ovšem nevyžaduje
podmínku, proto za klíčové slovo `else` dopisujeme rovnou `:` a podmínku
neuvádíme.

```Python
x = int(input('První číslo: '))
op = input('Operátor: ')
y = int(input('Druhé číslo: '))

if op == '+':
    print(f'{x} + {y} = {x+y}')

elif op == '-':
    print(f'{x} - {y} = {x-y}')

elif op == '*':
    print(f'{x} * {y} = {x*y}')

elif op == '/':
    print(f'{x} / {y} = {x/y}')

else:
    print('Neznámý operátor "{op}"')

print('Konec')
```

## Cykly

Často při psaní kódu chceme, aby se určitý kus kódu provedl vícekrát. Samozřejmě
nám nic nebrání dané řádky kódu jednoduše zkopírovat. Takové řešení je určitě
taky možné. Nese s sebou ovšem několik nevýhod. Zdrojový kód rychle roste
do délky a stává se špatně čitelným. Navíc se může stát, že ve zkopírovaném
kódu můžeme objevit chybu. Poté bychom museli všechen kód smazat a znovu
zkopírovat. Největší problém ale nastává v případě, kdy nevíme, kolikrát chceme
část kódu opakovat, nebo když chceme kód opakovat donekonečna.

K opakování určitého bloku kódu používáme v programování cykly. V programovacím
jazyce Python máme dva typy cyklů.

## Cyklus `while`

Cyklus `while` využijeme v případě, kdy chceme, aby se část kódu opakovala,
dokud podmínka odpovídá hodnotě `True`. Cyklus `while` zapisujeme úplně stejně
jako blok `if`, pouze místo klíčového slova `if` použijeme klíčové slovo
`while`. Kód se poté bude opakovat, dokud je podmínka splněna. Pokud je podmínka
`False` již při první kontrole, kód se neprovede vůbec.

```Python
number = 7
text = 'Hádej číslo v rozsahu 1 až 10: '
while int(input(text)) != number:
    print('Špatné číslo, hádej znovu.')
print(f'Správně. Číslo {number} je hledané číslo.')
```

Pokud bychom chtěli vytvořit nekonečnou smyčku, stačí jako podmínku použít
hodnotu `True`.

```Python
import time

i = 0
# Nekonečný cyklus lze ukončit stiskem ctrl+c
while True:
    print(i)
    i += 1
    time.sleep(1)
```

## Cyklus `for`

Cyklus `for` se nejčastěji využívá k průchodu kolekcí. Cyklus `for` vytvoří
proměnnou, do které postupně přiřazuje prvky z kolekce jeden za druhým. Pro
každou hodnotu v kolekci proběhne tělo cyklu právě jednou. Pozor! Pokud
proměnné využité cyklem `for` přiřadíme jinou hodnotu, změníme pouze danou
proměnnou, nezměníme původní hodnotu v kolekci.

```Python
fleet = ['Airbus A350', 'Airbus A320', 'Airbus A320', 'Airbus A321XLR']

for aircraft in fleet:
    print(aircraft)
```

### Třída `range`

Třída `range` je často využívána ve spojení s cyklem `for`. Objekty typu `range`
odpovídají sekvenci čísel. Při vytváření objektu typu `range` zadáme začátek,
konec, a případně krok v sekvenci. Pokud krok nezadáme, objekt `range` je
inicializován s krokem velikosti 1. Objekt typu `range` poté vygeneruje sekvenci
čísel podle zadaných parametrů. Sekvence začíná v zadaném začátku a hodnota
se postupně zvyšuje o zadaný krok, dokud nedojde do zadaného konce. Pozor,
specifikovaný konec už do sekvence nepatří.

```Python
for i in range(1, 10):
    print(i, end=' ')
print('')

# 1 2 3 4 5 6 7 8 9

for i in range(1, 10, 3):
    print(i, end=' ')
print('')

# 1 4 7
```

Objekt typu `range` není seznam a nelze jej jako seznam využít. Můžeme z něj
ale snadno seznam vytvořit, pokud bychom potřebovali.

```Python
lst = list(range(1, 11))
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Definice vlastních funkcí

Proč a jak využíváme funkce v programovacích jazycích jsme si ukázali
v předchozích kapitolách. Nyní si ukážeme, jak si můžeme vytvořit funkci
vlastní.

Při definici funkce využijeme klíčové slovo `def` (z anglického `define`).
Za klíčové slovo `def` zapíšeme název funkce. Název funkce následují kulaté
závorky, uvnitř kterých specifikujeme případné parametry. Za uzavírající kulatou
závorku zapíšeme znak `:`. Dále již pokračujeme na novém řádku, kde kód musíme
odsadit.

Pokud bychom chtěli z funkce vrátit nějakou hodnotu, můžeme tak udělat za pomocí
klíčového slova `return`.

```Python
import math

def greet(name):
    print(f'Hello, {name}!')

def hello_world():
    greet('World')

def calc_perimeter(radius):
    return round(math.pi * radius**2, 2)

def sum_of_numbers(lst):
    total = 0
    for i in lst:
        total += i
    return total

def is_valid_triangle(a, b, c):
    greatest = max(a, b, c)
    if a == greatest:
        return a < b + c
    elif b == greatest:
        return b < a + c
    return c < a + b


hello_world()  # Hello, World!
greet('Python')  # Hello, Python!
calc_perimeter(4)  # 50.27
sum_of_numbers(list(range(1, 11)))  # 55
is_valid_triangle(3, 4, 5)  # True
is_valid_triangle(3, 4, 8)  # False

---

<div style="text-align: left"  > <a href="collections.md">Předchozí kapitola </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět                 </a> </div>
<div style="text-align: right" > <a href="turtle.md">Následující kapitola    </a> </div>
