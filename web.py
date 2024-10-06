from flask import Flask, render_template, jsonify
from utils.dataOutput import output

app = Flask(__name__)

@app.route('/')
def index():
    data = output()
    return render_template('index.html', users=data)

@app.route('/all')
def all():
    data = output()
    return render_template('all.html', users=data)

@app.route('/all-data')
def all_data():
    data = output() 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
