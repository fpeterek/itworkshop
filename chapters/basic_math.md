# Aritmetické operace, proměnné a komentáře

Počítač, od slova `počítat`, anglicky `compute`, vznikl za účelem
automatizace výpočtů a práce s číselnými daty. Jako takový tedy
nejspíš dokáže docela dobře počítat. Nedokáže však pracovat
s obrázky, textem, nebo třeba 3D modely. Proto je třeba data tohoto
typu vyjádřit pomocí čísel. Toto už naštěstí zvládli programátoři
desítky let před námi a my se tím nemusíme zabývat, měli bychom ovšem
alespoň vědět, jak se s čísly pracuje.

V této části budeme používat prostředí IDLE. Alternativně lze také
využít prostředí `ipython`, které spustíme terminálovým příkazem
`ipython3`, nebo jen obyčejný terminálový shell, do kterého se
dostaneme pomocí příkazu `python3`.

## Komentáře

Komentáře se v jazyce Python denotují znakem `#`. Vše od znaku `#` až
po konec řádku je považováno za komentář. Komentáře jsou překladačem ignorovány,
slouží tedy pouze programátorům. Komentáře můžeme využít třeba k vysvětlení
složitější části kódu, dočasnému 'vyřazení' kódu, aby jej překladač ignoroval,
nebo k sepsání věcí, které je ještě třeba dodělat.

## Jednoduchá aritmetika

Zapsáním jednoduchého matematického výrazu do prostředí IDLE a jejím
následným spuštěním můžeme získat výsledek námi zadaného výrazu.

V programovacím jazyce Python můžeme využívat následující operátory

**Sčítání (`+`)**

Výraz: `10 + 15`

Výsledek: `25`

**Odčítání (`-`)**

Výraz: `15 - 10`

Výsledek: `5`

**Násobení (`*`)**

Výraz: `5 * 3`

Výsledek: `15`

**Dělení (`/`)**

Výraz: `25 / 2`

Výsledek: `12.5`

**Dělení bez zbytku (`//`)**

Výraz: `25 // 2`

Výsledek: `12`

**Zbytek po dělení (`%`)**

Výraz: `26 % 3`

Výsledek: `2`

**Mocnina (`**`)**

Výraz: `2 ** 10`

Výsledek: `1024`

Výraz: `9 ** 0.5`

Výsledek: `3`

**Řetězení**

Matematické výrazy lze samozřejmě řetězit. V takovém případě platí známá
matematická pravidla o pořadí operací (násobení má přednost před
sčítáním, apod.)

Výraz: `2 + 2 * 4`

Výsledek: `10`

**Závorky**

Pořadí operací lze změnit pomocí obyčejných závorek

Výraz: `(2 + 2) * 4`

Výsledek: `16`

## Proměnné

Často si budeme chtít nějakou hodnotu uložit, abychom ji mohli využít
znovu. Může to být například nějaká matematická konstanta nebo výsledek
předchozího výpočtu. Jakmile proměnné přiřadíme nějakou hodnotu,
proměnná se stává s přiřazenou hodnotou zaměnitelná.

Název proměnné může obsahovat malá a velká písmena, čísla a podtržítka,
začínat ale musí podtržítkem nebo písmenem.

Proměnnou přiřadíme pomocí operátoru `=`.

Existující proměnné samozřejmě můžeme přiřadit i novou hodnotu,
nerovnající se současné hodnotě proměnné

Příklad:

```
>>> pi = 3.14
>>> pi
3.14
>>> radius = 5
>>> area = pi * radius**2
>>> area
78.5
>>> pi = pi * 2
>>> pi
6.28
>>> long_variable_name = 10
```

## Zkrácený zápis modifikace proměnné

Pokud chceme proměnné přiřadit novou hodnotu, která je vypočtená
pomocí současné hodnoty, můžeme využít zkráceného zápisu.

Pokud bychom k proměnné `x` chtěli přičíst hodnotu `y`,
mohli bychom přičtení provést dvěma způsoby.

Způsob 1, obyčejný zápis:

`x = x + y`

Způsob 2, zkrácený zápis:

`x += y`

Tento zkrácený zápis funguje se všemi výše zmíněnými aritmetickými
operátory.

Příklad:

```
>>> x = 10
>>> x = x * (1.1 + 0.1)
>>> x
12
>>> x = 10
>>> x *= 1.1 + 0.1
>>> x
12
>>> x = 10
>>> x += x
>>> x
20
```

---

<div style="text-align: left"  > <a href="idle.md">Předchozí kapitola   </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět            </a> </div>
<div style="text-align: right" > <a href="functions.md">Příští kapitola </a> </div>
