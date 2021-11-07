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


## 5. Ütemterv:
* 2021.09.06. - 2021.09.12. - Project öteltelés és megbeszélése a csapattal.
* 2021.09.13. - 2021.09.19. - Megbeszélés és a követlemény specifikációk elkezdése
* 2021.09.20. - 2021.09.26. - Megbeszélés és a funkcionális specifikációk elkezdése és a rendszerterv elkezdése, Demo fejlesztés elkezdése.
* 2021.09.27. - 2021.10.03. - A követlemény specifikációk, funkcionális specifikációk és rendszertervek a Demora megfelelő állapotra hozása
* 2021.10.04. - 2021.10.10. - Demo, követlemény specifikációk, funkcionális specifikációk, rendszerterv bemutatása
* 2021.10.11. - 2021.10.17.
* 2021.10.18. - 2021.10.24.
* 2021.10.25. - 2021.10.31.
* 2021.11.01. - 2021.11.07.
* 2021.11.08. - 2021.11.14. - Dokumentáió befejezése
* 2021.11.15. - 2021.11.21. - Project fejlesztése
* 2021.11.22. - 2021.11.28.
* 2021.11.29. - 2021.12.05. - Project befejezése

## 6. Fizikai környezet:
A játékot Visual Studio Code, valamint PyCharm fejlesztőeszközök segítségével fogjuk fejleszteni. A fejlesztés során alkalmazni fogjuk a Kivy, a Tkinter librarykat pythonhoz, valamint használni fogunk MySQL adatbázist is az eredmények eltárolása érdekében. A játék PC platformon lesz elérhető.

## 7. Absztrakt domain modell:
A programunkban az MVC programtervezési mintát követjük. Ez a minta három részből áll: Modell, Nézet, és Vezérlő.
A modell valósítja meg az üzleti logikát.
A nézet felel a felhaszálói felület megjelenítéséért. Itt jelenik meg a felhasználónak szánt adatok.
A vezérlő egy kapcsoló elem. Fogadja a felhasználói utasításokat és továbbítja azt a modell réteg felé, valamit a modell adatait a nézet felé.

##  Use casek: 

# Regisztrációs menü

![asd1](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/247068458_565058974568987_706624926524511276_n.png)


* Az alkalmazás indítása után a felhasználóknak regisztrálni kell, vagy ha már ezt megtették, akkor bejelentkezni
* A regisztrációs menüben szerepel majd login és register funkció is
* Az itt bevitt adatok egy adatbázisban tárolódnak
* A regisztrációhoz, usernam, password és email rubrikákat kell kitölteni
* A **Register** gomb lenyomása után, a beírt adatokat ellenőrzi a rendszer, ha ezek megfelelnek (emailben kukacosság, megfelelő jelszó, nem foglalt felhasználó) létrehozza az új felhasználót
* A **Login** gomb lenyomásával pedig a beírt adatok alapján beléphet a már regisztrált felhasználó
* A **Play** gomb megnyomásával, bekerülünk a játék főmenüjébe

# Főmenü

![asd1](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/menu.jpg)


* **Character** gombra kattintva kiválaszthatjuk a játékbeli karakterünket, itt több lehetőségből választhatnak a játékosok
* **Play** gombot megnyomva a játékos elkezdheti a játékot
* **Credits** gombot megnyomva a játékos megtekintheti a készítők listáját
* **TOP list** gombot megnyomva  a játékos megtekintheti az aktuális toplistát
* **Exit** gombot megnyomva a játékos kilép az alkalmazásból
* **Controls** gombot megnyomva a játékos megtekintheti azt, hogy miként lehet a karakterét irányítani a játékban
* **Legend** gombra kattintva a játékos megnyithat egy jelmagyarázatot amiben el vannak magyarázva a játék alapvetői elemei és a pályán megjelenő objektumok 

# Játékban

![asd1](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/gamescreen.jpg)


* W - fel
* S - le
* A - balra
* D - jobbra
* Space - ugrás
* Bal egérgomb - lövés (fegyverrel)
* ESC - megszakítás

## 8. Tesztterv:
### 8.1 Fő részek:
* 8.1.1 teszt végrehajtása
* 8.1.2 észrevételek dokumentálása
* 8.1.3 teszt dokumentáció archiválása

### 8.2 A tesztelést manuálisan kell végrehajtani. A teszt akkor sikeres, ha a program minden komponensét átnézve (ebben értendő az ellenféllel való harc, a saját karakter mozgatása, regisztrálás, belépés) rendben működik és nem kapunk hibaüzentet vagy programleállást.

### 8.3 A manuális tesztelés során egy tesztjegyzőkönyvet kell készíteni amiben dokumentálva van a tesztelt funkció annak elvárt viselkedése, a funkció által adott viselkedés és az, hogy ez sikeres/sikertelen.


## 9. Telepítési terv:
* 9.1 A program futtatásához python-ra van szükség amit a https://www.python.org/downloads/ weboldalról lehet telepíteni. A verziószámának 3.0+ - nak kell lennie.
* 9.2 Szükség van még a nyílt forráskódú kivy programozói könyvtárra, amit erről a weboldalról lehet letölteni és telepíteni: https://kivy.org/doc/stable/gettingstarted/installation.html.
* 9.3 MySQL adatbázis kezelő rendszerre van szükség: (<https://www.mysql.com/>)
* 9.4 Programozói környezetre is szükség van, ajánlott : Visual Studio (<https://visualstudio.microsoft.com/>) vagy Pycharm (<https://www.jetbrains.com/pycharm/>)

## Fogalom szótár:
* Visual Studio Code - A Visual Studio Code egy ingyenes, nyílt forráskódú kódszerkesztő, melyet a Microsoft fejleszt Windows, Linux és OS X operációs rendszerekhez.
* PyCharm - A PyCharm egy integrált fejlesztői környezet, amelyet a számítógépes programozásban használnak, kifejezetten a Python nyelv számára.
* MySQL - A MySQL egy többfelhasználós, többszálú, SQL-alapú relációs adatbázis-kezelő szerver.
* regisztrálás - beíratás, beiratkozás, bejegyezés, bejelentés, esetünkben a felhasználók közé
* bejelentkezés - a rendszerbe
* tesztelés - A szoftvertesztelés a szoftverminőség-biztosítás és így a szoftverfejlesztés részét képezi. A tesztelés egy rendszer vagy program kontrollált körülmények melletti futtatása, és az eredmények kiértékelése. A hagyományos megközelítés szerint a tesztelés célja az, hogy a fejlesztés során létrejövő hibákat minél korábban felfedezze, és ezzel csökkentse azok kijavításának költségeit.
* kivy -  Kivy egy ingyenes és nyílt forráskódú Python-keretrendszer mobilalkalmazások és más, természetes felhasználói felülettel rendelkező multitouch alkalmazásszoftverek fejlesztésére.
* python - A Python egy általános célú, nagyon magas szintű programozási nyelv.
* archiválás - adat eltárolása, irattárba helyezés

