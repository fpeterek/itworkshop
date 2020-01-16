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
nebo **IDE**.

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
že je splněna určitá podmínka. Pokud není, kód se neprovede, počítač skočí
na konec bloku `if` a pokračuje dál v exekuci programu.

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



---

<div style="text-align: left"  > <a href="collections.md">Předchozí kapitola </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět                 </a> </div>
<div style="text-align: right" > <a href="turtle.md">Následující kapitola    </a> </div>
