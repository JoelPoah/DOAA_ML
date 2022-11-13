from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField,RadioField
from wtforms.validators import Length, InputRequired, ValidationError,NumberRange
class PredictionForm(FlaskForm):
    gender = RadioField('IsMale', choices=[('value_1','male_1'),('value_0','female_0')])
    hypertension = RadioField('IsMale', choices=[('value_1','hypertension_yes_1'),('value_0','hypertension_no_0')])
    heartdisease = RadioField('Isheartdisease', choices=[('value_1','heart_disease_yes_1'),('value_0','heart_disease_no_0')])
    married = RadioField('Ismarried', choices=[('value_1','married_1'),('value_0','not_married_0')])
    urban = RadioField('Isurban', choices=[('value_1','urban_1'),('value_0','rural_0')])
    smoking = RadioField('Issmoking', choices=[('value_1','smoking_1'),('value_0','not_smoking_0')])
    smokeformerly = RadioField('Issmokeformerly', choices=[('value_1','formerly_smoked_yes_1'),('value_0','never_smoked_0')])
    govtjob = RadioField('Isgovtjob', choices=[('value_1','Gov_Job_yes_1'),('value_0','non_Govt_job_0')])
    workedbefore = RadioField('Isworkedbefore', choices=[('value_1','worked_before_1'),('value_0','never_worked_0')])
    privatework = RadioField('Isprivatework', choices=[('value_1','private_work_1'),('value_0','non_private_work_0')])
    selfemployed = RadioField('Isselfemployed', choices=[('value_1','self_employed_1'),('value_0','not_self_employed_0')])
    workchildren = RadioField('Isworkchildren', choices=[('value_1','work_w_children_1'),('value_0','not_working_w_children_0')])
    Name = StringField("Name",validators=[InputRequired(),Length(min=1,max=30)])
    age = FloatField("Age",validators=[InputRequired(), NumberRange(0,1000)])
    average_glucose_level = FloatField("Average glucose level",validators=[InputRequired(), NumberRange(0,100)])
    bmi = FloatField("bmi",validators=[InputRequired(), NumberRange(0,100)])
    submit = SubmitField("Predict") 