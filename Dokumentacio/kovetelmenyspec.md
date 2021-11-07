# Követelmény Specifikáció

## 1. Jelenlegi helyzet leírása:
A True Gamer gaming tábor egy felejthetetlen élményt nyújt mindenkinek, aki szívesen tölti az idejét videójátékokozással, vagy éppen most szeretne megismerkedni a videójátékok világával. A résztvevők egy héten keresztül fejleszthetik tudásukat a táborvezetőink segítségével.
A táborozókat az első napon két csoportba lesznek osztva tudásuk szerint. Az első csoportba fognak tartozni azok a játékosok, akik még csak most csöppennek bele a játékok világába, vagy csak nagyon kevés tapasztalattal rendelkeznek. Ők a játékokat az alap szinttől sajátítják el, kezdve az irányítással, és az alapvető játékmechanika megismerésével.
A második csoporba kerülnek azok, akik már némi tapasztalattal rendelkeznek a játékok területén. Velük nehány bemelegítő kör után elkezdünk pár magasabb szintű praktikát is kipróbálni, valamint nagyobb gyakorlottságot igénylő takitákak átvenni.  
Az utolsó napon, a különböző játékokban a legjobban teljesítők értékes jutalmakat kapnak a teljesítményükért.
A tábor egyik különlegessége az, hogy itt nem csak a már jól ismert játékokban mérhetik össze a tudásukat a résztvevők, hanem egy kifejezetten erre az alkalomra fejlesztett játékban is kipróbálhatják magukat. Ezt főként a kezdő csoport számára fejlesztettük alap tudásuk könnyebb megszerzése érdekében. Segít a játék a billentyűzeten való irányítás gyakorlásában, az ellenfelekkel és fegyverekkel való bánásmód megismerésében valamint, mivel logikai elemeket is tartalmaz, ezért a játéklogikai késséget is fejleszti. A játékmechanika a szokásos platformer játékokat követi, ezáltal a játékban szerzett tapasztalatok hasznosak lesznek más játékok játszása közben is. 

## 2. Vágyálomrendszer leírása:
<p>Mivel a True Gamer gaming tábor népszerűsége egyre csak nő, az idei évben szeretné meglepni a táborozókat egy saját kis játékkal, amely hozzájárul az egyéni fejlődéshez is,
  valamint közelebb hozza a táborozókat, ezáltal jobb élményt nyújtva mind a táborozóknak, mind a személyzetnek.</p> 
<p>A játéknak több célja is lenne. A főbb célok között van a szórakoztatás, a fejlődés, de egy verseny is fog indulni a játékkal, amin a legtöbb pontszámot elért játékosok 
  nyereményeket is nyerhetnek. Tehát a táborban résztvevők, valamint a személyzet minden tagjának szeretnénk egy 2D-s játékot biztosítani.</p> 
  <p>A játéknak az lenne a lényege, hogy az adott játékosnak végig kell mennie az aktuális pályán vagy pályákon, felvéve minnél több érmét, majd ezután eljutni a célba, hogy
  átléphessen a következő pályára. </p> 
  <p>A különböző pályákon különböző pozíciókban, más-más csapdák legyenek elhelyezve, akár különböző méretben, a pályák jól elkülöníthetőek legyenek.</p>
  <p>Mindezekmellett valami kompetitivitást is bele kell raknunk a játékba, ugyanis versenyt tervezünk szervezni a játékkal kapcsolatban. Arra gondoltunk, hogy ennek megoldására
  egy pontrendszer lenne a legalkalmasabb. Minden egyes felvett érméért a játékos pontot kap, minden egyes csapdába sétálásért (halálért) a játékos pontot veszít, valamint minél 
  gyorsabban teljesít egy játékos egy pályát, annál több pontot kap a végén. </p>
  <p>A játékos továbbá gyüjthet még fegyvereket, plusz életet, páncélt vagy különböző erősítéseket. Mindezek mellett, a pályán el lesznek rejtve bónusz ládák is, illetve kulcsok
  amik a továbbjutáshoz kellennek, ezzel egy kis logikát viszünk a játékba. Egy stratégia elem lehetne az, hogy az ellenfelek számára csapdákat helyezünk le. 
  <p>A legtöbb pontot szerzett játékosok egy TOP 3-as listában lesznek, ez a lista is a játékban tekinthető meg, benne a játékos nevével és az elért pontszámmal. </p>
  <p>Ehhez az szükséges, hogy a játék végén, ha a játékos bekerült a legjobb 3 helyezett közé, akkor megadhassa a nevét és ez legyen elmentve egy adatbázisba. </p>
  <p>A menüben legyen egy gomb is, amivel törölhető az adatbázis tartalma, ugyanis a különböző korosztályok külön fognak versenyezni, ezért minden korosztály versenyének kezdete
  előtt ki kell üríteni az eddigi eredményeket.</p>
  <p> A menüben a játékosok több karakter közül is választhassanak. A játéknak esztétitikusnak kell lennie, háttér hangoknak és effekteknek is kell szerepelni. A játéknak 
  egyszerű története is legyen. </p>

