# Funkcionális Specifikációk

## 1. Jelenlegi helyzet
A táborban egyenlőre nincs egy olyan játék ami a vezetők saját fejéből pattant ki.
A táborban jelenleg bérelt gépeken és konzolokon játszanak. A cégnek több nagy játékfejlesztővel 
is van kapcsolata, ezek viszont már kész játékokat szolgáltatnak nekik bérlet formájában. A vezetőknek nincs beleszólása abban, hogy a fejlesztők milyen játékokat hoznak létre.

## 2. Vágyálom rendszer leírása
A cég igazgatója szeretne egy olyen játékot, ami az ő elképezelése alapján készülne el, azért, 
hogy egyrészt egy olyat készíthessenek ami több korosztály számára is megfelelő, másrészt ennek a játéknak
oktató jellegűnek és szorakoztatónak is kellene lennie. Egy ilyen játék nagyban megdobná a tábor presztizsét,
még ha nem is küszködnek ilyen gondokkal, illetve marketing fogásként is nagyszerű.
Mivel a tábor már több éve sikeresen működik, szeretnének a mostani meghírdetett táborokba valami különlegeset vinni, ezért is gondoltak erre, hogy egy játékot készítenek.

## 3. Igényelt Üzleti Folyamatok Modellje
### 3.1 Az igényelt termék egy játék, nem szükségesek komplex üzleti modellek. ✓
### 3.2 Néhány üzletszerű folyamat: 
* 3.2.1 Top lista ✗
* 3.2.2 Pontok számítása ✗
* 3.2.3 Asztali számítógépen megjeleníthető legyen ✓
* 3.2.4 Menüsor legyen (Exit, Play) ✗
* 3.2.5 Készítők neve szerpeljen ✗

## 4. Használati leírás:
* Játékos: A játébeli karaktert tudja mozgatni fel, le, jobbra, balra a pályán. Ha a karater érintkezik a képernyőn lévő ellenféllel, akkor azt érzékeli a program.

## 5. Megfeleltetés, hogyan fedik le a használati esetek a követelményeket

* a játékban egy külön ablakban jelenjen meg ✓
* a játékban jelenjen meg, hogy a játékos hogyan tudja irányítani a karakterét ✓
* a játékban lehessen pontokat gyűjteni a megölt ellenfelek után és ezt egy számláló mutassa az egyik sarokban ✗
* a játék felülete legyen egyszerű ✓
* a menü legyen egyértelmű és egyszerű ✗
* a high-score jelenjen meg a menü felületén ✗

## 6. Képernyő tervek:
A játék elindításakor a képernyőn megjelenik a karakter amit a játékos tud irányítani, valamint egy ellenfél.

![asd1](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/kepernyo_terv.PNG)

A játék már egy kiforottab alakban, fegyver, karakter ellenfelek, pályamodell, háttér

![asd2](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/gamescreen.jpg)

Menu, amiből elérhetőek az említett funkciók

![asd3](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/menu.jpg)

Top lista, benne néhány játékos által elért pontsszámok

![asd4](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/highscore.png)

## 7. Forgatókönyvek.
<p>Az első futtatásnál regisztrálni kell és továbbiakban a regisztrált felhasználónévvel és jelszóval lehet bejelentkezni.</p>
<p>A futási időben az figyelhető meg, hogy egy ablakban megjelenik egy saját karakter amit a W-A-S-D gombokkal lehet irányítani.</p>
<p>A játékban a lényeg, hogy minnél több pontot gyűjtve és minnél gyorsabban vigyük végig a pályát megölve az ellenfeleket és felvéve az érméket. Az érméket úgy lehet felvenni,
ha belemegyünk.</p>
<p>Vannak a pályán ellenfelek, amikkel meg lehet küzdeni és egy fegyverrel, ami lehet pisztoly vagy gépfegyver illetve csapdákat tudunk letenni amibe az ellenfelek
  belesétálhatnak azonban ez csak véges számú, és ezáltal megölni őket. Egy ellenfél megölése esetén pontokat kapunk ami hozzáadódik a számlálóhoz és a végén kapott
  pontoszámhoz.</p>
<p>A saját karakterünknek alapértelmezetten kettő élete van, amit ha elveszít akkor "Game Over" feliratot kap és megmutatja az eddigiekben elért pontszámot.
  Viszont a futás alatt van lehetőség több élet gyűjtésére, ami hozzáadódik a eddigi életeihez. Az életeket úgy lehet elveszíteni, ha nekimegyünk egy ellenfélnek vagy beleesünk
  valamilyen csapdába, azonban a futás automatikusan visszadob vagy a pálya elejére vagy az utolsó mentési pontra, ha eljutottunk egy pálya olyan részére ahol már begyűjthettünk
  egy mentési pontot.</p>
