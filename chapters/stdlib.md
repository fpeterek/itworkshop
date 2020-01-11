# Moduly, funkce ze standardní knihovny

Se sčítáním a odčítáním čísel si bohužel moc nevystačíme. Už jen kvůli
výpočtu souřadnic ve 2D prostoru často potřebujeme goniometrické funkce.
Naštěstí jazyk Python obsahuje rozsáhlou knihovnu tříd a funkcí. Této knihovně
často říkáme 'standardní knihovna,' anglicky 'standard library.' Tato knihovna
je, jak již název napovídá, standardizovaná. Nachází se tedy ve všech
implementacích jazyka Python na všech platformách, a vždy ve stejné podobě.

#### Funkce

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

##### Proč funkce?