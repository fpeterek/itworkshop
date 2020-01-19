# Spouštění programů z terminálu, IDE

V příští kapitole již trochu naroste složitost kódu a prostředí IDLE přestane
být vhodné. Z tohoto důvodu přejdeme k jinému prostředí, IDE Pycharm.

#### Co je to IDE

IDE (Integrated Development Environment) je prostředí vytvořené za účelem psaní
a debugování kódu. Nabízí zvýrazňování syntaxe, našeptávač kódu, nástroje pro
spouštění, testování a debugování programu a spoustu dalších funkcí. My
využijeme IDE PyCharm. Prostředí PyCharm nabízí kromě verzi placenou i
neplacenou. Placená verze je ovšem poskytována studentům zdarma. Prostředí
PyCharm [lze stáhnout zde](https://www.jetbrains.com/pycharm/download/).


Místo IDE můžeme také využít jakýkoliv textový editor, přednostně pak editor,
který podporuje zvýrazňování syntaxe (anglicky 'syntax highlighting') pro jazyk
Python.

## Vývojové prostředí PyCharm

Placeholder

## Spouštění programů z terminálu

Programy napsané v jazyce Python lze také spouštět z terminálu (v Linuxu,
mac OS) nebo z příkazové řádky (Windows). Příkaz pro spuštění programu je
naštěstí stejný ve všech třech operačních systémech.

```Bash
python3 /path/to/file.py
```

Nejjednodušší řešení samozřejmě je přesunout se do složky se zdrojovými kódy
za pomocí příkazu `cd`. Poté je totiž stačí jako cestu k souboru zadat pouze
název daného souboru.

Za využití následujících příkazů můžeme na ploše vytvořit složku test,
ve které vytvoříme soubor main.py, do kterého následně můžeme psát zdrojový
kód a poté jej i spustit. Příkazy fungují pouze v operačních systémech Linux
a mac OS.

```Bash
cd Desktop/     # Přesun do složky Desktop (na systémech v češtině je třeba napsat 'Plocha' místo 'Desktop')
mkdir test      # Vytvoření nové složky test
cd test         # Přesun do složky test
touch main.py   # Vytvoření soubory main.py

# Následující příkaz je nepovinný. Místo něj můžeme soubor upravit v libovolném
# textovém editoru.
echo 'print("Hello, World!")' > main.py # Zapsání programu 'Hello, World!' do souboru


python3 main.py # Spuštění souboru main.py
```

Vše lze samozřejmě provést také v grafickém rozhraní, nemusíme nutně používat
terminál. Spousta programátorů ale po nějaké době začne preferovat textové
rozhraní terminálu, jelikož jim přijde rychlejší a příjemnější na použití
(opravdu, věřte mi).

---

<div style="text-align: left"  > <a href="terminal.md">Předchozí kapitola </a> </div>
<div style="text-align: center"> <a href="../README.md">Zpět              </a> </div>
<div style="text-align: right" > <a href="turtle.md">Následující kapitola </a> </div>
