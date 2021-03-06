from flask import Flask, render_template, flash, redirect, request, url_for
from random import shuffle, randint
import karty

app = Flask(__name__)

class Gracze():
    '''Klasa gracza'''
    def __init__(self, nazwa):
        self.nazwa = nazwa
    znacznikPierwszegoGracza = False
    punkty = 0
    domek = 0
    dach = 0
    ogrodek = []

#pelna talia kart pomieszczen na poczatek gry
taliaKartPomieszczen = [karty.gabinet, karty.PokojGier, karty.biblioteka, karty.PokojDzieciecy1, karty.PokojDzieciecy2,
                        karty.PokojDzieciecy3, karty.PokojDzieciecy4, karty.PokojDzieciecy5, karty.PokojDzieciecy6,
                        karty.PokojDzieciecy7, karty.PokojDzieciecy8, karty.kuchnia1, karty.kuchnia2, karty.kuchnia3,
                        karty.kuchnia4, karty.kuchnia5, karty.kuchnia6, karty.kuchnia7, karty.kuchnia8,
                        karty.sypialnia1,
                        karty.sypialnia2, karty.sypialnia3, karty.sypialnia4, karty.sypialnia5, karty.sypialnia6,
                        karty.sypialnia7, karty.sypialnia8, karty.lazienka1, karty.lazienka2, karty.lazienka3,
                        karty.lazienka4, karty.lazienka5, karty.lazienka6, karty.lazienka7, karty.lazienka8,
                        karty.salon1,
                        karty.salon2, karty.salon3, karty.salon4, karty.salon5, karty.salon6, karty.salon7,
                        karty.salon8,
                        karty.salon9, karty.salon10, karty.salon11, karty.salon12, karty.spizarnia, karty.garderoba,
                        karty.sauna, karty.skladzik, karty.warsztat, karty.pralnia, karty.PiwniczkaNaWino, karty.garaz1,
                        karty.garaz2, karty.garaz3, karty.garaz4, karty.garaz5, karty.garaz6]

#pelna talia kart dodatkow na poczatek gry
taliaKartDodatkow = [karty.brazowyOkno, karty.brazowy1, karty.brazowy2, karty.brazowy3, karty.brazowy4, karty.brazowy5,
                     karty.brazowy6, karty.fioletowyOkno, karty.fioletowy1, karty.fioletowy2, karty.fioletowy3,
                     karty.fioletowy4, karty.fioletowy5, karty.fioletowy6, karty.pomaranczowyOkno, karty.pomaranczowy1,
                     karty.pomaranczowy2, karty.pomaranczowy3, karty.pomaranczowy4, karty.pomaranczowy5,
                     karty.pomaranczowy6,
                     karty.czerwonyOkno, karty.czerwony1, karty.czerwony2, karty.czerwony3, karty.czerwony4,
                     karty.czerwony5,
                     karty.czerwony6, karty.zielonyOkno, karty.zielony1, karty.zielony2, karty.zielony3, karty.zielony4,
                     karty.czarnyOkno, karty.czarny1, karty.czarny2, karty.czarny3, karty.czarny4, karty.DomekNaDrzewie,
                     karty.DomekDlaPtakow, karty.DomekDlaKota, karty.MaszynaDoLodow, karty.jacuzzi, karty.Wanna,
                     karty.fortepian,
                     karty.obrazy, karty.lozko, karty.regaly]
#talia kart, ktore gracz moze wybrac podczas rundy
biezacaTaliaPomieszczen = []
biezacaTaliaDodatkow = []
TaliaPomieszczenOdrzuconych = []
TaliaDodatkowOdrzuconych = []
tura = 0
licznikGracza = -1
gracz = 0
domek = 0
zmiana = [False, 5]
wyniki = []
ruch = False
pierwszyraz = True
pierwszywRundzie = True


#domki poszczegolnych graczy
Domek1 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
Domek2 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
Domek3 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
Domek4 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
Dach1 = []
Dach2 = []
Dach3 = []
Dach4 = []
Ogrod1 = []
Ogrod2 = []
Ogrod3 = []
Ogrod4 = []

#tworzenie graczy
gracz1 = Gracze('gracz1')
gracz1.dach = Dach1
gracz1.domek = Domek1
gracz1.ogrodek = Ogrod1

gracz2 = Gracze('gracz2')
gracz2.dach = Dach2
gracz2.domek = Domek2
gracz2.ogrodek = Ogrod2


