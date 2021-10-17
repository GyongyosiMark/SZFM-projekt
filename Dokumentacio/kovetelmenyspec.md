# Követelmény Specifikáció

## 1. Jelenlegi helyzet leírása:
A True Gamer gaming tábor egy felejthetetlen élményt nyújt mindenkinek, aki szívesen tölti az idejét videójátékokozással, vagy éppen most szeretne megismerkedni a videójátékok világával.
A résztvevők egy héten keresztül fejleszthetik tudásukat a táborvezetők segítségével. Az utolsó napon, a különböző játékokban a legjobban teljesítők értékes jutalmakat kapnak a teljesítményükért.
A tábor egyik különlegessége az, hogy itt nem csak a már jól ismert játékokban mérhetik össze a tudásukat a résztvevők, hanem egy kifejezetten erre az alkalomra fejlesztett játékban is kipróbálhatják magukat. 

## 2. Vágyálomrendszer leírása:
Mivel a True Gamer gaming tábor népszerűsége egyre csak nő, az idei évben szeretné meglepni a táborozókat egy saját kis játékkal, amely hozzájárul az egyéni fejlődéshez is, valamint közelebb hozza a táborozókat, ezáltal jobb élményt nyújtva mind a táborozóknak, mind a személyzetnek. A játéknak több célja is lenne. A főbb célok között van a szórakoztatás, a fejlődés, de egy verseny is fog indulni a játékkal, amin a legtöbb pontszámot elért játékosok nyereményeket is nyerhetnek.
Tehát a táborban résztvevők, valamint a személyzet minden tagjának szeretnénk egy 2D-s játékot biztosítani. A játéknak az lenne a lényege, hogy az adott játékosnak végig kell mennie az aktuális pályán vagy pályákon, felvéve minnél több érmét, majd ezután eljutni a célba, hogy átléphessen a következő pályára. A különböző pályákon különböző pozíciókban, más-más csapdák legyenek elhelyezve, akár különböző méretben, a pályák jól elkülöníthetőek legyenek. Mindezekmellett valami kompetitivitást is bele kell raknunk a játékba, ugyanis versenyt tervezünk szervezni a játékkal kapcsolatban. Arra gondoltunk, hogy ennek megoldására egy pontrendszer lenne a legalkalmasabb. Minden egyes felvett érméért a játékos pontot kap, minden egyes csapdába sétálásért (halálért) a játékos pontot veszít, valamint minél gyorsabban teljesít egy játékos egy pályát, annál több pontot kap a végén. A játékos továbbá gyüjthet még fegyvereket, plusz életet, páncélt vagy különböző erősítéseket. Mindezek mellett, a pályán el lesznek rejtve bónusz ládák is, illetve kulcsok amik a továbbjutáshoz kellennek, ezzel egy kis logikát viszünk a játékba. Egy stratégia elem lehetne az, hogy az ellenfelek számára csapdákat helyezünk le. A legtöbb pontot szerzett játékosok egy TOP 3-as listában lesznek, ez a lista is a játékban tekinthető meg, benne a játékos nevével és az elért pontszámmal. Ehhez az szükséges, hogy a játék végén, ha a játékos bekerült a legjobb 3 helyezett közé, akkor megadhassa a nevét és ez legyen elmentve egy adatbázisba. A menüben legyen egy gomb is, amivel törölhető az adatbázis tartalma, ugyanis a különböző korosztályok külön fognak versenyezni, ezért minden korosztály versenyének kezdete előtt ki kell üríteni az eddigi eredményeket. A menüben a játékosok több karakter közül is választhassanak. A játéknak esztétitikusnak kell lennie, háttér hangoknak és effekteknek is kell szerepelni. A játéknak egyszerű története is legyen. 

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
