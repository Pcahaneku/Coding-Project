from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__) 
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safari.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/') #This leads users to the Homepage
def homepage():
    return render_template('index.html')

@app.route('/signup') #This leads users to the SignUp Page
def signup():
    return render_template('signup.html') 

@app.route('/add_users', methods=['POST'])
def add_users():
    if request.form == 'POST':
        name = request.form['name']
        email = request.form['email']
        plain_password = request.form['password']
        hashed_password = bcrypt_generate_hash(plain_password).decode('utf-8')

        dob = request.form['dob']

        if dob: 
            try:
                dob = datetime.strptime(dob, '%Y-%m-%d').date() #Converts the date of birth string to a date object
            except ValueError:
                return "Invalid date format. Please use YYYY-MM-DD."

        new_user = User(name=name, email=email, password=hashed_password, dob=dob)

        try:
            db.session.add(new_user) 
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"An error occured: {e}"

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