gracz3 = Gracze('gracz3')
gracz3.dach = Dach3
gracz3.domek = Domek3
gracz3.ogrodek = Ogrod3

gracz4 = Gracze('gracz4')
gracz4.dach = Dach4
gracz4.domek = Domek4
gracz4.ogrodek = Ogrod4

#tworzenie druzyny
Druzyna = [gracz1, gracz2, gracz3, gracz4]


def zmianaDruzyny(Druzyna, numer):
    '''Funkcja do zmiany pierwszego gracza'''
    if numer == 1:
        zmienna = Druzyna[0]
        Druzyna[0] = Druzyna[1]
        Druzyna[1] = Druzyna[2]
        Druzyna[2] = Druzyna[3]
        Druzyna[3] = zmienna
    elif numer == 2:
        zmienna = Druzyna[0]
        zmienna2 = Druzyna[1]
        Druzyna[0] = Druzyna[2]
        Druzyna[1] = Druzyna[3]
        Druzyna[2] = zmienna
        Druzyna[3] = zmienna2
    elif numer == 3:
        zmienna = Druzyna[0]
        Druzyna[0] = Druzyna[3]
        Druzyna[3] = Druzyna[2]
        Druzyna[2] = Druzyna[1]
        Druzyna[1] = zmienna
    return Druzyna

