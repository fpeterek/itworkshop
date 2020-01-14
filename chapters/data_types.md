# Datové typy

Datové typy nejsou v jazyce Python dodržovány tolik, jako v některých jiných
jazycích. Díky tomu je vývoj v jazyce Python rychlejší a pohodlnější, ale také
díky tomu může vzniknout celá řada bugů, které by se v jazyce, který
na dodržování datových typů dbá více, vůbec nikdy neobjevily. I přes nižší
podmínky na dodržování datových typů bychom o nich však stejně měli něco vědět.
Nejenom že se každý programátor ve svém životě setká s alespoň jedním jazykem,
který je v tomhle ohledu striktnější, ale i v jazyce Python nám znalost toho,
co je to datový typ, přijde vhod.

Pozorní čtenáři, kteří nepřeskočili úvod, ví, že v počítači jsou všechna data
reprezentována číselně. Všechna data, včetně textu nebo dat složených z více
prvků (tedy objekty). Samotné číslo, nebo přesněji skupina bitů, ovšem nemá
bez kontextu žádný význam. Co znamená `0b1111010011010000`? Nevíme. Nemůžeme to
vědět, aniž bychom měli nějaký dodatečný kontext. Nemůžeme říct, jakou hodnotu
skupina bitů reprezentuje, pokud nemáme popis struktry dat.

Datové typy, téma této kapitoly, slouží právě k popsání těchto dat. Určují, co
znamená skupina bitů, a jak s nimi počítač může pracovat. V minulé kapitole jsme
se věnovali třídám a objektům. Řekli jsme si, že objekt je popsán třídou.
Nepřípomíná tato věta náhodou něco, co jsme již zmínili výše? Že skupiny bitů
jsou popsány datovým typem? Každá jednotlivá třída je totiž datovým typem,
zatímco objekty jsou skupiny bitů, kterým význam dodává až jejich datový typ.

V jazyce Python naštěstí platí, že datový typ je vždy třídou, a že data jsou
vždy objekt. V ostatních jazycích to tak ovšem platit nemusí. Třída bude vždy
datovým typem, datový ale nemusí být třídou. Stejně tak objekt budou vždy data,
data ale nemusí nutně být objektem.

## Základní datové typy v jazyce Python

Standardní knihovna jazyka Python obsahuje velké množství tříd, které nalezneme
v modulech. Kromě těchto tříd ale Python implementuje také několik základních
datových typů, které jsou přímou součástí jazyka Python a nemusíme je
importovat. Tyto datové typy jsou `int`, `float`, `bool`, `str`, `list` a další
jako třeba `set` nebo `dict`, kterým se z důvodu jejich složitější nátury
nebudeme nyní věnovat.

## `int`

Datový typ `int`, z anglického slova 'integer', popisuje celé číslo, ať už
záporné, kladné, nebo nulu. Datový typ `int` je velmi jednoduchý a přímočarý
na použití. Pokud zapíšeme celé číslo, vytvoříme objekt typu `int`. Tato čísla
můžeme sčítat, odčítat, násobit, dělit, můžeme s nimi počítat stejně, jako jsme
zvyklí z matematiky. Pokud bychom chtěli vytvořit celé číslo z čísla
desetinného, případně třeba z řetězce (viz pozdější odstavec o typu `str`),
můžeme tak udělat zavoláním `int`, jako by to byla funkce. Parametrem, který
při volání předáme, bude hodnota, kterou na celé číslo chceme převést.

## `float`

Datový typ `float`, z anglického 'floating point number', reprezentuje číslo
s plovoucí řadovou čárkou. Řečeno srozumitelněji, datový typ `float`
reprezentuje reálné (desetinné) číslo. Práce s typem `float` je analogická práci
s typem `int`. Nesmíme ovšem zapomenout, že v jazyce Python se místo desetinné
čárky zapisuje desetinná tečka, podobně, jako se tečka píše v anglicky mluvících
zemích. Pokud bychom tedy chtěli specifikovat reálné číslo, uděláme to
následujícím stylem

```Python
pi = 3.14159
```

## `bool`

