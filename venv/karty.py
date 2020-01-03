class karta_pomieszczen():
    def __init__(self, nazwa):
        self.nazwa = nazwa
    id = 0
    punkty = {1: 0, 2: 0, 3: 0}  # klucze to odpowiednio ilość kart obok siebie
    miejsce = [0]  # na którym piętrze może być


class karta_aneks():
    def __init__(self, nazwa):
        self.nazwa = nazwa

    id = 0
    punkty = {1: 0, 2: 0}
    miejsce = [0]
    sasiad = [0]


class karta_dachu():
    def __init__(self, nazwa):
        self.nazwa = nazwa

    id = 0
    okno = False  # jeśli TRUE to dodatkowy punkt


class karta_wyposazenia():
    def __init__(self, nazwa):
        self.nazwa = nazwa

    id = 0
    punkty = 0
    miejsce = [0]  # w ktorym pomieszczeniu moze byc


biblioteka = karta_pomieszczen(1)
biblioteka.punkty[1] = 2
biblioteka.miejsce = [1, 2]
biblioteka.id = 1

gabinet = karta_pomieszczen(2)
gabinet.miejsce = [1, 2]
gabinet.punkty[1] = 2
gabinet.id = 2

garaz1 = karta_pomieszczen(3)
garaz1.miejsce = [3]
garaz1.punkty[1] = 0
garaz1.punkty[2] = 4
garaz1.id = 3

garaz2 = karta_pomieszczen(3)
garaz2.miejsce = [3]
garaz2.punkty[1] = 0
garaz2.punkty[2] = 4
garaz2.id = 4

garaz3 = karta_pomieszczen(3)
garaz3.miejsce = [3]
garaz3.punkty[1] = 0
garaz3.punkty[2] = 4
garaz3.id = 5

garaz4 = karta_pomieszczen(3)
garaz4.miejsce = [3]
garaz4.punkty[1] = 0
garaz4.punkty[2] = 4
garaz4.id = 6

garaz5 = karta_pomieszczen(3)
garaz5.miejsce = [3]
garaz5.punkty[1] = 0
garaz5.punkty[2] = 4
garaz5.id = 7

garaz6 = karta_pomieszczen(3)
garaz6.miejsce = [3]
garaz6.punkty[1] = 0
garaz6.punkty[2] = 4
garaz6.id = 8

sypialnia1 = karta_pomieszczen(4)
sypialnia1.punkty[1] = 1
sypialnia1.punkty[2] = 4
sypialnia1.miejsce = [1, 2]
sypialnia1.id = 9

sypialnia2 = karta_pomieszczen(4)
sypialnia2.punkty[1] = 1
sypialnia2.punkty[2] = 4
sypialnia2.miejsce = [1, 2]
sypialnia2.id = 10

sypialnia3 = karta_pomieszczen(4)
sypialnia3.punkty[1] = 1
sypialnia3.punkty[2] = 4
sypialnia3.miejsce = [1, 2]
sypialnia3.id = 11

sypialnia4 = karta_pomieszczen(4)
sypialnia4.punkty[1] = 1
sypialnia4.punkty[2] = 4
sypialnia4.miejsce = [1, 2]
sypialnia4.id = 12

sypialnia5 = karta_pomieszczen(4)
sypialnia5.punkty[1] = 1
sypialnia5.punkty[2] = 4
sypialnia5.miejsce = [1, 2]
sypialnia5.id = 13

sypialnia6 = karta_pomieszczen(4)
sypialnia6.punkty[1] = 1
sypialnia6.punkty[2] = 4
sypialnia6.miejsce = [1, 2]
sypialnia6.id = 14

sypialnia7 = karta_pomieszczen(4)
sypialnia7.punkty[1] = 1
sypialnia7.punkty[2] = 4
sypialnia7.miejsce = [1, 2]
sypialnia7.id = 15

sypialnia8 = karta_pomieszczen(4)
sypialnia8.punkty[1] = 1
sypialnia8.punkty[2] = 4
sypialnia8.miejsce = [1, 2]
sypialnia8.id = 16

kuchnia1 = karta_pomieszczen(5)
kuchnia1.punkty[1] = 1
kuchnia1.punkty[2] = 6
kuchnia1.miejsce = [1, 2]
kuchnia1.id = 17

kuchnia2 = karta_pomieszczen(5)
kuchnia2.punkty[1] = 1
kuchnia2.punkty[2] = 6
kuchnia2.miejsce = [1, 2]
kuchnia2.id = 18

