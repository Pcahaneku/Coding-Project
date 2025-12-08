from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User
from datetime import datetime
from flask_bcrypt import Bcrypt


app = Flask(__name__) 
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safari.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='avery_long_secret_random_key'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/') #This leads users to the Homepage
def homepage():
    return render_template('index.html')

@app.route('/signup') #This leads users to the SignUp Page
def signup():
    return render_template('signup.html') 

@app.route('/signup', methods=['POST'])
def add_users():
    if request.method == 'POST':

        firstname = request.form.get['firstname']
        lastname = request.form.get['lastname']
        email = request.form.get['email']
        plain_password = request.form.get['password']
        hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')

        dob = request.form.get['dob']

        if dob: 
            try:
                dob = datetime.strptime(dob, '%Y-%m-%d').date() #Converts the date of birth string to a date object
            except ValueError:
                return "Invalid date format. Please use YYYY-MM-DD."
        
        user_option = request.form.get['user_option']

        #conn = sqlite3.connect('safari.db')
        #c = conn.cursor()
       #try:
            #c.execute("INSERT INTO users (firstname, lastname, email, password, user_option) VALUES (?, ?, ?, ?, ?)",
                    #(firstname, lastname, email, hashed_password, user_option))
            #conn.commit()
        #except sqlite3.IntegrityError:
            #conn.close()
            #return "Email already registered!"
        #conn.close()
        #return render_template(url_for('homepage'))

        new_user = User(firstname=firstname, lastname=lastname, email=email, password=hashed_password, dob=dob, user_option=user_option)

        try:
            db.session.add(new_user) 
            db.session.commit()
            return render_template('/login.html') #directs users to the Login Page
        except Exception as e:
            return f"An error occured: {e}"

@app.route('/login', methods=['GET','POST']) #This leads users to the Login Page
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()

        if user and bcrypt.check_password_hash(user.password, password):     
            return render_template('/ticket.html', message="You've been logged in successfuly", message_type="success")
        else:
            return render_template('/ticket.html', message="Login Failed, Please check your Email Address and Password and Try Again.", message_type="error")
        
    return render_template('login.html')


@app.route('/ticket') #This leads users to the Ticket Page
def ticket():
    return render_template('ticket.html')

@app.route('/hotel') #This leads users to the Hotel Page
def hotel():
    return render_template('hotel.html')

@app.route('/guides') #This leads users to the Educational Guides Page Page
def guides():
    return render_template('guides.html')

#This helps in running the app in debug mode. By reloading the server when code changes.
if __name__ == '__main__':
    app.run(debug=True)