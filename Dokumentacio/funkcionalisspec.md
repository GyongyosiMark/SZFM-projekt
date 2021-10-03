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
A futási időben az figyelhető meg, hogy egy ablakban megjelenik egy saját karakter amit a W-A-S-D gombokkal lehet irányítani és ezenkívül van egy ellenfél, amihez ha hozzáér a karakterünk ezt érzékeli.

## 8. Funkció – követelmény megfeleltetés.
* 8.1 A program futtatásához Python 3-ra van szügségünk
* 8.2 A futtatáshoz Kivy programzói könyvtárra van szügségünk

## 9. Fogalomszótár:
* 9.1 Kivy - A Kivy egy nyílt forráskódú Python programozói könyvtár, gyors alkalmazásfejlesztéshez, ami újszerű felhasználói felületet használ, mint a többérintéses alkalmazások. A Kivy program fut Linuxon, Windowson, macOS-en, Androidon, iOS-en, és Raspberry Pi-n. Ugyanaz a kód futhat minden platformon.
* 9.3 Python - A Python egy könnyen tanulható, de hatékony programozási nyelv. Magasszintű adatstruktúrái, az objektum-orientáltság egyszerű megközelítése, elegáns szintaxisa, dinamikus típusossága és interpreteres mivolta ideális script-nyelvvé teszi.