kuchnia3 = karta_pomieszczen(5)
kuchnia3.punkty[1] = 1
kuchnia3.punkty[2] = 6
kuchnia3.miejsce = [1, 2]
kuchnia3.id = 19

kuchnia4 = karta_pomieszczen(5)
kuchnia4.punkty[1] = 1
kuchnia4.punkty[2] = 6
kuchnia4.miejsce = [1, 2]
kuchnia4.id = 20

kuchnia5 = karta_pomieszczen(5)
kuchnia5.punkty[1] = 1
kuchnia5.punkty[2] = 6
kuchnia5.miejsce = [1, 2]
kuchnia5.id = 21

kuchnia6 = karta_pomieszczen(5)
kuchnia6.punkty[1] = 1
kuchnia6.punkty[2] = 6
kuchnia6.miejsce = [1, 2]
kuchnia6.id = 22

kuchnia7 = karta_pomieszczen(5)
kuchnia7.punkty[1] = 1
kuchnia7.punkty[2] = 6
kuchnia7.miejsce = [1, 2]
kuchnia7.id = 23

kuchnia8 = karta_pomieszczen(5)
kuchnia8.punkty[1] = 1
kuchnia8.punkty[2] = 6
kuchnia8.miejsce = [1, 2]
kuchnia8.id = 24

lazienka1 = karta_pomieszczen(6)
lazienka1.punkty[1] = 1
lazienka1.miejsce = [1, 2]
lazienka1.id = 25

lazienka2 = karta_pomieszczen(6)
lazienka2.punkty[1] = 1
lazienka2.miejsce = [1, 2]
lazienka2.id = 26

lazienka3 = karta_pomieszczen(6)
lazienka3.punkty[1] = 1
lazienka3.miejsce = [1, 2]
lazienka3.id = 27

lazienka4 = karta_pomieszczen(6)
lazienka4.punkty[1] = 1
lazienka4.miejsce = [1, 2]
lazienka4.id = 28

lazienka5 = karta_pomieszczen(6)
lazienka5.punkty[1] = 1
lazienka5.miejsce = [1, 2]
lazienka5.id = 29

lazienka6 = karta_pomieszczen(6)
lazienka6.punkty[1] = 1
lazienka6.miejsce = [1, 2]
lazienka6.id = 30

lazienka7 = karta_pomieszczen(6)
lazienka7.punkty[1] = 1
lazienka7.miejsce = [1, 2]
lazienka7.id = 31

lazienka8 = karta_pomieszczen(6)
lazienka8.punkty[1] = 1
lazienka8.miejsce = [1, 2]
lazienka8.id = 32

PiwniczkaNaWino = karta_pomieszczen(7)
PiwniczkaNaWino.miejsce = [3]
PiwniczkaNaWino.punkty[1] = 1
PiwniczkaNaWino.id = 33

PokojDzieciecy1 = karta_pomieszczen(8)
PokojDzieciecy1.miejsce = [1, 2]
PokojDzieciecy1.punkty[1] = 2
PokojDzieciecy1.punkty[2] = 6
PokojDzieciecy1.id = 34

PokojDzieciecy2 = karta_pomieszczen(8)
PokojDzieciecy2.miejsce = [1, 2]
PokojDzieciecy2.punkty[1] = 2
PokojDzieciecy2.punkty[2] = 6
PokojDzieciecy2.id = 35

PokojDzieciecy3 = karta_pomieszczen(8)
PokojDzieciecy3.miejsce = [1, 2]
PokojDzieciecy3.punkty[1] = 2
PokojDzieciecy3.punkty[2] = 6
PokojDzieciecy3.id = 36

PokojDzieciecy4 = karta_pomieszczen(8)
PokojDzieciecy4.miejsce = [1, 2]
PokojDzieciecy4.punkty[1] = 2
PokojDzieciecy4.punkty[2] = 6
PokojDzieciecy4.id = 37

PokojDzieciecy5 = karta_pomieszczen(8)
PokojDzieciecy5.miejsce = [1, 2]
PokojDzieciecy5.punkty[1] = 2
PokojDzieciecy5.punkty[2] = 6
PokojDzieciecy5.id = 38

PokojDzieciecy6 = karta_pomieszczen(8)
PokojDzieciecy6.miejsce = [1, 2]
PokojDzieciecy6.punkty[1] = 2
PokojDzieciecy6.punkty[2] = 6
PokojDzieciecy6.id = 39

