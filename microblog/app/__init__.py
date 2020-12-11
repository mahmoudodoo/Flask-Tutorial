from flask import Flask
from app.config import Config
    
#  app name
app = Flask(__name__)
app.config.from_object(Config)
# to avoid importing error we should import our app in the end
from app import routes



