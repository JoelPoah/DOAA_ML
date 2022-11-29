from application import app
from flask import render_template,request,flash, redirect, url_for 
from application import ai_model
from application.forms import PredictionForm, LoginForm, RegisterForm
from application import db
from application.models import Entry, User
from datetime import datetime
import logging
import sys 
#Handles http://127.0.0.1:5000/hello
end_type = ['No Stroke you gonna live','You are gonna have Stroke you gonna die']

@app.route('/registerpage', methods=['GET'])
def registerpage():
    rform1 = RegisterForm()
    return render_template('register.html', form=rform1)
def add_user(new_user):
    try:
        db.session.add(new_user)
        db.session.commit()
        return new_user.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")

@app.route('/register', methods=['GET','POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            user = rform.username.data
            passw = rform.password.data
            new_user = User(username=user, password=passw)
            user_id = add_user(new_user)
            if user_id:
                flash('User Registered Successfully','success')
                return render_template('register.html', form=rform)
            else:
                flash('User Registration Failed','danger')
                return render_template('register.html', form=rform)
        else:
            flash(rform.errors)
    return render_template('register.html', form=rform)



@app.route('/', methods=['GET'])
def login_page():
    lform = LoginForm()
    return render_template('login.html',form=lform)

@app.route('/login', methods=['POST'])
def login():
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():
            user = lform.username.data
            passw = lform.password.data
            user = User.query.filter_by(username=user).first()
            if user and user.password == passw:
                flash('User Login Successfully','success')
                return index_page(user.id)
            else:
                flash('User Login Failed','danger')
                return render_template('login.html', form=lform)
        else:
            flash(lform.errors)
    return render_template('login.html', form=lform)



@app.route('/home/<id>', methods=['GET'])
def index_page(id):
    form = PredictionForm()
    return render_template('index.html',form=form, title='Stroke Prediction', id=id)
def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")



def remove_entry(id):
    try:
        entry = Entry.query.get(id) # version 2
        # entry = db.get_or_404(Entry, id)
        db.session.delete(entry)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

@app.route("/<id>/predict", methods=['GET','POST'])
def predict(id):
    form = PredictionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
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
            new_entry = Entry(user_id = id,gender_male=gender_male,hypertension=hypertension,heartdisease=heartdisease,married=married,urban=urban,smoking=smoking,smokeformerly=smokeformerly,govtjob=govtjob,workedbefore=workedbefore,privatework=privatework,selfemployed=selfemployed,workchildren=workchildren,age=age,average_glucose_level=average_glucose_level,bmi=bmi,prediction=int(result[0]),name=name,predicted_on=datetime.utcnow())
            add_entry(new_entry)
            flash(f"Prediction: {end_type[result[0]]}","success")
            return index_page(id)
        else:
            flash("Error, cannot proceed with prediction all input is required","danger")
            return index_page(id)




@app.route("/predictions/<id>", methods=['GET'])
def predictions(id):
    entries = Entry.query.filter_by(user_id=id).all()
    return render_template("predictions.html", title="Predictions", entries=entries, stroke_type=end_type,id=id)


@app.route('/remove/<userid>', methods=['POST'])
def remove(userid):
    form = PredictionForm()
    req = request.form
    id = req["id"]
    remove_entry(id)
    return predictions(userid)


