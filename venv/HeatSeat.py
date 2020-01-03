from flask import Flask, render_template
from random import shuffle, randint
import karty

app = Flask(__name__)

@app.route('/HeatSeat')
def HeatSeat():

    class Gracze():
        def __init__(self, nazwa):
            self.nazwa = nazwa
        znacznikPierwszegoGracza = False
        punkty = 0
        domek = {}
        dach = []

    taliaKartPomieszczen = [karty.gabinet, karty.PokojGier, karty.biblioteka, karty.PokojDzieciecy1, karty.PokojDzieciecy2,
                            karty.PokojDzieciecy3, karty.PokojDzieciecy4, karty.PokojDzieciecy5, karty.PokojDzieciecy6,
                            karty.PokojDzieciecy7, karty.PokojDzieciecy8, karty.kuchnia1, karty.kuchnia2, karty.kuchnia3,
                            karty.kuchnia4, karty.kuchnia5, karty.kuchnia6, karty.kuchnia7, karty.kuchnia8, karty.sypialnia1,
                            karty.sypialnia2, karty.sypialnia3, karty.sypialnia4, karty.sypialnia5, karty.sypialnia6,
                            karty.sypialnia7, karty.sypialnia8, karty.lazienka1, karty.lazienka2, karty.lazienka3,
                            karty.lazienka4, karty.lazienka5, karty.lazienka6, karty.lazienka7, karty.lazienka8, karty.salon1,
                            karty.salon2, karty.salon3, karty.salon4, karty.salon5, karty.salon6, karty.salon7, karty.salon8,
                            karty.salon9, karty.salon10, karty.salon11, karty.salon12, karty.spizarnia, karty.garderoba,
                            karty.sauna, karty.skladzik, karty.warsztat, karty.pralnia, karty.PiwniczkaNaWino, karty.garaz1,
                            karty.garaz2, karty.garaz3, karty.garaz4, karty.garaz5, karty.garaz6]

    taliaKartDodatków = [karty.brazowyOkno, karty.brazowy1, karty.brazowy2, karty.brazowy3, karty.brazowy4, karty.brazowy5,
                         karty.brazowy6, karty.fioletowyOkno, karty.fioletowy1, karty.fioletowy2, karty.fioletowy3,
                         karty.fioletowy4, karty.fioletowy5, karty.fioletowy6, karty.pomaranczowyOkno, karty.pomaranczowy1,
                         karty.pomaranczowy2, karty.pomaranczowy3, karty.pomaranczowy4, karty.pomaranczowy5, karty.pomaranczowy6,
                         karty.czerwonyOkno, karty.czerwony1, karty.czerwony2, karty.czerwony3, karty.czerwony4, karty.czerwony5,
                         karty.czerwony6, karty.zielonyOkno, karty.zielony1, karty.zielony2, karty.zielony3, karty.zielony4,
                         karty.czarnyOkno, karty.czarny1, karty.czarny2, karty.czarny3, karty.czarny4, karty.DomekNaDrzewie,
                         karty.DomekDlaPtakow, karty.DomekDlaKota, karty.MaszynaDoLodow, karty.jacuzzi, karty.Wanna, karty.fortepian,
                         karty.obrazy, karty.lozko, karty.regaly]

    Domek1 = { 1 : ['0','0','0','0','0'], 2 : ['0','0','0','0','0'], 3 : ['tlo','dach','tlo','0','0']}
    Domek2 = { 1 : ['0','0','0','0','0'], 2 : ['0','0','0','0','0'], 3 : ['tlo','dach','tlo','0','0']}
    Domek3 = { 1 : ['0','0','0','0','0'], 2 : ['0','0','0','0','0'], 3 : ['tlo','dach','tlo','0','0']}
    Domek4 = { 1 : ['0','0','0','0','0'], 2 : ['0','0','0','0','0'], 3 : ['tlo','dach','tlo','0','0']}
    Dach1 = []
    Dach2 = []
    Dach3 = []
    Dach4 = []

    gracz1 = Gracze('gracz1')
    gracz1.dach = Dach1
    gracz1.domek = Domek1

    gracz2 = Gracze('gracz2')
    gracz2.dach = Dach2
    gracz2.domek = Domek2

    gracz3 = Gracze('gracz3')
    gracz3.dach = Dach3
    gracz3.domek = Domek3

    gracz4 = Gracze('gracz4')
    gracz4.dach = Dach4
    gracz4.domek = Domek4

    shuffle(taliaKartDodatków)
    shuffle(taliaKartPomieszczen)

    Druzyna = [gracz1, gracz2, gracz3, gracz4]

    def rozgrywka(taliaDodatkow, taliaPomieszczen, Druzyna):
        tura = 1
        numer = randint(0,4)
        for x in Druzyna:
            x.znacznikPierwszegoGracza = False
        Druzyna[numer].znacznikPierwszegoGracza = True
        Druzyna = zmianaDruzyny(Druzyna, numer)
        for x in taliaPomieszczen:
            biezacaTaliaPomieszczen = []
            biezacaTaliaDodatkow = []
            biezacaTaliaPomieszczen.extend([taliaPomieszczen[0],taliaPomieszczen[1], taliaPomieszczen[2], taliaPomieszczen[3],
                                     taliaPomieszczen[4]])
            biezacaTaliaDodatkow.extend([taliaDodatkow[0], taliaDodatkow[1], taliaDodatkow[2], taliaDodatkow[3]])
            del taliaPomieszczen[:5]
            del taliaDodatkow[:4]
            runda(biezacaTaliaPomieszczen, biezacaTaliaDodatkow, Druzyna, tura)
            tura = tura + 1

    def zmianaDruzyny(Druzyna, numer):
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


    def runda(taliaPomieszczen, taliaDodatkow, druzyna, tura):
        render_template('HeatSeat.html', taliaPomieszczen = taliaPomieszczen, taliaDodatkow = taliaDodatkow, tura = tura)

    return render_template('HeatSeat.html', domek = Domek1)

if __name__ == '__main__':
    app.run(debug = True)