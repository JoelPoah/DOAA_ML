from application import app
from flask import render_template
from application.forms import PredictionForm
#Handles http://127.0.0.1:5000/hello
@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():
    form = PredictionForm()
    return render_template('index.html',form=form, title='Stroke Prediction')