PokojDzieciecy7 = karta_pomieszczen(8)
PokojDzieciecy7.miejsce = [1, 2]
PokojDzieciecy7.punkty[1] = 2
PokojDzieciecy7.punkty[2] = 6
PokojDzieciecy7.id = 40

PokojDzieciecy8 = karta_pomieszczen(8)
PokojDzieciecy8.miejsce = [1, 2]
PokojDzieciecy8.punkty[1] = 2
PokojDzieciecy8.punkty[2] = 6
PokojDzieciecy8.id = 41

PokojGier = karta_pomieszczen(9)
PokojGier.miejsce = [1, 2]
PokojGier.punkty[1] = 2
PokojGier.id = 42

pralnia = karta_pomieszczen(10)
pralnia.punkty[1] = 1
pralnia.miejsce = [3]
pralnia.id = 43

salon1 = karta_pomieszczen(11)
salon1.punkty[1] = 1
salon1.punkty[2] = 4
salon1.punkty[3] = 9
salon1.miejsce = [1, 2]
salon1.id = 44

salon2 = karta_pomieszczen(11)
salon2.punkty[1] = 1
salon2.punkty[2] = 4
salon2.punkty[3] = 9
salon2.miejsce = [1, 2]
salon2.id = 45

salon3 = karta_pomieszczen(11)
salon3.punkty[1] = 1
salon3.punkty[2] = 4
salon3.punkty[3] = 9
salon3.miejsce = [1, 2]
salon3.id = 46

salon4 = karta_pomieszczen(11)
salon4.punkty[1] = 1
salon4.punkty[2] = 4
salon4.punkty[3] = 9
salon4.miejsce = [1, 2]
salon4.id = 47

salon5 = karta_pomieszczen(11)
salon5.punkty[1] = 1
salon5.punkty[2] = 4
salon5.punkty[3] = 9
salon5.miejsce = [1, 2]
salon5.id = 48

salon6 = karta_pomieszczen(11)
salon6.punkty[1] = 1
salon6.punkty[2] = 4
salon6.punkty[3] = 9
salon6.miejsce = [1, 2]
salon6.id = 49

salon7 = karta_pomieszczen(11)
salon7.punkty[1] = 1
salon7.punkty[2] = 4
salon7.punkty[3] = 9
salon7.miejsce = [1, 2]
salon7.id = 50

salon8 = karta_pomieszczen(11)
salon8.punkty[1] = 1
salon8.punkty[2] = 4
salon8.punkty[3] = 9
salon8.miejsce = [1, 2]
salon8.id = 51

salon9 = karta_pomieszczen(11)
salon9.punkty[1] = 1
salon9.punkty[2] = 4
salon9.punkty[3] = 9
salon9.miejsce = [1, 2]
salon9.id = 52

salon10 = karta_pomieszczen(11)
salon10.punkty[1] = 1
salon10.punkty[2] = 4
salon10.punkty[3] = 9
salon10.miejsce = [1, 2]
salon10.id = 53

salon11 = karta_pomieszczen(11)
salon11.punkty[1] = 1
salon11.punkty[2] = 4
salon11.punkty[3] = 9
salon11.miejsce = [1, 2]
salon11.id = 54

salon12 = karta_pomieszczen(11)
salon12.punkty[1] = 1
salon12.punkty[2] = 4
salon12.punkty[3] = 9
salon12.miejsce = [1, 2]
salon12.id = 55

skladzik = karta_pomieszczen(12)
skladzik.punkty[1] = 1
skladzik.miejsce = [3]
skladzik.id = 56

warsztat = karta_pomieszczen(13)
warsztat.punkty[1] = 1
warsztat.miejsce = [3]
warsztat.id = 57

PustyPokoj = karta_pomieszczen(17)
PustyPokoj.miejsce = [1, 2, 3]
PustyPokoj.id = 58

garderoba = karta_aneks(14)
garderoba.miejsce = [1, 2]
garderoba.punkty[1] = 1
garderoba.punkty[2] = 3
garderoba.sasiad = [4]
garderoba.id = 59

sauna = karta_aneks(15)
sauna.miejsce = [1, 2]
sauna.punkty[1] = 1
sauna.punkty[2] = 3
sauna.sasiad = [6]
sauna.id = 60

spizarnia = karta_aneks(16)
spizarnia.miejsce = [1, 2]
spizarnia.punkty[1] = 1
spizarnia.punkty[2] = 3
spizarnia.sasiad = [5]
spizarnia.id = 61

czerwony1 = karta_dachu(100)
czerwony1.id = 1

czerwony2 = karta_dachu(100)
czerwony2.id = 2