def liczeniePunktow():
    global Druzyna
    licznik = 0
    licznikOkien = 0
    tenSamDach = False
    zOknem = False
    okno = 0
    lazienka = False
    kuchnia = False
    sypialnia = False
    licznikpetli = 0
    dwieLazienki = False
    for x in Druzyna:
        for y in x.domek:
            print('y %d' %y)
            if y == 3: #liczenie punktów w piwnicy
                if 2 in x.domek[y][3].punkty: #jesli pomieszczenie jest 2 pokojowe
                    if x.domek[y][3].nazwa == x.domek[y][4].nazwa: #sprawdzenie, czy obok jest takie samo pomieszczenie
                        x.punkty = x.punkty + x.domek[y][3].punkty[2] #jeśli tak, to gracz otrzymuje punkty za 2 pokoje
                        if x.domek[y][3].wyposazenie != 0:
                            x.punkty = x.punkty + x.domek[y][3].wyposazenie.punkty
                            print('punkt za wyposazenie')
                        print('punkty', x.punkty, 'licznik', licznik)
                    else:
                        x.punkty = x.punkty + x.domek[y][3].punkty[1] + x.domek[y][4].punkty[1] #jesli obok siebie są różne pomieszczenie, to dostaje punkty za jednopokojowe pomieszczenia
                        if x.domek[y][3].wyposazenie != 0:
                            x.punkty = x.punkty + x.domek[y][3].wyposazenie.punkty
                            print('punkt za wyposazenie')
                        if x.domek[y][4].wyposazenie != 0:
                            x.punkty = x.punkty + x.domek[y][4].wyposazenie.punkty
                            print('punkt za wyposazenie')
                        print('punkty', x.punkty, 'licznik', licznik)
                else:
                    x.punkty = x.punkty + x.domek[y][3].punkty[1] + x.domek[y][4].punkty[1] #jesli pomieszczenie jest jednopokojowe to dostaje punkty za dwa jednopokojowe pomieszczenia
                    print('punkty', x.punkty, 'licznik', licznik)
                    if x.domek[y][3].wyposazenie != 0:
                        x.punkty = x.punkty + x.domek[y][3].wyposazenie.punkty
                        print('punkt za wyposazenie')
                    if x.domek[y][4].wyposazenie != 0:
                        x.punkty = x.punkty + x.domek[y][4].wyposazenie.punkty
                        print('punkt za wyposazenie')
                print('liczenie piwnicy')
            else: #jesli piętro nie jest piwnicą
                while licznik <= 4: #przechodzenie po każdym pokoju (jest 5 na kazdym pietrze)
                    if 3 in x.domek[y][licznik].punkty: #jesli pomieszczenie moze być 3pokojowe
                        if licznik != 4: #jesli pokoj nie jest ostatni na pietrze
                            if x.domek[y][licznik+1].nazwa == x.domek[y][licznik].nazwa: # jeśli kolejny pokoj to to samo pomieszczenie
                                if licznik != 3: #jesli pokoj nie jest przedostatni
                                    if x.domek[y][licznik+2].nazwa == x.domek[y][licznik].nazwa: #jesli 3 karty pod rząd to to samo pomieszczenie
                                        x.punkty = x.punkty + x.domek[y][licznik].punkty[3]
                                        licznik = licznik + 3
                                        print('punkty', x.punkty, 'licznik', licznik)
                                    else: #jesli tylko trzeci pokoj jest inny niz poprzednie dwa
                                        x.punkty = x.punkty + x.domek[y][licznik].punkty[2]
                                        licznik = licznik + 2
                                        print('punkty', x.punkty, 'licznik', licznik)
                                else: #jesli jest przedostatni
                                    x.punkty = x.punkty + x.domek[y][licznik].punkty[2]
                                    licznik = licznik + 2
                                    print('punkty', x.punkty, 'licznik', licznik)
                            else: #jesli nie jest ostatni,ale kolejny pokoj to nie to samo pomieszczenie
                                x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                                licznik = licznik + 1
                                print('punkty', x.punkty, 'licznik', licznik)
                        else: #jesli pokoj jest na ostatni na piętrze
                            x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                            licznik = licznik + 1
                            print('punkty', x.punkty, 'licznik', licznik)
                    elif 2 in x.domek[y][licznik].punkty: #jesli pomieszczenie moze byc dwupokojowe
                        if x.domek[y][licznik].sasiad != None: #sprawdzenie, czy to aneks
                            if licznik != 4: #sprawdzenie, czy jest to ostatni pokoj
                                if x.domek[y][licznik].sasiad == x.domek[y][licznik+1].nazwa: #jesli to nie jest ostatni pokoj to sprawdzenie, czy kolejne pomieszczenie to dobry sasiad dla aneksu
                                    x.punkty = x.punkty + x.domek[y][licznik].punkty[2]
                                    licznik = licznik + 1
                                    print('punkty', x.punkty, 'licznik', licznik)
                                else: #jesli koeljny pokoj to niedobry sasiad dla aneksu
                                    if licznik != 0: #sprawdzenie, czy nie jest to pierwszy pokoj
                                        if x.domek[y][licznik].sasiad == x.domek[y][licznik-1].nazwa: #sprawdzenie, czy poprzedni pokoj to dobry sasiad
                                            x.punkty = x.punkty + x.domek[y][licznik].punkty[2]
                                            licznik = licznik + 1
                                            print('punkty', x.punkty, 'licznik', licznik)
                                        else: #jesli aneks nie ma zadnego dobrego sasiada
                                            x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                                            licznik = licznik + 1
                                            print('punkty', x.punkty, 'licznik', licznik)
                                    else: #jesli jest to pierwszy pokoj, to aneks ma tylko jednego sasiada, ktorego juz sprawdzilismy
                                        x.punkty = x.domek[y][licznik].punkty[1]
                                        licznik = licznik + 1
                                        print('punkty', x.punkty, 'licznik', licznik)
                            else:
                                if x.domek[y][licznik].sasiad == x.domek[y][licznik - 1].nazwa:  # sprawdzenie, czy poprzedni pokoj to dobry sasiad
                                    x.punkty = x.punkty + x.domek[y][licznik].punkty[2]
                                    licznik = licznik + 1
                                    print('punkty', x.punkty, 'licznik', licznik)
                                else:  # jesli aneks nie ma zadnego dobrego sasiada
                                    x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                                    licznik = licznik + 1
                                    print('punkty', x.punkty, 'licznik', licznik)
                        else: #jesli to nie aneks
                            if licznik != 4: #jesli nie jest to ostatni pokoj
                                if x.domek[y][licznik + 1].nazwa == x.domek[y][licznik].nazwa: #sprawdzenie, czy kolejny pokoj to to samo pomieszczenie
                                    x.punkty = x.punkty + x.domek[y][licznik].punkty[2]
                                    licznik = licznik + 2
                                    print('punkty', x.punkty, 'licznik', licznik)
                                else: #jesli kolejny pokoj to inne pomieszczenie
                                    x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                                    licznik = licznik + 1
                                    print('punkty', x.punkty, 'licznik', licznik)
                            else: #jesli jest to ostatnie pomieszczenie
                                x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                                licznik = licznik + 1
                                print('punkty', x.punkty, 'licznik', licznik)
                    else: #jesli pomieszczenie jest jednopokojowe
                        x.punkty = x.punkty + x.domek[y][licznik].punkty[1]
                        licznik = licznik + 1
                        print('punkty', x.punkty, 'licznik', licznik)
            print('liczneie pietra')
            licznik = 0 #wyzerowanie licznika pokoju

        #liczenie punktów za dach
        if len(x.dach) >= 4: #czy gracz ma przynajmniej 4 karty dachu
            kopiaDachu = []
            for w in x.dach: #stworzenie listy z nazwami dachów
                kopiaDachu.append(w.nazwa)
            kopiaDachu = list(set(kopiaDachu)) #stworzenie listy z unikalnymi nazwami dachów
            for t in kopiaDachu:
                if zOknem == True:
                    break
                else:
                    lista = [p for p in x.dach if p.nazwa == t]
                    listadwa = [a for a in x.dach if a.nazwa == t+1]
                    lista.extend(listadwa)
                    if len(lista) >= 4: #czy są 4 takie same dachy
                        tenSamDach = True
                        for f in lista: #sprawdzenie, czy w takich samych dachach jest okno
                            if f.nazwa == t+1:
                                x.punkty = x.punkty + 9
                                zOknem = True
                                print('punkty za okno i dach w tym samym kolorze')
            if zOknem == False and tenSamDach == True:
                x.punkty = x.punkty + 8
                print('ten sam dach')
            elif zOknem == False and tenSamDach == False:
                x.punkty = x.punkty + 3
                print('punkty za rozny dach')
                for d in x.dach:
                    if licznikOkien <= 4:
                        if d.okno:
                            x.punkty = x.punkty + 1
                            licznikOkien = licznikOkien + 1
                            print('punkty za okno')
        else: #nie ma wystarczającej ilości kart dachu
            print('nie ma dachu')
            pass
        licznikOkien = 0
        zOknem = False
        tenSamDach = False
        okno = 0

        for k in x.domek[1]:
            if 6 == k.nazwa: #przyznawanie punktów za funckjonalność domku, lazienki na kazdym piętrze
                for j in x.domek[2]:
                    if 6 == j.nazwa:
                        dwieLazienki = True
                        print('za lazienki')

        if dwieLazienki:
            x.punkty = x.punkty + 3
            print('dwie lazienki sa')
        dwieLazienki = False

        if lazienka:
            pass
        else:
            while licznikpetli <= 4:
                print(x.domek[1][licznikpetli].nazwa)
                if x.domek[1][licznikpetli].nazwa == 6:
                    lazienka = True
                    print('jest lazienka na 1 pietrze')
                licznikpetli = licznikpetli + 1
        licznikpetli = 0

        if lazienka:
            pass
        else:
            while licznikpetli <= 4:
                print(x.domek[2][licznikpetli].nazwa)
                if x.domek[2][licznikpetli].nazwa == 6:
                    lazienka = True
                    print('jest lazienka na 2 pietrze')
                licznikpetli = licznikpetli + 1
        licznikpetli = 0

        if sypialnia:
            pass
        else:
            while licznikpetli <= 4:
                print(x.domek[1][licznikpetli].nazwa)
                if x.domek[1][licznikpetli].nazwa == 4:
                    sypialnia = True
                    print('jest sypialnia na 1 pietrze')
                licznikpetli = licznikpetli + 1
        licznikpetli = 0

        if sypialnia:
            pass
        else:
            while licznikpetli <= 4:
                print(x.domek[2][licznikpetli].nazwa)
                if x.domek[2][licznikpetli].nazwa == 4:
                    sypialnia = True
                    print('jest sypialnia na 2 pietrze')
                licznikpetli = licznikpetli + 1
        licznikpetli = 0

        if kuchnia:
            pass
        else:
           while licznikpetli <= 4:
                print(x.domek[2][licznikpetli].nazwa)
                if x.domek[1][licznikpetli].nazwa == 5:
                    kuchnia = True
                    print('jest kuchnia na 1 pietrze')
                licznikpetli = licznikpetli + 1
        licznikpetli = 0

        if kuchnia:
            pass
        else:
            while licznikpetli <= 4:
                print(x.domek[2][licznikpetli].nazwa)
                if x.domek[2][licznikpetli].nazwa == 5:
                    kuchnia = True
                    print('jest kuchnia na 2 pietrze')
                licznikpetli = licznikpetli + 1
        licznikpetli = 0

        if kuchnia:
            if lazienka:
                if sypialnia:
                    x.punkty = x.punkty + 3
                    print('za lazienke, kuchnie, sypialnie')

        kuchnia = False
        lazienka = False
        sypialnia = False
        licznikpetli = 0

        for m in x.ogrodek:
            x.punkty = x.punkty + m.punkty
            print('punkt za', m.tytul)

        while licznikpetli <= 4:
            print(x.domek[1][licznikpetli].nazwa)
            if x.domek[1][licznikpetli].wyposazenie != 0:
                x.punkty = x.punkty + x.domek[1][licznikpetli].wyposazenie.punkty
                print('wyposazenie na 2 pietrze')
            licznikpetli = licznikpetli + 1
        licznikpetli = 0

        while licznikpetli <= 4:
            print(x.domek[2][licznikpetli].nazwa)
            if x.domek[2][licznikpetli].wyposazenie != 0:
                x.punkty = x.punkty + x.domek[2][licznikpetli].wyposazenie.punkty

            licznikpetli = licznikpetli + 1
        licznikpetli = 0

