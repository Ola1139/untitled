from flask import Flask, render_template
import JedenGracz, HeatSeat, Multiplayers

app = Flask(__name__)

@app.route('/poczatek')
def main():
    return render_template('index.html')

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

@app.route('/HeatSeat/<int:kartaPomieszczen>/<int:kartaDodatkow>')
def runda(kartaPomieszczen, kartaDodatkow):
    return HeatSeat.runda(kartaPomieszczen, kartaDodatkow)

if __name__ == '__main__':
    app.run(debug = True)

