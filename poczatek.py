from flask import Flask, render_template
import JedenGracz, HeatSeat, Multiplayers

app = Flask(__name__)

@app.route('/poczatek')
def main():
    return render_template('index.html')

@app.route('/JedenGracz/<int:liczbaKomputerow>')
def JGWybor(liczbaKomputerow):
    return JedenGracz.JedenGraczWybor(liczbaKomputerow)

@app.route('/JedenGracz')
def JG():
    return JedenGracz.JedenGracz()

@app.route('/HeatSeat')
def HS():
    return HeatSeat.HeatSeat()

@app.route('/Multiplayers')
def MP():
    return Multiplayers.Multiplayers()

@app.route('/Zasady')
def Zasady():
    return render_template('zasady.html')

@app.route('/ileGraczy')
def ileGraczy():
    return render_template('ileGraczy.html')

@app.route('/HeatSeat/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def runda(kartaPomieszczen, kartaDodatkow):
    return HeatSeat.runda(kartaPomieszczen, kartaDodatkow)

@app.route('/polozenie/<int:t>/<int:loopindex>/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def HeatSeatPolozenie(t, loopindex, kartaPomieszczen, kartaDodatkow):
    return HeatSeat.polozenie(t, loopindex, kartaPomieszczen,kartaDodatkow)

@app.route('/polozenieWyposazenia/<int:t>/<int:loopindex>/<int:kartaDodatkow>')
def polozenieWyposazenia(t, loopindex, kartaDodatkow):
    return  HeatSeat.polozenieWyposazenia(t, loopindex, kartaDodatkow)

@app.route('/JedenGracz/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def rundaJG(kartaPomieszczen, kartaDodatkow):
    return JedenGracz.runda1(kartaPomieszczen, kartaDodatkow)

@app.route('/polozenieJG/<int:t>/<int:loopindex>/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def polozenieJG(t, loopindex, kartaPomieszczen, kartaDodatkow):
    return JedenGracz.polozenieJG(t, loopindex, kartaPomieszczen,kartaDodatkow)

@app.route('/polozenieWyposazeniaJG/<int:t>/<int:loopindex>/<int:kartaDodatkow>')
def polozenieWyposazeniaJG(t, loopindex, kartaDodatkow):
    return  JedenGracz.polozenieWyposazeniaJG(t, loopindex, kartaDodatkow)

@app.route('/nowaGra')
def nowaGra():
    return HeatSeat.nowaGra()

@app.route('/newGame')
def newGame():
    return JedenGracz.newGame()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, debug = True)

