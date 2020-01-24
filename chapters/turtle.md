# Práce s modulem Turtle

Modul `Turtle` není modul, který by se při vývoji skutečných aplikací používal
velmi často. Tento modul totiž slouží především k výuce jazyka Python. Umožňuje
zkoušení různých konstrukcí v jazyce Python a jejich jednoduché a rychlé
grafické znázornění.

Modul `Turtle` importujeme za pomocí příkazu

```Python
import turtle
```

V modulu nalezneme třídu `Turtle`. Nejprve si musíme vytvořit objekt třídy
`Turtle`

```Python
t = turtle.Turtle()  # Inicializuje želvu
t.shape('turtle')  # Nastaví želvě tvar skutečné želvy (nepovinné)
```

Objekt při své inicializaci vytvoří okno s želvou uprostřed. Za pomocí metod
můžeme želvu rozpohybovat. Želva za sebou zanechává stopu. Takto můžeme kreslit
obrazce a hrát si s jazykem Python.

```Python
t.forward(100)
```

## Příklady

Příklady jsou samozřejmě dobrovolné, avšak silně doporučené pro čtenáře,
kteří si stále jsou jistí, že se chtějí programování naučit. Seznam všech metod,
které jsou k dokončení příkladů potřeba, je dostupný níže.

1) Nakreslit čáru

2) Nakreslit kruh

3) Nakreslit přerušovanou čáru pomocí cyklu

4) Nakreslit trojúhelník, nejlépe pomocí cyklu

5) Nakreslit čtverec pomocí cyklu

6) Nakreslit šestiúhelník pomocí cyklu

7) Nakreslit znak Audi pomocí cyklu, nejlépe pomocí cyklu

8) Nakreslit logo Olympijských her, lze využít cyklu

9) Nakreslit kruh pomocí cyklu (bez metody `circle`)

10) Nakreslit vlny

11) Nakreslit vlny bez metody `circle`, nejlépe bez použití kódu z příkladu 8

## Seznam potřebných metod

### forward(distance)

Parametry:

* distance - vzdálenost, kterou má želva ujít

Funkce: Želva popojde o specifikovanou vzdálenost ve směru, kterým směřuje

Příklad:

```Python
import Turtle
t = turtle.Turtle()

t.forward(100)
```

### penup()

Parametry: žádné

Funkce: Zakáže kreslení stopy za želvou

Příklad:

```Python
import Turtle
t = turtle.Turtle()

t.forward(100)
t.penup()
t.forward(100)
```

### pendown()

Parametry: žádné

Funkce: Povolí kreslení stopy za želvou

```Python
import Turtle
t = turtle.Turtle()

t.penup()
t.forward(100)
t.pendown()
t.forward(100)
```

### right(angle)

Parametry:

* angle - úhel, o který se má želva otočit; udává se ve stupních

Funkce: Želva se otočí o `angle` stupňů doprava

Příklad:

```Python
import Turtle
t = turtle.Turtle()

t.right(45)
t.forward(100)
```

### left(angle)

Parametry:

* angle - úhel, o který se má želva otočit; udává se ve stupních

Funkce: Želva se otočí o `angle` stupňů doleva

Příklad:

```Python
import Turtle
t = turtle.Turtle()

t.left(135)
t.forward(100)
```

### circle(radius, extent)

Parametry:

* radius - poloměr kružnice, pokud je záporný, kružnice se kreslí opačným směrem

* extent - jaká část kružnice se nakreslí, udává se ve stupních (hodnota 180
           nakreslí polovinu kružnice, hodnota 45 jednu osminu...), tento
           parametr je nepovinný

```Python
import Turtle
t = turtle.Turtle()

t.circle(50)
t.penup()
t.forward(100)
t.pendown()
t.circle(50, 180)
t.penup()
t.forward(200)
t.pendown()
t.circle(50, 45)
```

### reset()

Parametry: žádné

Funkce: Resetuje stav želvy a vyčistí okno

```Python
import Turtle
t = turtle.Turtle()

t.circle(100)
t.reset()
```


Třída `Turtle` obsahuje ještě spoustu dalších metod, které lze [dohledat
v dokumentaci](https://docs.python.org/3.3/library/turtle.html). Příklady
z této kapitoly je ale možné vyřešit pouze za pomocí výše zmíněných metod třídy
`Turtle`.

---

<div style="text-align: left"  > <a href="constructs.md">Předchozí kapitola </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět                </a> </div>
