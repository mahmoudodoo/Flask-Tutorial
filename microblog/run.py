#!flask-venv/bin/python

# run the server so we can run the server by 'python3 <filename> in our situation the name of file is run.py'
from app import app
app.run(debug=True)

