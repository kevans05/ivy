#################
#### imports ####
#################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


###############
#### config ####
################

app = Flask(__name__)
app.config.from_object('config')


from static import views