from flask import Flask, render_template, request
from models import db


app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safari.db'


db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/') #This leads users to the Homepage
def homepage():
    return render_template('index.html')

@app.route('/signup') #This leads users to the SignUp Page
def signup():
    return render_template('signup.html') 

@app.route('/login') #This leads users to the Login Page
def login():
    return render_template('login.html')

@app.route('/ticket') #This leads users to the Ticket Page
def ticket():
    return render_template('ticket.html')

@app.route('/hotel') #This leads users to the Hotel Page
def hotel():
    return render_template('hotel.html')

#This helps in running the app in debug mode. By reloading the server when code changes.
if __name__ == '__main__':
    app.run(debug = True)