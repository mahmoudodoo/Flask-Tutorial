# Initialize application 
from flask import Flask
#  app name
app = Flask(__name__)
# to avoid importing error we should import our app in the end
from app import views


