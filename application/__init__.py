from flask import Flask
import pickle
#create the Flask app
app = Flask(__name__)
# load configuration from config.cfg
app.config.from_pyfile('config.cfg')
#run the file routes.py


#AI model file
joblib_file = "./AI/RFCmodel.pkl"
# Load from file
with open(joblib_file, 'rb') as f:
    ai_model = pickle.load(f)


from application import routes