Datový typ `bool`, z anglického 'boolean', používáme, pokud chceme reprezentovat
jednu logickou hodnotu. Logické hodnoty jsou dvě, `True` a `False`, a používáme
je při rozhodování v podmínkách, což je téma, které probereme později.

Nad logickými hodnotami můžeme provádět tři základní operace, negaci, logický
součin a logický součet. Tyto názvy možná na první pohled zní složitě,
ve skutečnosti na nich ale nic složitého není.

#### Negace

Negace se v jazyce Python značí klíčovým slovem `not`. Negace logické hodnoty
nám vrátí logickou hodnotu opačnou. Tedy negací hodnoty `True` získáme `False`,
a naopak.

```Python
not True  # False
value = False
not value  # True
```

#### Logický součin

Logický součin už je třeba provést na dvou logických hodnotách. Logický součin
provádíme pomocí operátoru `and`. Logický součin vrátí hodnotu `True`, pokud
mají oba dva operandy součinu hodnotu `True`. V opačném případě vrátí hodnotu
`False`.

```Python
True and True         # True
True and False        # False
not (True and False)  # True
```

#### Logický součet

Logický součet taktéž provádíme na dvou logických hodnotách. Logický součet
vrátí hodnotu `True`, jestliže alespoň jeden z operandů odpovídá hodnotě `True`.
Jestliže jsou oba operandy `False`, bude i výsledkem logického součtu `False`.
Pro logický součet používáme operátor `or`.

```Python
True or True        # True
True or False       # True
False or False      # False
False or not False  # True
```

### Porovnávání hodnot

Porovnávání hodnot úzce souvisí s datovým typem `bool`, neboť porovnání vrací
jako svůj výsledek právě logickou hodnotu. Přesněji řečeno, pokud je výsledek
porovnání pravidivý, vrací porovnávací operace hodnotu `True`. V opačném případě
vrací hodnotu `False`.

V programovací jazyce Python existuje několik operátorů určených k porovnávání

#### Operátor `==`

Operátor rovnosti. Vrácí `True`, jestliže se operandy rovnají.

```Python
1 == 1  # True
1 == 2  # False
```

#### Operátor `!=`

Operátor nerovnosti, vrací `True`, jestliže se hodnoty nerovnají.

```Python
1 != 2  # True
1 != 1  # False
```

#### Operátor `<`, `>`

Operátor `<` vrací hodnotu `True`, pokud má pravý operand vyšší hodnotu, než
operand levý. Operátor `>` funguje analogicky.

```Python
1 < 2  # True
2 < 2  # False
2 > 1  # True
```

#### Operátor `<=`, `>=`

Operátor 'menší nebo rovno' (`<=`) a 'větší nebo rovno' (`>=`). Narozdíl
od operátorů `<` a `>` vrací hodnotu `True` také pokud se hodnoty rovnají.

```Python
1 <= 2  # True
2 <= 1  # False
2 >= 2  # True
```

#### Řetězení porovnávacích operátorů

Porovnávací operátory v jazyce Python lze také řetězit. Takto zřetězený výraz
vrátí hodnotu `True` pouze pokud jsou všechna porovnání ve výrazu pravdivá.

```Python
1 == (2 - 1) < 3 > 2 != -1  # True
```

#### Přetypování nelogických hodnot na hodnoty logické

Všechny hodnoty v programovacím jazyce Python lze převést na hodnotu logickou.
Logickou hodnotu takto můžeme získat z hodnoty nelogické podobně jako když
bychom chtěli získat hodnotu celočíselnou. Zavoláme `bool` podobně, jako bychom
chtěli volat funkci. Při volání jako argument předáme hodnotu, kterou bychom
chtěli převést na hodnotu `True`, `False`.

Při přetypování platí následující pravidla:

1) Všechny číselné hodnoty, které se nerovnají 0, odpovídají hodnotě `True`
2) Nula odpovídá hodnotě `False`
3) Všechny neprázdné kolekce(viz zbytek kapitoly) odpovídají hodnotě `True`
4) Všechny prázdné kolekce odpovídají hodnotě `False`
5) Hodnota `None` (viz pozdější odstavec) vždy vrací `False`
6) Všechny ostatní objekty vrací `True`, pokud nemají definovanou vlastní
konverzi