@app.route('/HeatSeat')
def HeatSeat():
    '''Gra HeatSeat'''
    global Druzyna
    global taliaKartDodatkow
    global taliaKartPomieszczen
    global biezacaTaliaDodatkow
    global biezacaTaliaPomieszczen
    global TaliaDodatkowOdrzuconych
    global TaliaPomieszczenOdrzuconych
    global tura
    global licznikGracza
    global zmiana
    global wyniki
    global ruch
    global pierwszyraz
    global pierwszywRundzie


    if ruch:
        tura = tura + 1
        licznikGracza = licznikGracza + 1
        licznikGracza = licznikGracza%4
        ruch = False
    #jesli pierwsza tura, tasuje karty, losuje pierwszego gracza
    if tura == 0:
        if pierwszyraz:
            tura = tura + 1
            licznikGracza = licznikGracza + 1
            licznikGracza = licznikGracza % 4
            shuffle(taliaKartDodatkow)
            shuffle(taliaKartPomieszczen)
            numer = randint(0,3)
            Druzyna[numer].znacznikPierwszegoGracza = True
            Druzyna = zmianaDruzyny(Druzyna, numer)
            pierwszyraz = False
    #jesli tura będzie powyżej 13 to kończy grę
    elif tura == 49:
        liczeniePunktow()
        wyniki.extend([gracz1, gracz2, gracz3, gracz4])
        wyniki.sort(key = lambda x: x.punkty, reverse=True)
        if wyniki[0].punkty != wyniki[1].punkty:
            return render_template('spraw.html', Druzyna=Druzyna, zwyciezca = [wyniki[0]])
        elif wyniki[0].punkty != wyniki[2].punkty:
            return render_template('spraw.html', Druzyna= Druzyna, zwyciezca = [wyniki[0], wyniki[1]])
        elif wyniki[0].punkty != wyniki[3].punkty:
            return render_template('spraw.html', Druzyna= Druzyna, zwyciezca = [wyniki[0], wyniki[1], wyniki[2]])
        else:
            return render_template('spraw.html', Druzyna= Druzyna, zwyciezca = wyniki)
    elif tura > 49:
        if wyniki[0] != wyniki[1]:
            return render_template('spraw.html', Druzyna=Druzyna, zwyciezca=[wyniki[0]])
        elif wyniki[0] != wyniki[2]:
            return render_template('spraw.html', Druzyna=Druzyna, zwyciezca=[wyniki[0], wyniki[1]])
        elif wyniki[0] != wyniki[3]:
            return render_template('spraw.html', Druzyna=Druzyna, zwyciezca=[wyniki[0], wyniki[1], wyniki[2]])
        else:
            return render_template('spraw.html', Druzyna=Druzyna, zwyciezca=wyniki)

    if tura%4 == 1:
        if pierwszywRundzie:
            #zmiana gracza, jesli ktos wybral kartę ze znacznikiem pierwszego gracza
            if zmiana[0] == True:
                zmianaDruzyny(Druzyna, zmiana[1])
                zmiana[0] = False
                zmiana[1] = 5
            #zerowanie malej talii
            biezacaTaliaPomieszczen.clear()
            biezacaTaliaDodatkow.clear()
            # tworzenie talii kart, ktorych gracze moga wybrac podczas rundy
            biezacaTaliaPomieszczen.extend([taliaKartPomieszczen[0],taliaKartPomieszczen[1], taliaKartPomieszczen[2], taliaKartPomieszczen[3],
                                         taliaKartPomieszczen[4]])
            biezacaTaliaDodatkow.extend([taliaKartDodatkow[0], taliaKartDodatkow[1], taliaKartDodatkow[2], taliaKartDodatkow[3]])
            TaliaPomieszczenOdrzuconych.extend([taliaKartPomieszczen[0],taliaKartPomieszczen[1], taliaKartPomieszczen[2], taliaKartPomieszczen[3],
                                         taliaKartPomieszczen[4]])
            TaliaDodatkowOdrzuconych.extend([taliaKartDodatkow[0], taliaKartDodatkow[1], taliaKartDodatkow[2], taliaKartDodatkow[3]])
            #usuwanie kart z ogolnej talii (te ktore pojawily się w malej talii)
            del taliaKartPomieszczen[:5]
            del taliaKartDodatkow[:4]
            pierwszywRundzie = False
    # print(licznikGracza)


    domek = Druzyna[licznikGracza].domek

    return render_template('HeatSeat.html', taliaPomieszczen=biezacaTaliaPomieszczen, taliaDodatkow=biezacaTaliaDodatkow, tura=tura,
                           gracz = Druzyna[licznikGracza], domek = domek)

