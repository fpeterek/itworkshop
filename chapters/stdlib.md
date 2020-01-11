# Moduly, funkce ze standardní knihovny

Se sčítáním a odčítáním čísel si bohužel moc nevystačíme. Už jen kvůli
výpočtu souřadnic ve 2D prostoru často potřebujeme goniometrické funkce.
Naštěstí jazyk Python obsahuje rozsáhlou knihovnu tříd a funkcí. Této knihovně
často říkáme 'standardní knihovna,' anglicky 'standard library.' Tato knihovna
je, jak již název napovídá, standardizovaná. Nachází se tedy ve všech
implementacích jazyka Python na všech platformách, a vždy ve stejné podobě.

### Funkce

Funkce jsou v moderních programovacích jazycích velmi důležité. Mohli bychom
si je představit například jako matematické funkce. Na vstupu funkci předáme
argumenty, se kterými má pracovat. Funkce nám argumenty zpracuje a vrátí nám
na svém výstupu výsledek. Takto funguje například funkce sinus dobře známá
z matematiky. Pro vstup `0` nám funkce sinus vrátí hodnotu `0`. Pro vstup `pi/2`
nebo `90°`funkce sinus vrátí hodnotu `1`. Kdo nevěří, může si to sám ověřit na
kalkulačce.

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
kód několikrát zkopírovat, případně použít skoky. Skoky vedly ke špatně
čitelnému kódu, kódu, který neformálně označujeme jako `spaghetti code`, neboť
právě špagety docela dobře vystihují strukturu takového kódu. V případě
kopírování byl zase zdrojový kód zbytečně dlouhý, a špatně se upravoval. Pokud
bychom našli chybu v části kódu, museli bychom tu samou chybu opravit vícekrát,
jednou pro každou kopii. Pomocí funkcí také můžeme vytvářet knihovny, podobné
těm, které programovací jazyk Python nabízí již v základu.

### Třídy a objekty

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

```
Třída Letadlo:
    atributy: model, registrace, typ motoru
    metody: leť(počátek, destinace)

Objekty:
    Airbus A350-1000, registrace G-XWBA, motor Rolls Royce Trent XWB  # British Airways Airbus A35K
    Boeing 787-8, registrace A7-BCR, motor Rolls Royce Trent 1000     # Qatar Airways Boeing 787 Dreamliner
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

```
dreamliner.leť(WSSS, OMDB)  # Pošleme letadlo Boeing 787 Dreamliner na let z letiště Singapore Changi na letiště Dubai International
```