# Rendszerterv

## 1. A rendszer célja:
A cég igazgatója szeretne egy olyen játékot, ami az ő elképezelése alapján készülne el, azért, hogy egyrészt egy olyat készíthessenek ami több korosztály számára is megfelelő, másrészt ennek a játéknak oktató jellegűnek és szorakoztatónak is kellene lennie. Egy ilyen játék nagyban megdobná a tábor presztizsét, még ha nem is küszködnek ilyen gondokkal, illetve marketing fogásként is nagyszerű.

A játék tervezésekor fontos, hogy egyszerű felülettel kell rendelkezzen, és még a fiatalabb
felhasználók is (5-8) évesek is könnyen tudjanak navigálni benne és megérteni annak elemeit.

## 2. Projekt terv:
Kezdés időpontja: 2021.09.06   
Tervezett befejezés dátuma: 2021.10.04   
Feladatok és hatáskörök a Trello-n vannak kezelve.  
A projekt fő lekövetése Trello-n keresztül történik.  
A gyors kommunikációra a Messengert használjuk.  
A hosszas egyeztetésekre és meetingekre Discord szervert használunk.  
Az elkészült elemeket Github-ra töltjük fel.  
### Projekten dolgozó fejlesztők:
* Orosz Regina
* Takács Balázs
* Batizi Máté
* Gyöngyösi Márk

## 4. Követelmények:

A rendszerterv az alábbi követelmények megvalósítását célozza meg:
* a játékban egy külön ablakban jelenjen meg
* a játékban jelenjen meg, hogy a játékos hogyan tudja irányítani a karakterét
* a játékban lehessen pontokat gyűjteni a megölt ellenfelek után és ezt egy számláló mutassa az egyik sarokban
* a játék felülete legyen egyszerű
* a menü legyen egyértelmű és egyszerű
* a high-score jelenjen meg a menü felületén
* az eredmények eltárolása adatbázisban

## 6. Absztrakt domain modell:
A programunkban az MVC programtervezési mintát követjük. Ez a minta három részből áll: Modell, Nézet, és Vezérlő.
A modell valósítja meg az üzleti logikát.
A nézet felel a felhaszálói felület megjelenítéséért. Itt jelenik meg a felhasználónak szánt adatok.
A vezérlő egy kapcsoló elem. Fogadja a felhasználói utasításokat és továbbítja azt a modell réteg felé, valamit a modell adatait a nézet felé.

## 7. Tesztterv:
### 7.1 Fő részek:
* 7.1.1 teszt végrehajtása
* 7.1.2 észrevételek dokumentálása
* 7.1.3 teszt dokumentáció archiválása

### 7.2 A tesztelést manuálisan kell végrehajtani. A teszt akkor sikeres, ha a program minden komponensét átnézve (ebben értendő az ellenféllel való harc, a saját karakter mozgatása) rendben működik és nem kapunk hibaüzentet vagy programleállást.

### 7.3 A manuális tesztelés során egy tesztjegyzőkönyvet kell készíteni amiben dokumentálva van a tesztelt funkció annak elvárt viselkedése, a funkció által adott viselkedés és az, hogy ez sikeres/sikertelen.


## 8. Telepítési terv:
* 8.1 A program futtatásához python-ra van szükség amit a https://www.python.org/downloads/ weboldalról lehet telepíteni. A verziószámának 3.0+ - nak kell lennie.
* 8.2 Szükség van még a nyílt forráskódú kivy programozói könyvtárra, amit erről a weboldalról lehet letölteni és telepíteni: https://kivy.org/doc/stable/gettingstarted/installation.html.

