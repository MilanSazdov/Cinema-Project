<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Osnove programiranja - Projektni zadatak</h1>
    <h2>2023/2024</h2>
    <h3>Verzija 12.12.2023.</h3>
    <h2>Unos, izmenu i brisanje filmova i bioskopski projekcija</h2>
    <p>Zahtev da test set sadrži termine bioskopskih projekcija u sledeće dve nedelje.</p>
    <p>Potrebno je implementirati Python aplikaciju za evidentiranje prodaja karata u bioskopu.</p>
    <p>Aplikaciju mogu koristiti neregistrovani kupci, registrovani kupci, prodavci i menadžeri.</p>
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
        <li>Validnost lozinke– lozinka mora da bude duža od 6 karaktera i da sadrži bar jednu cifru.</li>
    </ul>
    <h3>Osnovni entiteti u sistemu:</h3>
    <ul>
        <li>Bioskopska projekcija</li>
        <li>Sala za projekcije</li>
        <li>Film</li>
        <li>Karta</li>
        <li>Termin bioskopske projekcije</li>
    </ul>
    <h3>Funkcionalnosti aplikacije:</h3>
    <p>Funkcionalnosti zajedničke za sve korisnike:</p>
    <ol>
        <li>Prijava na sistem.</li>
        <li>Izlazak iz aplikacije.</li>
        <li>Pregled dostupnih filmova.</li>
        <li>Pretraga filmova.</li>
        <li>Višekriterijumska pretraga filmova.</li>
        <li>Pretraga termina bioskopskih projekcija.</li>
    </ol>
    <h3>Funkcionalnosti za neregistrovanog klijenta:</h3>
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