<p>A pontok a felső sarokban jelennek meg és folyamatosan frissülnek, ha egy ellenfelet ölünk meg vagy egy érmét veszünk fel.</p>
<p>A pontokat a program eltárolja és a legközelebbi futáskor visszanézhető, hogy ki milyen felhasználónévvel érte el a legmagasabb pontszámot és ezt a pontszámot milyen gyorsan 
  sikerült elérnie. Ezt egy három oszlopos táblázatban mutatja, ahol az első oszlop megjeleníti a felhasználó nevét a második oszlop megjeleníti a a felhasználónak elért 
  pontszámát és a harmadik oszlopban megjelenik az idő, ami alatt sikerült teljesítenie a pályát.</p>
<p>Ezt a funkciót egy High Score menüpontban érhetjük el, amiben egymás alatt megjelenik a három legmagasabb pontszám és azoknak a felhasználónak a neve, aki elérte azt a 
  pontszámot.</p>


## 8. Funkció – követelmény megfeleltetés.
* 8.1 A program futtatásához Python 3-ra van szükségünk: (<https://www.python.org/>)
* 8.2 A futtatáshoz Kivy programzói könyvtárra van szükségünk: (<https://kivy.org/>)
* 8.3 MySQL adatbázis kezelő rendszerre van szükség: (<https://www.mysql.com/>)
* 8.4 Programozói környezetre is szükség van, ajánlott : Visual Studio (<https://visualstudio.microsoft.com/>) vagy Pycharm (<https://www.jetbrains.com/pycharm/>)


## 9. Fogalomszótár:
* 9.1 Kivy - A Kivy egy nyílt forráskódú Python programozói könyvtár, gyors alkalmazásfejlesztéshez, ami újszerű felhasználói felületet használ, mint a többérintéses alkalmazások. A Kivy program fut Linuxon, Windowson, macOS-en, Androidon, iOS-en, és Raspberry Pi-n. Ugyanaz a kód futhat minden platformon.
* 9.2 Python - A Python egy könnyen tanulható, de hatékony programozási nyelv. Magasszintű adatstruktúrái, az objektum-orientáltság egyszerű megközelítése, elegáns szintaxisa, dinamikus típusossága és interpreteres mivolta ideális script-nyelvvé teszi.
* 9.3 MySQL - A MySQL egy többfelhasználós, többszálú, SQL-alapú relációs adatbázis-kezelő szerver.
* Videójáték - A videojátékok olyan elektronikus játékszoftverek, amelyeket szórakoztatás céljából fejlesztettek ki olyan elektronikus eszközökön keresztül, mint például játéktermek, konzolok, számítógépek vagy digitális eszközök.
* Karakter - Egy figura, amit a felhasználó irányít a játék közben.
* Pálya - Az a tér, ahol a játékos a karaktert irányítja.
* Pont - Az az érték amivel egy játékos rendelkezik, ez minősíti a teljesítményét
* Bonus chest - Olyan elem a pályán ami előnyökhez juttatja a játékost
* Páncél - Ha a játékos ezzel rendelkezik, akkor kivédi az ellenfelek egy támadását
* Power Up - olyan bónusz tulajdonság amit a játékos megszerezhet (pl. gyorsaság)
* W-A-S-D - a billentyűzet azon gombjai amelyekkel a karaktert egy derékszögű koordináta rendszerben mozgathatunk. Ennek a rendszernek az origója a képernyő bal alsó sarka, a játékos spawnpointja
* spawnpoint - a játékos karakterének kezdőpontja, a játék betöltődése után
* érme - a pályadizájn egy eleme, gyűjthető elemek, hozzáadnak a játékos által elért pontszámhoz
* pisztoly - az egyik megszerezhető fegyver, bal egérgomb kattintásra egy golyót lő ki
* gépfegyver - a másik megszerezhető fegyver, a bal egérgomb nyomva tartásával sorozatosan lő
* mentési pont/checkpoint - ha a játékosnak, halála után marad még élete akkor a pálya egy kijelölt részén éled, ha ezt már elérte, egy ilyen pont elérésekor, üzenetet küldünk
* High Score - a játékos által elért legmagasabb pontszám, mely tárolódik, ebből a TOP 3 megtekinthető az alkalmazásból
* asztali számítógép - Az asztali számítógép retronim kifejezés olyan személyi számítógépet (PC) vagy munkaállomást jelent, amely a többfelhasználós számítógépeknél általában    kisebb helyen, a hordozható eszközökhöz képest viszonylag kötött helyen (például egy íróasztalon) működik.
* TOP lista - a legjobb N darab játékos listája, elért pontszám és idő szerint
