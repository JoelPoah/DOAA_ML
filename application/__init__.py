from flask import Flask
import pickle
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#create the Flask app
app = Flask(__name__)
# load configuration from config.cfg
app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    from .models import Entry
    db.create_all()
    db.session.commit()
    print('Created Database!')
#run the file routes.py


#AI model file
joblib_file = "./AI/RFCmodel.pkl"
# Load from file
with open(joblib_file, 'rb') as f:
    ai_model = pickle.load(f)


from application import routes