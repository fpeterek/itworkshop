# Funkce, třídy, moduly

Zatím jsme se naučili sčítat, odčítat, případně i násobit čísla. S tím si
bohužel moc nevystačíme. Proto se tato kapitola věnuje základnímu stavebnímu
bloku v moderních programovacích jazycích, funkcím. Funkce nám nabízí určitou
funkcionalitu, na jejímž základě můžeme postavit funkcionalitu jinou, vlastní.

Programovací jazyk Python obsahuje rozsáhlou knihovnu funkcí, tzv. 'standardní
knihovnu,' anglicky 'standard library'. Jak je již patrné z názvu, tato
knihovna je standardizovaná a musí ji obsahovat všechny implementace jazyka
Python. Díky tomu se nemusíme bát využívat funkce ze standardní knihovny.
Ať už si náš program spustíme kdekoliv, vždy víme, že tam bude stejná knihovna
se stejnými funkcemi.

### Funkce

Jak už bylo dříve zmíněno, funkce jsou v programovacích jazycích velmi
důležíté. Proto je třeba abychom správně pochopili princip jejich fungování
a jejich použití. Funkce bychom si mohli představit například jako matematické
funkce. Na vstupu funkci předáme argumenty, se kterými má pracovat. Funkce nám
argumenty zpracuje a vrátí nám na svém výstupu výsledek. Takto funguje například
funkce sinus dobře známá z matematiky. Pro vstup `0` nám funkce sinus vrátí
hodnotu `0`. Pro vstup `pi/2` nebo `90°` funkce sinus vrátí hodnotu `1`. Kdo
nevěří, může si to sám ověřit na kalkulačce.

Taková představa by však nebyla úplně vhodná. Není nutně špatná, je pouze
omezená. Funkce v programovacím jazyce Python toho totiž zvládnou daleko víc.
Funkce v jazyce Python totiž nemusí mít vůbec žádný vstup. Nebo naopak žádný
výstup. Nebo nemusí mít ani vstup, ani výstup. Na vstupu nemusí přijímat pouze
číselné hodnoty. Argumenty funkcí, a stejně tak výstupními hodnotami, můžou být
také řetězce znaků, seznamy, slovníky, nebo uživatelem definované objekty.

Funkce v jazyce Python nemusí být nutně matematické operace a transformace
vstupních hodnot. Funkce můžou také upravovat stav svých argumentů, upravovat
stav mimo funkci, nebo měnit své chování za pomocí podmínek na základě hodnot
vstupních argumentů.

#### Proč funkce?

Hlavní důvod, proč programátoři používají funkce, je, že nám funkce umožní
určitý kus kódu používat vícekrát bez zbytečného kopírování. V době, kdy funkce
ještě neexistovali, museli programátoři, pokud chtěli využít kus kódu vícekrát,
kód několikrát zkopírovat, případně přímo použít skoky. Skoky vedly ke špatně
čitelnému kódu, kódu, který neformálně označujeme jako `spaghetti code`, neboť
právě špagety docela dobře vystihují strukturu takového kódu. V případě
kopírování byl zase zdrojový kód zbytečně dlouhý a špatně se upravoval. Pokud
bychom našli chybu v části kódu, museli bychom tu samou chybu opravit vícekrát,
jednou pro každou kopii. Pomocí funkcí také můžeme vytvářet knihovny, podobné
těm, které programovací jazyk Python nabízí již v základu.

### Třídy a objekty

Třídy, a s nimi úzce spojené objekty, jsou již o něco složitější koncept.
Bohužel se bez něj však v jazyce Python moc neobejdeme, takže je alespoň
základní pochopení principu konceptu objektů nezbytné.

Třídy a objekty jsou základním konceptem stylu programování, kterému se říká
objektově orientované programování, zkráceně OOP. Principem OOP je modelování
objektů skutečného světa za pomocí virtuálních modelů. Tomuto modelu se říká
třída. Třída definuje určitý počet proměnných (atributů), které daný objekt
popisují, a také určitý počet funkcí, které nad daným objektem provádí určité
operace. Takovýmto funkcím říkame členské funkce, případně metody. Třída slouží
jako šablona, podle které se vytváří konkrétní objekty. Objekt je soubor
proměnných, které definuje třída. S objektem můžeme pracovat za pomocí členských
funkcí, které jsou definovány třídou.

Tato definice se nejspíše bude neprogramátorům zdát matoucí. Ukážeme si tedy
příklad, který účel tříd a objektů, a rozdíl mezi nimi, snad osvětlí o něco
lépe.

```Python
Třída Letadlo:
    atributy: model, registrace, typ motoru
    metody: leť(počátek, destinace)

Objekty:
    Airbus A350-1000, registrace G-XWBA, motor Rolls Royce Trent XWB  # British Airways Airbus A35K
    Boeing 787-8, registrace A7-BCR, motor Rolls Royce Trent 1000     # Qatar Airways Boeing 787 Dreamliner
    Airbus A380-800, registrace A6-EUE, motor Rolls Royce Trent 900   # Emirates Airbus A380
```

Jak můžeme vidět, třída je pouze jedna, a definuje několik atributů, které
popisují letadlo. Také definuje metodu leť, za pomocí které řekneme letadlu,
aby letělo z jednoho bodu do druhého. Je zřejmé, že třída Letadlo popisuje
letadlo obecně. Nevyjadřuje však žádné konkrétní letadlo.

