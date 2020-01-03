from flask import Flask, render_template

app = Flask(__name__)

@app.route('/JedenGracz')
def JedenGracz():
    Domek1={}
    Domek2={}
    Domek3={}
    Domek4={}
    return "Jeden Gracz kontra komputer"

if __name__ == '__main__':
    app.debug = True
    app.run()