@app.route('/HeatSeat/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def runda(kartaPomieszczen, kartaDodatkow):
    global Druzyna
    global TaliaDodatkowOdrzuconych
    global TaliaPomieszczenOdrzuconych
    global biezacaTaliaPomieszczen
    global biezacaTaliaDodatkow
    global licznikGracza
    global tura
    global zmiana
    indeks = 0
    domek = Druzyna[licznikGracza].domek

    #szukanie wybranej karty pomieszczenia w talii
    for x in TaliaPomieszczenOdrzuconych:
        if x.id == kartaPomieszczen:
            kartaPomieszczen = x

    #usuwanie wybranej karty z biezacej talii
    for x in biezacaTaliaPomieszczen:
        if x == kartaPomieszczen:
            indeks = biezacaTaliaPomieszczen.index(kartaPomieszczen)
            biezacaTaliaPomieszczen[indeks] = 'tlo'

    if kartaDodatkow == 123456:
        kartaDodatkow = karty.karta_pierwszego_gracza
    else:
        for x in TaliaDodatkowOdrzuconych:
            if x.id == kartaDodatkow:
                kartaDodatkow = x

        for x in biezacaTaliaDodatkow:
            if x == kartaDodatkow:
                indeks = biezacaTaliaDodatkow.index(kartaDodatkow)
                biezacaTaliaDodatkow[indeks] = 'tlo'


    return render_template('runda.html', kartaPomieszczen=kartaPomieszczen, kartaDodatkow = kartaDodatkow, gracz = Druzyna[licznikGracza],
                           domek = domek, tura = tura)

@app.route('/polozenie/<int:t>/<int:loopindex>/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def polozenie(t, loopindex, kartaPomieszczen, kartaDodatkow):
    global Druzyna
    global TaliaDodatkowOdrzuconych
    global TaliaPomieszczenOdrzuconych
    global biezacaTaliaPomieszczen
    global licznikGracza
    global tura
    global taliaKartPomieszczen
    global zmiana
    global ruch
    global pierwszywRundzie

    domek = Druzyna[licznikGracza].domek
    dach = Druzyna[licznikGracza].dach
    ogrodek = Druzyna[licznikGracza].ogrodek

    if kartaPomieszczen == 58:
        kartaPomieszczen = karty.PustyPokoj
    else:
        for x in TaliaPomieszczenOdrzuconych:
            if x.id == kartaPomieszczen:
                kartaPomieszczen = x

    if kartaDodatkow == 123456:
        kartaDodatkow = karty.karta_pierwszego_gracza
    else:
        for x in TaliaDodatkowOdrzuconych:
            if x.id == kartaDodatkow:
                kartaDodatkow = x

    if domek[t][loopindex] == '0':
        #sprawdzenie, czy piętro niżej jest jakieś pomieszczenie, piwnicy (t = 3) nie trzeba sprawdzać
        if t == 3 or domek[t+1][loopindex] != '0':
            #sprawdzenie czy pomieszczenie jest na dobrym piętrze
            if t in kartaPomieszczen.miejsce:
                domek[t][loopindex] = kartaPomieszczen
                if kartaDodatkow.id == 123456:
                    zmiana[0] = True
                    zmiana[1] = licznikGracza
                elif kartaDodatkow.nazwa >= 100 and kartaDodatkow.nazwa <= 601:
                    dach.append(kartaDodatkow)
                elif kartaDodatkow.miejsce[0] == 2121:
                    ogrodek.append(kartaDodatkow)
                    if licznikGracza % 4 == 3:
                        if tura >= 4:
                            pierwszywRundzie = True
                    ruch = True
                elif kartaDodatkow.miejsce[0] != 2121:
                    if licznikGracza % 4 == 3:
                        if tura >= 4:
                            pierwszywRundzie = True
                    ruch = True
                    return render_template('dodawanieWyposazenia.html', kartaPomieszczen=kartaPomieszczen, kartaDodatkow = kartaDodatkow,
                                           gracz = Druzyna[licznikGracza],
                                   domek = domek, tura = tura )

                if licznikGracza%4 == 3:
                    if tura >= 4:
                        pierwszywRundzie = True
                ruch = True
                gracz = Druzyna[licznikGracza]
                return render_template('runda1.html', domek = domek, gracz = gracz)
            else:
                return render_template('runda.html', x='Położyłeś pomieszczenia na złym piętrze',
                                       kartaPomieszczen=kartaPomieszczen, kartaDodatkow=kartaDodatkow,
                                       gracz=Druzyna[licznikGracza],
                                       domek=domek, tura=tura)
        else:
            return render_template('runda.html', x = 'Nie możesz położyć pomieszczenia nad pustym pomieszczeniem',
                                   kartaPomieszczen=kartaPomieszczen, kartaDodatkow = kartaDodatkow, gracz = Druzyna[licznikGracza],
                                   domek = domek, tura = tura)
    else:
        return render_template('runda.html', x='To było niegodne zagranie!',
                               kartaPomieszczen=kartaPomieszczen, kartaDodatkow=kartaDodatkow,
                               gracz=Druzyna[licznikGracza],
                               domek=domek, tura=tura)

@app.route('/polozenieWyposazenia/<int:t>/<int:loopindex>/<int:kartaDodatkow>')
def polozenieWyposazenia(t, loopindex, kartaDodatkow):
    global Druzyna
    global TaliaDodatkowOdrzuconych
    global TaliaPomieszczenOdrzuconych
    global biezacaTaliaPomieszczen
    global licznikGracza
    global tura
    global taliaKartPomieszczen
    global ruch
    global pierwszywRundzie

    domek = Druzyna[licznikGracza].domek

    for x in TaliaDodatkowOdrzuconych:
        if x.id == kartaDodatkow:
            kartaDodatkow = x

    if domek[t][loopindex].nazwa in kartaDodatkow.miejsce:
        if domek[t][loopindex].wyposazenie == 0:
            domek[t][loopindex].wyposazenie = kartaDodatkow
            domek[t][loopindex].zamkniecie = True
        else:
            return render_template('dodawanieWyposazenia.html', kartaDodatkow=kartaDodatkow,
                                   gracz=Druzyna[licznikGracza],
                                   domek=domek, tura=tura, x='Nie mozesz polozyc tutaj wyposazenia')
    else:
        return render_template('dodawanieWyposazenia.html', kartaDodatkow = kartaDodatkow,
                                       gracz = Druzyna[licznikGracza],
                               domek = domek, tura = tura, x = 'Nie mozesz polozyc tutaj wyposazenia' )
    ruch = True
    if licznikGracza % 4 == 3:
        if tura >= 4:
            pierwszywRundzie = True
    gracz = Druzyna[licznikGracza]
    return render_template('runda1.html', domek = domek, gracz = gracz)

@app.route('/nowaGra')
def nowaGra():
    global Druzyna
    global taliaKartDodatkow
    global taliaKartPomieszczen
    global biezacaTaliaDodatkow
    global biezacaTaliaPomieszczen
    global TaliaDodatkowOdrzuconych
    global TaliaPomieszczenOdrzuconych
    global tura
    global licznikGracza
    global zmiana
    global wyniki
    global pierwszyraz
    global ruch
    global pierwszywRundzie

    # pelna talia kart pomieszczen na poczatek gry
    taliaKartPomieszczen = [karty.gabinet, karty.PokojGier, karty.biblioteka, karty.PokojDzieciecy1,
                            karty.PokojDzieciecy2,
                            karty.PokojDzieciecy3, karty.PokojDzieciecy4, karty.PokojDzieciecy5, karty.PokojDzieciecy6,
                            karty.PokojDzieciecy7, karty.PokojDzieciecy8, karty.kuchnia1, karty.kuchnia2,
                            karty.kuchnia3,
                            karty.kuchnia4, karty.kuchnia5, karty.kuchnia6, karty.kuchnia7, karty.kuchnia8,
                            karty.sypialnia1,
                            karty.sypialnia2, karty.sypialnia3, karty.sypialnia4, karty.sypialnia5, karty.sypialnia6,
                            karty.sypialnia7, karty.sypialnia8, karty.lazienka1, karty.lazienka2, karty.lazienka3,
                            karty.lazienka4, karty.lazienka5, karty.lazienka6, karty.lazienka7, karty.lazienka8,
                            karty.salon1,
                            karty.salon2, karty.salon3, karty.salon4, karty.salon5, karty.salon6, karty.salon7,
                            karty.salon8,
                            karty.salon9, karty.salon10, karty.salon11, karty.salon12, karty.spizarnia, karty.garderoba,
                            karty.sauna, karty.skladzik, karty.warsztat, karty.pralnia, karty.PiwniczkaNaWino,
                            karty.garaz1,
                            karty.garaz2, karty.garaz3, karty.garaz4, karty.garaz5, karty.garaz6]

    # pelna talia kart dodatkow na poczatek gry
    taliaKartDodatkow = [karty.brazowyOkno, karty.brazowy1, karty.brazowy2, karty.brazowy3, karty.brazowy4,
                         karty.brazowy5,
                         karty.brazowy6, karty.fioletowyOkno, karty.fioletowy1, karty.fioletowy2, karty.fioletowy3,
                         karty.fioletowy4, karty.fioletowy5, karty.fioletowy6, karty.pomaranczowyOkno,
                         karty.pomaranczowy1,
                         karty.pomaranczowy2, karty.pomaranczowy3, karty.pomaranczowy4, karty.pomaranczowy5,
                         karty.pomaranczowy6,
                         karty.czerwonyOkno, karty.czerwony1, karty.czerwony2, karty.czerwony3, karty.czerwony4,
                         karty.czerwony5,
                         karty.czerwony6, karty.zielonyOkno, karty.zielony1, karty.zielony2, karty.zielony3,
                         karty.zielony4,
                         karty.czarnyOkno, karty.czarny1, karty.czarny2, karty.czarny3, karty.czarny4,
                         karty.DomekNaDrzewie,
                         karty.DomekDlaPtakow, karty.DomekDlaKota, karty.MaszynaDoLodow, karty.jacuzzi, karty.Wanna,
                         karty.fortepian,
                         karty.obrazy, karty.lozko, karty.regaly]
    # talia kart, ktore gracz moze wybrac podczas rundy
    biezacaTaliaPomieszczen = []
    biezacaTaliaDodatkow = []
    TaliaPomieszczenOdrzuconych = []
    TaliaDodatkowOdrzuconych = []
    tura = 0
    licznikGracza = -1
    gracz = 0
    domek = 0
    zmiana = [False, 5]
    wyniki = []
    ruch = False
    pierwszyraz = True
    pierwszywRundzie = True
    for x in taliaKartPomieszczen:
        x.wyposazenie = 0
        x.zamkniecie = False
    # domki poszczegolnych graczy
    Domek1 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
    Domek2 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
    Domek3 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
    Domek4 = {1: ['0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0'], 3: ['tlo', 'dach', 'tlo', '0', '0']}
    Dach1 = []
    Dach2 = []
    Dach3 = []
    Dach4 = []
    Ogrod1 = []
    Ogrod2 = []
    Ogrod3 = []
    Ogrod4 = []

    # tworzenie graczy
    gracz1 = Gracze('gracz1')
    gracz1.dach = Dach1
    gracz1.domek = Domek1
    gracz1.ogrodek = Ogrod1

    gracz2 = Gracze('gracz2')
    gracz2.dach = Dach2
    gracz2.domek = Domek2
    gracz2.ogrodek = Ogrod2

    gracz3 = Gracze('gracz3')
    gracz3.dach = Dach3
    gracz3.domek = Domek3
    gracz3.ogrodek = Ogrod3

    gracz4 = Gracze('gracz4')
    gracz4.dach = Dach4
    gracz4.domek = Domek4
    gracz4.ogrodek = Ogrod4

    # tworzenie druzyny
    Druzyna = [gracz1, gracz2, gracz3, gracz4]


    return redirect('/HeatSeat')