## 3 Jelenlegi Üzleti Folyamatok Modellje
### 3.1 Regisztráció
* 3.1.1 Táborba regisztrált személyek nyilvántartása --> Dosszié
* 3.1.2 Visszatérő vendégek nyilvántartása --> Dosszié
* 3.1.3 Cégen belüli személyzet nyilvántartása, foglalkozásokat elkülönítve → Dosszié
* 3.1.3 Cégen belüli személyzet béreinek nyilvántartása → Dosszié
* 3.1.4 Regisztrált személyek korcsoport szerinti beosztása → Dosszié
* 3.1.5 Játék vásárlások → Dosszié
* 3.1.6 Hardver (pc, konzol) vásárlások → Dosszié
* 3.1.7 Étel mennyiség és minőség kategóriákra osztva (vegán, paleo, stb...) → Dosszié
* 3.1.8 Táborban szükséges háztartási eszközök vásárlása → Dosszié

### 3.2 Fizetés/Szolgáltatás
* 3.2.1 Egész nyaras tábor → Kassza → Készpénz/Terminál
* 3.2.2 30 napos tábor → Kassza → Készpénz/Terminál
* 3.2.3 1 hetes tábor → Kassza → Készpénz/Terminál
* 3.2.4 Sátor kölcsönzés → Kassza → Készpénz/Terminál
* 3.2.5 Fa lakóház bérlés → Kassza → Készpénz/Terminál
* 3.2.6 Coach → Kassza → Készpénz/Terminál
* 3.2.7 Menza → Kassza → Készpénz/Terminál
* 3.2.8 Cafeteria/Kávézó → Kassza → Készpénz/Terminál
* 3.2.9 Kisbolt → Kassza → Készpénz/Terminál
* 3.2.10 Személyzet kifizetése → Személyesen → Készpénz
* 3.2.11 Szabadtéri játszótér → Ingyenes
* 3.2.12 Készleteink feltöltése külön-külön mind passzív(tárgyilagos) és aktív(élelem) értelemben→ Készpénz/Terminál → Dosszié
* 3.2.13 Edzőterem használata -> ingyenes

### 3.3 Kapcsolattartás/Hirdetés
* 3.3.1 Tábor elérhetősége → Weboldal/Plakátok/Autó reklámfelület/TV reklám → Telefon / Személyes
* 3.3.2 Vendégek értesítése → Regisztrált személyek dosszié → Telefon
* 3.3.3 Személyzeti meeting → Aula → Személyesen
* 3.3.4 Panaszigény benyújtása → Személyesen
* 3.3.5 Visszajelzés a vendégtől → Vendégkönyv

## 4. Igényelt Üzleti Folyamatok Modellje

#### 4.1 Az igényelt termék egy játék, nem szükségesek komplex üzleti modellek.
#### 4.2 Néhány üzletszerű folyamat: 
* 4.2.1 Top lista
* 4.2.2 Pontok számítása
* 4.2.3 Asztali számítógépen megjeleníthető legyen
* 4.2.4 Menüsor legyen (Exit, Play)
* 4.2.5 Készítők neve szerpeljen

## 5. Követelmény lista:

* a játékban egy külön ablakban jelenjen meg
* a játékban jelenjen meg, hogy a játékos hogyan tudja irányítani a karakterét
* a játékban lehessen pontokat gyűjteni a megölt ellenfelek illetve szerzett pontok után és ezt egy számláló mutassa az egyik sarokban
* a játék felülete legyen egyszerű
* a menü legyen egyértelmű és egyszerű
* a high-score jelenjen meg a menü felületén
* a pontszámok kerüljenek eltárolásra adatbázisban

## 6. Irányított és szabad szöveges riportok szövege: 

* Milyen fő funkciókat vár el egy ilyen játéktól?
* Milyen képességeket lehetne fejleszetni a játékkal?
* Mit gondol mennyire nehéz megtanulni egy mai gyereknek egy játék kezelését?

## 7. Fogalomszótár:

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
