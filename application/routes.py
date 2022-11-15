from application import app
from flask import render_template,request,flash
from application import ai_model
from application.forms import PredictionForm
from application import db
from application.models import Entry
from datetime import datetime
import logging
import sys 
#Handles http://127.0.0.1:5000/hello
end_type = ['No Stroke you gonna live','You are gonna have  Stroke you gonna die',]
@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():
    form = PredictionForm()

    return render_template('index.html',form=form, title='Stroke Prediction')
@app.route("/predict", methods=['GET','POST'])
def predict():
    form = PredictionForm()
    # if request.method == 'POST':
        # if form.validate_on_submit():
    gender_male = form.gender.data
    hypertension = form.hypertension.data
    heartdisease = form.heartdisease.data
    married = form.married.data
    urban = form.urban.data
    smoking = form.smoking.data
    smokeformerly = form.smokeformerly.data
    govtjob = form.govtjob.data
    workedbefore = form.workedbefore.data
    privatework = form.privatework.data
    selfemployed = form.selfemployed.data
    workchildren = form.workchildren.data
    name = form.Name.data
    age = form.age.data
    average_glucose_level = form.average_glucose_level.data
    bmi = form.bmi.data
    X = [[gender_male,hypertension,heartdisease,married,urban,smokeformerly,smoking,govtjob,workedbefore,privatework,selfemployed,workchildren,age,average_glucose_level,bmi]]
    # sepal_l = form.sepal_l.da ta
    # sepal_w = form.sepal_w.data
    # petal_l = form.petal_l.data
    # petal_w = form.petal_w.data
    # X = [[ gender_male]
    
    result = ai_model.predict(X)
    # new_entry = Entry(sepal_length=sepal_l,
    # sepal_width=sepal_w,
    # petal_length=petal_l,
    # petal_width=petal_w,
    # prediction=int(result[0]),
    # predicted_on=datetime.utcnow())
    # add_entry(new_entry)
    flash(f"Prediction: {end_type[result[0]]}","success")
# else:
#     flash("Error, cannot proceed with prediction","danger")
    return render_template("index.html", title="Enter Iris Parameters", form=form, index=True )


