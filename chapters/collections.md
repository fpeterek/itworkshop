# Kolekce

Datovým typům, které umožňují ukládat více prvků najednou, se říká kolekce.
V Pythonu existuje kolekcí spousta, my si ale probereme jen dvě, `str` a `list`.
Kolekce nám umožňují lépe organizovat kód a pracovat s množinou hodnot. Jazyk
Python také obsahuje spoustu funkcí pro práci s kolekcemi. Některé z nich si
ukážeme v následujících odstavcích.

## `str`

Řetězec, v Pythonu `str`, z anglického 'string' je datový typ sloužící
k reprezentování textu. Objekt typu `str` vytvoříme pomocí uvozovek, ať už
jednoduchých, nebo složených. Důležité je, aby byl ten samý typ uvozovek
na začátku i na konci řetězce a aby se uvozovací znak neobjevoval uprostřed
řetězce, protože by počítač nemusel poznat, kde přesně má řetězec končit.
Řetězec je kolekcí, protože reprezentuje množinu jednotlivých znaků.

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

s.startswith('Air')  # True
s.endswith('747')    # False
s.replace('A350', 'A330')  # 'Airbus A330'

s * 2  # 'Airbus A350AirbusA350'
'1234' * 3  # '123412341234'
int('1234') * 3  # 3 702
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
f'{x} + {x} = {x + y}'  # '23 + 39 = 62'
f'"Kobeřice".startswith("Ko") = {"Kobeřice".startswith("Ko")}'  # '"Kobeřice".startswith("Ko") = True'
```

## `list`

Posledním datovým typem, kterým se budeme v této kapitole zabývat, je seznam,
anglicky 'list'. Seznamy nám umožňují ukládat předem nespecifikovaný počet hodnot.
Tato vlastnost je užitečná především v případě, že předem nevíme, kolik vůbec
budeme chtít uložit hodnot. Další výhodou seznamu je ovšem také možnost
procházet jím pomocí cyklu (viz příští kapitola), což nám umožňuje psát kratší
a čitelnější kód. Také můžeme pomocí seznamu omezit počet proměnných. Měli
bychom si ale dát pozor. Seznamy jsou užitečná věc, ale bychom v nich nutně
ukládat vše pouze za účelem omezení počtu proměnných. Je velmi důležité, abychom
psali čitelný kód, a list vzájemně nesouvisejících hodnot, ke kterým
přistupujeme nesystematicky, může být velmi matoucí.

Zapsáním prázdných hranatých závorek vytvoříme nový prázdný seznam. Zapsáním
hodnot oddělených čárkami vytvoříme seznam zadaných hodnot. Tím ovšem práce
se seznamem nekončí. Seznam má totiž dynamickou velikost. Jinými slovy,
seznam se může zvětšovat i zmenšovat podle našich potřeb. Můžeme do něj kdykoliv
přidat novou hodnotu, odebrat z něj hodnotu starší, nebo přistupovat k současným
hodnotám a případně je upravovat.

Seznam je, jako všechno ostatní v jazyce Python, objekt. Pracujeme s ním tedy
pomocí metod. Mezi tyto metody patří například metoda `append`, která na konec
listu přidá nový prvek, metoda `pop`, která prvek z listu odstraní, nebo metoda
`sort`, která seznam seřadí. Metod je samozřejmě více a můžeme je všechny
dohledat v dokumentaci.

```Python
seznam = [1, 4, 2, 3]
seznam.append(5)
seznam.append(0)
seznam.pop()
seznam.sort()
print(seznam)  # [1, 2, 3, 4]

```

## Práce s kolekcemi

Kromě metod vlastních jednotlivým kolekcím obsahuje Python také několik funkcí,
které fungují nezávisle nad použitou kolekcí. Ty nejdůležitější si nyní
popíšeme.

### Funkce `len`

Funkce `len` přijímá jako svůj první argument kolekci. Její návratovou hodnotou
je délka předané kolekce.

```Python
len([])  # 0
len([1, 2, 3])  # 3
len("Airbus A350-1000")  # 16
```

### Přístup k jednotlivým prvkům

Pro přístup k jednotlivému prvku z kolekce používáme operátor `[]`. Za název
proměnné, případně za jakýkoliv jiný výraz, jejímž výsledkem je kolekce,
dopíšeme hranaté závorky, do kterých dopíšeme pořadové číslo (index) prvku,
který chceme získat. Při zadávání indexu prvku samozřejmě nemusíme zadávat
konkrétní hodnotu, můžeme použít i hodnotu vypočtenou, nebo můžeme využít
proměnnou. **Pozor, index prvního prvku je 0.** Pokud bychom tedy chtěli získat
první prvek, napíšeme `kolekce[0]`. Pokud bychom chtěli přistoupit k poslednímu
prvku kolekce, napíšeme `kolekce[len(kolekce) - 1]`.

```Python
seznam = ['a', 'b', 'c', 'd', 'e']
seznam[0]  # 'a'

index = 2
seznam[index]  # 'c'
seznam[4]  # 'e'
seznam[len(seznam) - 1]  # 'e'
'retezec'[3]  # 'e'
```

Užitečnou funkcí jazyka Python je také to, že nabízí indexaci od konce kolekce.
V takovém případě jako index prvku použijeme záporné číslo. Indexace od konce
kolekce začíná indexem -1.

```Python
[1, 2, 3][-1]  # 3
'retezec'[-5]  # t
```

### Operátor `in`

Operátor `in` se používá k ověření, že se hodnota nachází v kolekci. Na levou
stranu operátoru `in` zadáme hledanou hodnotu, na stranu pravou zadáme kolekci,
kterou chceme prohledat. Pokud se hodnota v kolekci nachází, vrátí výraz
s operátorem `in` hodnotu `True`, pokud ne, vrátí hodnotu `False`. Pokud bychom
chtěli operátor `in` znegovat, můžeme využít zápis `item not in collection`,
který se chová stejně jako výraz `not (item in collection)`, čte se ale
přirozeněji.

```Python
1 in [1, 2, 3]   # True
'a' in 'airbus'  # True
'a' in 'Airbus'  # False
-1 not in [1, 2, 3, 4]  # True
```

Pokud vyhledáváme prvky v řetězci, můžeme pomocí operátoru `in` hledat nejen
jednotlivé znaky, ale také podřetězce (anglicky 'substringy').ß

```Python
'A350' in `Airbus A350`  # True
```

---

<div style="text-align: left"  > <a href="data_types.md">Předchozí kapitola   </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět                  </a> </div>
<div style="text-align: right" > <a href="terminal.md">Následující kapitola </a> </div>

