from flask import Flask, render_template
from database import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/edit')
def edit():
    data = get_data()
    return render_template('edit.html',data=data)

if __name__ == 'main':
    app.run()