czerwony3 = karta_dachu(100)
czerwony3.id = 3

czerwony4 = karta_dachu(100)
czerwony4.id = 4

czerwony5 = karta_dachu(100)
czerwony5.id = 5

czerwony6 = karta_dachu(100)
czerwony6.id = 6

czerwonyOkno = karta_dachu(101)
czerwonyOkno.okno = True
czerwonyOkno.id = 7

brazowy1 = karta_dachu(200)
brazowy1.id = 8

brazowy2 = karta_dachu(200)
brazowy2.id = 9

brazowy3 = karta_dachu(200)
brazowy3.id = 10

brazowy4 = karta_dachu(200)
brazowy4.id = 11

brazowy5 = karta_dachu(200)
brazowy5.id = 12

brazowy6 = karta_dachu(200)
brazowy6.id = 13

brazowyOkno = karta_dachu(201)
brazowyOkno.okno = True
brazowyOkno.id = 14

fioletowy1 = karta_dachu(300)
fioletowy1.id = 15

fioletowy2 = karta_dachu(300)
fioletowy2.id = 16

fioletowy3 = karta_dachu(300)
fioletowy3.id = 17

fioletowy4 = karta_dachu(300)
fioletowy4.id = 18

fioletowy5 = karta_dachu(300)
fioletowy5.id = 19

fioletowy6 = karta_dachu(300)
fioletowy6.id = 20

fioletowyOkno = karta_dachu(301)
fioletowyOkno.okno = True
fioletowyOkno.id = 21

pomaranczowy1 = karta_dachu(400)
pomaranczowy1.id = 22

pomaranczowy2 = karta_dachu(400)
pomaranczowy2.id = 23

pomaranczowy3 = karta_dachu(400)
pomaranczowy3.id = 24

pomaranczowy4 = karta_dachu(400)
pomaranczowy4.id = 25

pomaranczowy5 = karta_dachu(400)
pomaranczowy5.id = 26

pomaranczowy6 = karta_dachu(400)
pomaranczowy6.id = 27

pomaranczowyOkno = karta_dachu(401)
pomaranczowyOkno.okno = True
pomaranczowyOkno.id = 28

zielony1 = karta_dachu(500)
zielony1.id = 29

zielony2 = karta_dachu(500)
zielony2.id = 30

zielony3 = karta_dachu(500)
zielony3.id = 31

zielony4 = karta_dachu(500)
zielony4.id = 32

zielonyOkno = karta_dachu(501)
zielonyOkno.okno = True
zielonyOkno.id = 33

czarny1 = karta_dachu(600)
czarny1.id = 34

czarny2 = karta_dachu(600)
czarny2.id = 35

czarny3 = karta_dachu(600)
czarny3.id = 36

czarny4 = karta_dachu(600)
czarny4.id = 37

czarnyOkno = karta_dachu(601)
czarnyOkno.okno = True
czarnyOkno.id = 38

DomekDlaKota = karta_wyposazenia(20)
DomekDlaKota.miejsce = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
DomekDlaKota.punkty = 1
DomekDlaKota.id = 39

DomekDlaPtakow = karta_wyposazenia(21)
DomekDlaPtakow.miejsce = [2121]
DomekDlaPtakow.punkty = 1
DomekDlaPtakow.id = 40

DomekNaDrzewie = karta_wyposazenia(22)
DomekNaDrzewie.miejsce = [2121]
DomekNaDrzewie.punkty = 1
DomekNaDrzewie.id = 41

MaszynaDoLodow = karta_wyposazenia(23)
MaszynaDoLodow.miejsce = [5]
MaszynaDoLodow.punkty = 2
MaszynaDoLodow.id = 42

jacuzzi = karta_wyposazenia(24)
jacuzzi.miejsce = [6]
jacuzzi.punkty = 2
jacuzzi.id = 43

Wanna = karta_wyposazenia(25)
Wanna.miejsce = [6]
Wanna.punkty = 2
Wanna.id = 44

fortepian = karta_wyposazenia(26)
fortepian.miejsce = [11]
fortepian.punkty = 3
fortepian.id = 45

obrazy = karta_wyposazenia(27)
obrazy.miejsce = [11]
obrazy.punkty = 2
obrazy.id = 46

lozko = karta_wyposazenia(28)
lozko.miejsce = [4]
lozko.punkty = 2
lozko.id = 47

regaly = karta_wyposazenia(29)
regaly.miejsce = [3, 7, 10, 12, 13]
regaly.punkty = 1
regaly.id = 48