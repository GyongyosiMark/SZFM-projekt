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

![asd](https://github.com/Kaiusz/SZFM-projekt/blob/main/Dokumentacio/img/kepernyo_terv.PNG)

## 7. Forgatókönyvek.
<p>Az első futtatásnál regisztrálni kell és továbbiakban a regisztrált felhasználónévvel és jelszóval lehet bejelentkezni.</p>
A futási időben az figyelhető meg, hogy egy ablakban megjelenik egy saját karakter amit a W-A-S-D gombokkal lehet irányítani.
A játékban a lényeg, hogy minnél több pontot gyűjtve és minnél gyorsabban vigyük végig a pályát megölve az ellenfeleket és felvéve az érméket. Az érméket úgy lehet felvenni, ha belemegyünk.
Vannak a pályán ellenfelek, amikkel meg lehet küzdeni és egy fegyverrel, ami lehet pisztoly, gépfegyver vagy csapdákat tudunk letenni amibe az ellenfelek belesétálhatnak azonban ez csak véges számú és ezáltal megölni őket. Egy ellenfél megölése esetén pontokat kapunk ami hozzáadódik a számlálóhoz és a végén kapott pontoszámhoz.
A saját karakterünknek alapértelmezetten kettő élete van, amit ha elveszít akkor "Game Over" feliratot kap és megmutatja az eddigiekben elért pontszámot. Viszont a futás alatt van lehetőség több élet gyűjtésére, ami hozzáadódik a eddigi életeihez. Az életeket úgy lehet elveszíteni, ha nekimegyünk egy ellenfélnek vagy beleesünk valamilyen csapdába, azonban a futás automatikusan visszadob vagy a pálya elejére vagy az utolsó mentési pontra, ha eljutottunk egy pálya olyan részére ahol már begyűjthettünk egy mentési pontot, ha leesünk a pályáról.
A pontok a felső sarokban jelennek meg és folyamatosan frissülnek, ha egy ellenfelet ölünk meg vagy egy érmét veszünk fel.
A pontokat a program eltárolja és a legközelebbi futáskor visszanézhető, hogy ki milyen felhasználónévvel érte el a legmagasabb pontszámot és ezt a pontszámot milyen gyorsan sikerült elérnie. Ezt egy három oszlopos táblázatban mutatja, ahol az első oszlop megjeleníti a felhasználó nevét a második oszlop megjeleníti a a felhasználónak elért pontszámát és a harmadik oszlopban megjelenik az idő, ami alatt sikerült teljesítenie a pályát.
Ezt a funkciót egy High Score menüpontban érhetjük el, amiben egymás alatt megjelenik a három legmagasabb pontszám és azoknak a felhasználónak a neve, aki elérte azt a pontszámot.


## 8. Funkció – követelmény megfeleltetés.
* 8.1 A program futtatásához Python 3-ra van szükségünk
* 8.2 A futtatáshoz Kivy programzói könyvtárra van szükségünk
* 8.3 MySQL adatbázis kezelő rendszerre van szükség

## 9. Fogalomszótár:
* 9.1 Kivy - A Kivy egy nyílt forráskódú Python programozói könyvtár, gyors alkalmazásfejlesztéshez, ami újszerű felhasználói felületet használ, mint a többérintéses alkalmazások. A Kivy program fut Linuxon, Windowson, macOS-en, Androidon, iOS-en, és Raspberry Pi-n. Ugyanaz a kód futhat minden platformon.
* 9.2 Python - A Python egy könnyen tanulható, de hatékony programozási nyelv. Magasszintű adatstruktúrái, az objektum-orientáltság egyszerű megközelítése, elegáns szintaxisa, dinamikus típusossága és interpreteres mivolta ideális script-nyelvvé teszi.
* 9.3 MySQL - A MySQL egy többfelhasználós, többszálú, SQL-alapú relációs adatbázis-kezelő szerver.
