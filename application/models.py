from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    gender_male = db.Column(db.Integer, nullable=False)
    hypertension = db.Column(db.Integer, nullable=False)
    heartdisease = db.Column(db.Integer, nullable=False)
    married = db.Column(db.Integer, nullable=False)
    urban = db.Column(db.Integer, nullable=False)
    smoking = db.Column(db.Integer, nullable=False)
    smokeformerly = db.Column(db.Integer, nullable=False)
    govtjob = db.Column(db.Integer, nullable=False)
    workedbefore = db.Column(db.Integer, nullable=False)
    privatework = db.Column(db.Integer, nullable=False)
    selfemployed = db.Column(db.Integer, nullable=False)
    workchildren = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    average_glucose_level = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    prediction = db.Column(db.Integer, nullable=False)
    predicted_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Entry {}>'.format(self.id)


