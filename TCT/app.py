from flask import Flask, render_template, request, redirect
from config import config

app = Flask('The Company Tours')

@app.route('/')
def inicio():
    return render_template('inicio.html')
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()