## `str`

Řetězec, v Pythonu `str`, z anglického 'string' je datový typ sloužící
k reprezentování textu. Objekt typu `str` vytvoříme pomocí uvozovek, ať už
jednoduchých, nebo složených. Důležité je, aby byl ten samý typ uvozovek
na začátku i na konci řetězce a aby se uvozovací znak neobjevoval uprostřed
řetězce, protože by počítač nemusel poznat, kde přesně má řetězec končit.

V řetězci si samozřejmě můžeme ukládat jakýkoliv text chceme. Řetězce můžeme
sčítat, a dokonce můžeme řetězec násobit celým číslem, pokud bychom chtěli
obsah řetězce zopakovat vícekrát. V řetězcích samozřejmě můžeme ukládat i čísla.
`'1234'` je v Pythonu validní řetězec. Musíme si ovšem dát pozor. Ačkoliv
obsahem tohoto řetězce jsou pouze čísla, řetězec jako číslo použít nemůžeme.
Výsledkem výrazu `'1234' * 2` nebude `2468`, ale `'12341234'`. Pokud bychom
chtěli z řetězce vytvořit číslo, můžeme tak učinit způsobem, jaký byl naznačen
již výše. Na celé číslo převedeme řetězec pomocí výrazu `int(retezec)`,
na desetinné číslo pomocí výrazu `float(retezec)`.

Třída `str` implementuje spoustu metod užitečných pro práci s textem. Mezi tyto
metody patří například metoda `lower`, která převede řetězec na malá písmena,
metoda `upper`, která řetězec naopak převede na velká písmena, metody
`startswith`, `endswith`, `replace`, a další. Tyto metody si ovšem nemá cenu
popisovat. Vše důležité lze totiž najít
v [dokumentaci](https://docs.python.org/3/library/stdtypes.html#textseq).

```Python
s = 'Airbus A350'

'Text s "uvozovkami"'  # Ano
"Text s 'uvozovkami'"  # Taky ano
'Text s 'uvozovkami''  # Ne

s.startswith('Air')  # True
s.endswith('747')  # False
s.replace('A350', 'A330')  # 'Airbus A330'

s * 2  # 'Airbus A350AirbusA350'
'1234' * 3  # '123412341234'
int('1234') * 3  # 3 702
```

### Formátování řetězců

Pokud víme, jaká data potřebujeme v řetězci uložit, není problém si celý
řetězec vytvořit už když píšeme kód. Pokud ale potřebujeme, aby obsah řetězce
závisel na vypočtené hodnotě, a nemůžeme předem říct, jaký co bude v řetězci
nakonec uloženo, může to být problém. Budeme totiž řetězec muset vytvořit až
za běhu programu. V Pythonu existuje více způsobů, jak takový řetězec vytvořit.
Zatím nejnovější, a taky nejjednodušší, způsob formátování řetězců jsou
takzvané f-stringy. F-stringy se, podobně jako obyčejné stringy, uvozují
uvozovkami, ať už jednoduchými, nebo dvojitými. Oproti obyčejným stringům
ale ještě před úvodní uvozovku přidáme znak `f`. Pokud bychom poté v f-stringu
chtěli uložit hodnotu proměnné, nebo nějakého výrazu, stačí nám v řetězci napsat
daný výraz, případně proměnnou, do složených závorek. Závorky se za běhu
programu nahradí skutečnou hodnotou výrazu.

```Python
f'1 + 1 = {1 + 1}'
x = 23
y = 39
'x + y = {x+y}'  # 'x + y = {x+y}'
'{x} + {x} = {x + y}'  # '{x} + {x} = {x + y}'
f'{x} + {x} = {x + y}'  # '23 + 39 = 62'
f'"Kobeřice".startswith("Ko") = {"Kobeřice".startswith("Ko")}'  # '"Kobeřice".startswith("Ko") = True'
```

## `list`

Posledním datovým typem, kterým se budeme v této kapitole zabývat, je seznam,
anglicky list. Seznamy nám umožňují ukládat předem nespecifikovaný počet hodnot.
