# Backend

1. Spletna aplikacija naj bo v Python-u, framework Bottle.
2. Spletna aplikacija naj po defaultu streže priložen card.html.
3. Spletna aplikacija naj ima endpoint, ki vrne naključni izlet do naključne atrakcije v JSON formatu, s polji, kot so definirani v `card.html`. Seznam atrakcij je na voljo v priloženi bazi zazipani v `slovenia_db.zip`. Uporabi smiselna polja, če neke informacije ni v vnosu v bazi, generiraj naključno.

# Frontend

1. Popravi frontend, da boš namesto preddefiniranih opcij za trip start, trip duration, trip price range in trip transport imel možnost izbire. Npr. za trip transport naj bo dropdown z možnostmi izbire prevoza Car, Bus ali Walking. Podobno za druga polja.
2. Dopolni frontend, da bo po kliku na gumb “Get new trip!” naredil klic na backend ter dobil nek nov random izlet in ga prikazal.
3. Dopolni frontend, da bo uporabniku po kliku na “Submit data!” prikazal izbrane opcije pri poljih izleta - recimo alert ali kar konzola.

# Splošna higiena

1. Dodaj komentarje, kjer je potrebno.
2. Uporabi konvencije glede pisanja aplikacij, recimo requirements.txt datoteko za beleženje zunanjih knjižnjic za Python in README, kjer napišeš kako pripraviš razvojno okolje ter poženeš razvito aplikacijo.

# README

Na začetku namestimo Bottle framework s python package managerjem:

```html
   pip install bottle
```


Projekt zaženemo (strežnik):

```html
   python start.py
```

Nato odpremo v brskalniku: [Links](http://localhost/:8080)
