from flask import Flask
app = Flask(__name__)
app.secret_key = "21century"
DATABASE = "to-do"