Objektů naopak máme více. Říkáme, že objekty jsou instance třídy Letadlo.
Každá instance má nastavené atributy na své vlastní požadované hodnoty a
odpovídá jednomu skutečnému konkrétnímu letadlu. Konkrétnímu letadlu také
můžeme přikázat, aby uskutečnilo let z jednoho letiště na druhé.

```Python
dreamliner.leť(WSSS, OMDB)  # Pošleme letadlo Boeing 787 Dreamliner na let z letiště Singapore Changi na letiště Dubai International
```

Objektově orientované programování se v praxi používá velmi často, právě díky
možnosti modelovat objekty skutečného světa, ale také díky spoustě dalších věcí,
které OOP nabízí, jako třeba zvýšená modularita kódu nebo skrytí nadbytečných
detailů implementace. OOP je ovšem poněkud složitější problematika, kterou se
nyní nebudeme zabývat více než je třeba.

### Používání funkcí a tříd

Pokud bychom chtěli získat výsledek nějaké funkce, musíme ji nejprve zavolat
(anglicky call, invoke). Volání (invokace) funkce je jednoduché. Nejprve
napíšeme název funkce, kterou chceme vyvolat. Za název funkce poté dopíšeme
kulaté závorky, ve kterých vyjmenujeme případné argumenty (parametry), které
funkci potřebujeme předat. Volání funkcí si můžeme vyzkoušet například
na funkcích `min` nebo `max`, které jsou součástí jazyka Python.

Funkce `max` přijímá nespecifikovaný počet parametrů a vrátí parametr
s nejvyšší hodnotou. Funkce `min` analogicky vrací parametr s nejnižší hodnotou.

```Python
# Volání funkce bez parametru
list()  # Vrátí prázdný seznam (viz. pozdější kapitoly)

# Volání funkce s jedním parametrem
bin(747)  # Vrátí binární reprezentaci čísla 747

# Volání funkce s více parametry
max(3, 5, 13, -20)  # Vrátí 13
```

Návratovou hodnotu funkce můžeme přímo využít v dalším výpočtu, jako argument
jiné funkce, nebo si ji můžeme přiřadit do proměnné

```Python
greatest = max(4, 2, 15, 7, 3)  # Přiřazení výsledku funkce proměnné greatest
min(-1, 3, max(-2, -10, -4), 25)  # Využití výsledku jedné funkce jako argumentu jiné funkce
5 + max(2**3, greatest)  # Využití proměnné jako argumentu funkce, využití výsledku funkce v jiném výpočtu
```

Třídu instancujeme (vytvoříme z ní objekt) způsobem podobným volání funkce.
Za název třídy dopíšeme kulaté závorky, mezi které zapíšeme případné parametry
objektu. Výsledkem tohoto volání je poté instancovaný objekt, který můžeme
využít úplně stejně jako v přechozím případu.

```Python
letadlo = Letadlo('A350-1000', 'G-XWBB', 'Rolls Royce Trent XWB')
dreamliner = Letadlo('Boeing 787-8 Dreamliner', 'A7-BCO', 'Rolls Royce Trent 1000')
```

Při práci s objekty se neobejdeme bez operátoru `.`. Operátor `.` slouží
k přístupu k atributům objektu, ale také k volání členských funkcí (metod)
nad objekty. Využití operátoru `.` je jednoduché. Nejprve napíšeme název
proměnné, k jejímž atributům chceme přistoupit. Poté napíšeme `.` a za ni název
atributu, případně volané metody. V případě volání metody za její název
zapíšeme kulaté závorky a voláme ji stejně jako obyčejnou funkci. Pokud bychom
chtěli přistoupit k atributu atributu, můžeme přístupy pomocí operátoru `.`
jednoduše řetězit.

```Python
letadlo.motor  # Přístup k atributu motor
letadlo.let('WSSS', 'OMDB')  # Volání metody let nad objektem letadlo
letadlo.motor.tah  # Přístup k atributu atributu
letadlo.motor.start()  # Volání metody nad atributem
```

### Moduly

Jak již víme, často je vhodné kód organizovat do funkcí, případně tříd.
S rostoucí komplexitou programu ale rychle roste také množství funkcí a tříd.
Nakonec tak můžeme stále skončit s nepřehledným a těžko udržovatelným kódem.
Proto v Pythonu vznikly moduly. Moduly nám umožňují funkce logicky uspořádávat
dle svého účelu. Modul v Pythonu je pouze obyčejný textový soubor s příponou
`.py`, který obsahuje kód v jazyce Python. Pokud bychom poté chtěli využít
některé z funkcí z určitého modulu, stačí nám daný modul importovat pomocí
direktivy `import`. Jakmile máme modul importovaný, používáme jej podobně jako
objekty, tedy přistupujeme ke členům modulu za pomocí operátoru `.`.

```Python
import math  # Import modulu math, který je součástí standardní knihovny jazyka Python

math.pi  # Přístup k proměnné definované v modulu math
math.cos(math.pi)  # Volání funkce definované v modulu math
cos_pi = math.cos(math.radians(180))

import turtle
t = turtle.Turtle()  # Vytvoření objektu podle třídy definované v modulu turtle
```

Výhodou modulu je také jeho znovupoužitelnost. Pokud bychom chtěli jeden modul
použít ve více programech, stačí nám pouze daný modul v obou programech
importovat. Nemusíme tak kopírovat žádný kód, a v případě, že bychom chtěli
provést změny v modulu, stačí změný provést pouze na jednom místě.

---

<div style="text-align: left"  > <a href="basic_math.md">Předchozí kapitola   </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět                  </a> </div>
<div style="text-align: right" > <a href="data_types.md">Následující kapitola </a> </div>
