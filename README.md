<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div align="center">
        <h1>Osnove programiranja - Projektni zadatak</h1>
        <h2>2023/2024</h2>
        <h3>Verzija 12.12.2023.</h3>
    </div>
    <h3><i>* Unos, izmenu i brisanje filmova i bioskopski projekcija</i></h3>
    <h3><i>* Zahtev da test set sadrži termine bioskopskih projekcija u sledeće dve nedelje.</i></h3>
    <hr>
    <p>Potrebno je implementirati Python aplikaciju za evidentiranje prodaja karata u bioskopu. Aplikaciju mogu koristiti neregistrovani kupci, registrovani kupci, prodavci i menadžeri.</p>
    <h3>Ulogovani kupci, prodavci i menadžeri su opisani sledećim podacima:</h3>
    <ul>
        <li>Korisničko ime (jedinstveno na nivou sistema)</li>
        <li>Lozinka</li>
        <li>Ime</li>
        <li>Prezime</li>
        <li>Uloga (numeracija - može biti: registrovan kupac, prodavac ili menadžer)</li>
    </ul>
    <h3>Prilikom registracije proveriti:</h3>
    <ul>
        <li>Jedinstvenost korisničkog imena u sistemu.</li>
        <li>Validnost lozinke – lozinka mora da bude duža od 6 karaktera i da sadrži bar jednu cifru.</li>
    </ul>
    <h3>Osnovni entiteti u sistemu je <strong>bioskopska projekcija</strong>. Projekcija je opisana sledećim podacima:</h3>
    <ul>
        <li>Šifra projekcije u obliku četvorocifrenog broja</li>
        <li>Sala u kojoj se projekcija održava (jedna od dostupnih sala)</li>
        <li>Vreme početka projekcije</li>
        <li>Vreme kraja projekcije</li>
        <li>Dani u nedelji kada se projekcija održava - niy koji može imati do 7 elemenata (ponedeljak, utorak, sreda, četvrtak, petak, subota, nedelja)</li>
        <li>Film koji se prikazuje (od dostupnih filmova)</li>
        <li>Cena karte (osnovna cena)</li>
    </ul>
    <h3>Sala za projekcije je opisana sledećim podacima:</h3>
    <ul>
        <li>Šifra sale</li>
        <li>Naziv sale (nije obavezno navesti)</li>
        <li>Broj redova (numeracija 1,2,3…)</li>
        <li>Oznakasedišta u svakom redu (numeracija A, B, C…)</li>
    </ul>
    <h3>Svaki film je opisan sledećim podacima:</h3>
    <ul>
        <li>Naziv filma</li>
        <li>Žanr(od dostupnih žanrova)</li>
        <li>Trajanje filma (u minutima)</li>
        <li>Režiser(i)</li>
        <li>Glavne uloge</li>
        <li>Zemlja porekla</li>
        <li>Godina proizvodnje</li>
        <li>Skraćeni opis filma</li>
    </ul>
    <p> Karte se prodaju za termin bioskopske projekcije (određen datumom, vremenom i salom
 u kojoj se održava).</p>
    <h3>Termin bioskopske projekcije je određen sledećim podacima:</h3>
    <ul>
        <li>Bioskopskom projekcijom</li>
        <li>Datumomodržavanja</li>
        <li>Šifrom koja se gradi od četvorocifrene oznake bioskopske projekcije spojene sa
 još 2 slova koja određuju termin bioskopske projekcije.</li>
    <p>Primer:</p>
    <p>Bioskopska projekcija: </p>
    <p>1111|A1|19:30|22:00|ponedeljak, sreda|Pulp Fiction|430.00</p>
        <br>
    <p>Termin bioskopske projekcije:</p>
        <p>1111AA|17.12.2023.-> iz šifre se vidi da je u pitanju termin projekcije gore
 navedene bioskopske projekcije</p>
    </ul>
    <p> Proveriti da li je dan održavanja u skladu sa danom u nedelji kada se projekcija održava
 (iz pripadajuće bioskopske projekcije).</p>
    <h3>Bioskopske karte se prodaju pojedinačnim kupcima. Za svaku kartu su vezani sledeći
 podaci:</h3>
    <ul>
        <li>Imeiprezime za neregistrovanog korisnika</li>
        <p>ili</p>
        <li>Korisničko ime za registrovanog korisnika</li>
        <li>Termin bioskopske projekcije</li>
        <li>Oznakasedišta (oznaka reda i kolone)</li>
        <li>Datumprodaje</li>
        <li>Podatak da li je rezervisana ili kupljena</li>
    </ul>
    <p> Za oznaku sedišta potrebno je navesti oznaku postojećeg sedišta u sali.</p>
    <p>Datum prodaje se dodaje automatski.</p>
    <p> Sve ove podatke je potrebno čuvati u datotekama. Prilikom pokretanja aplikacije,
 potrebno je učitati sve dostupne podatke iz datoteka.</p>
    <hr>
    <h3>Funkcionalnosti aplikacije:</h3>
    <p><i><u>Funkcionalnosti zajedničke za sve korisnike:</u></i></p>
    <ol>
        <li><strong>Prijava na sistem. </strong>Neprijavljeni korisnik unosi korisničko ime i lozinku dok ne
 unese ispravnu kombinaciju imena i lozinke registrovanog korisnika (bilo da je
 registrovan kupac, prodavac ili menadžer). Nakon toga, korisnik je prijavljen i
 može da izvršava aktivnosti predviđene njegovom ulogom.</li>
        <li><b>Izlazak iz aplikacije.</b></li>
        <li><b>Pregled dostupnih filmova.</b> Korisnik može da pregleda opšte informacije o
 dostupnim filmovima (naziv filma, žanr, trajanje, režisere, uloge, zemlju porekla,
 godinu proizvodnje).</li>
        <li><b>Pretraga filmova.</b> Korisnik može da pretražuje listu filmova po nazivu, žanru,
 trajanju filma (minimalno trajanje, maksimalno trajanje, navođenje granica),
 režiserima, glavnim ulogama, zemlji porekla, godini proizvodnje. Kao rezultat
 dobija listu filmova koji ispunjavaju uslove pretrage.</li>
        <li><b>Višekriterijumska pretraga filmova.</b> Korisniku se nude dostupni kriterijumi
 pretrage (pojedinačni kriterijum iz zadatka 4), čije vrednosti unosi nakon odabira.</li>
        <li><b>Pretraga termina bioskopskih projekcija.</b> Korisnik bira da li će pretraživati
 projekcije po filmovima, salama, datumu održavanja i vremenu početka i kraja.
 Kada korisnik odabere opciju i unese željene vrednosti, prikazuju se osnovni
 podaci o projekcijama (naziv filma, oznaka sale, datum održavanja, vreme
 početka i vreme kraja projekcije).</li>
    </ol>
    <h3><i><u>Funkcionalnosti za neregistrovanog klijenta:</u></i></h3>
    <p>Osim funkcionalnosti zajedničkih za sve korisnike, neregistrovanom kupcu su dostupne i sledeće opcije:</p>
    <ol>
        <li>Registracija.</li>
    </ol>
    <h3>Funkcionalnosti za sve registrovane korisnike (registrovani kupac, prodavac, menadžer):</h3>
    <ol start="7">
        <li>Odjava sa sistema.</li>
    </ol>
</body>
</html>
