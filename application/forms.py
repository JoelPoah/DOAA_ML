from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField,RadioField,IntegerField
from wtforms.validators import Length, InputRequired, ValidationError,NumberRange
class PredictionForm(FlaskForm):
    gender = RadioField('IsMale',validators=[InputRequired()], choices=[(1,'male_1'),(0,'female_0')])
    hypertension = RadioField('hypertension', choices=[(1,'hypertension_yes_1'),(0,'hypertension_no_0')])
    heartdisease = RadioField('Isheartdisease', choices=[(1,'heart_disease_yes_1'),(0,'heart_disease_no_0')])
    married = RadioField('Ismarried', choices=[(1,'married_1'),(0,'not_married_0')])
    urban = RadioField('Isurban', choices=[(1,'urban_1'),(0,'rural_0')])
    smoking = RadioField('Issmoking', choices=[(1,'smoking_1'),(0,'not_smoking_0')])
    smokeformerly = RadioField('Issmokeformerly', choices=[(1,'formerly_smoked_yes_1'),(0,'never_smoked_0')])
    govtjob = RadioField('Isgovtjob', choices=[(1,'Gov_Job_yes_1'),(0,'non_Govt_job_0')])
    workedbefore = RadioField('Isworkedbefore', choices=[(1,'worked_before_1'),(0,'never_worked_0')])
    privatework = RadioField('Isprivatework', choices=[(1,'private_work_1'),(0,'non_private_work_0')])
    selfemployed = RadioField('Isselfemployed', choices=[(1,'self_employed_1'),(0,'not_self_employed_0')])
    workchildren = RadioField('Isworkchildren', choices=[(1,'work_w_children_1'),(0,'not_working_w_children_0')])
    Name = StringField("Name",validators=[InputRequired(),Length(min=1,max=30)])
    age = FloatField("Age",validators=[InputRequired(), NumberRange(0,1000)])
    average_glucose_level = FloatField("Average glucose level",validators=[InputRequired(), NumberRange(0,300)])
    bmi = FloatField("bmi",validators=[InputRequired(), NumberRange(0,100)])
    submit = SubmitField("Predict") 


    

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[InputRequired(),Length(min=1,max=30)])
    password = StringField("Password",validators=[InputRequired(),Length(min=1,max=30)])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[InputRequired(),Length(min=1,max=30)])
    password = StringField("Password",validators=[InputRequired(),Length(min=1,max=30)])
    submit = SubmitField("Register")