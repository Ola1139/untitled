from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Multiplayers')
def Multiplayers():
    return "Dwóch, trzech, czterech graczy przy różnych komputerach"

if __name__ == '__main__':
    app.debug = True
    app.run()