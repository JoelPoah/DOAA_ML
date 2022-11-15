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
end_type = ['No Stroke you gonna live','You are gonna have  Stroke you gonna die']
@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():

    form = PredictionForm()
    return render_template('index.html',form=form, title='Stroke Prediction')
def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
@app.route("/predict", methods=['GET','POST'])
def predict():
    print('please')
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

    
    result = ai_model.predict(X)
    print(result)
    new_entry = Entry(gender_male=gender_male,hypertension=hypertension,heartdisease=heartdisease,married=married,urban=urban,smoking=smoking,smokeformerly=smokeformerly,govtjob=govtjob,workedbefore=workedbefore,privatework=privatework,selfemployed=selfemployed,workchildren=workchildren,age=age,average_glucose_level=average_glucose_level,bmi=bmi,prediction=int(result[0]),name=name,predicted_on=datetime.utcnow())
    add_entry(new_entry)
    flash(f"Prediction: {end_type[result[0]]}","success")
# else:
#     flash("Error, cannot proceed with prediction","danger")
    return render_template("index.html", title="Enter Iris Parameters", form=form, index=True )


