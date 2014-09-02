from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging
from flask_mail import Mail


app = Flask(__name__)

#app.config.from_object('config.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

mail = Mail(app)


from app import views, models, forms


