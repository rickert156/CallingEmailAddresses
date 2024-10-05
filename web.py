from flask import Flask, render_template
import sqlite3
from dataOutput import output

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html')


if __name__ == '__main__':
    app.run(debug=True)
