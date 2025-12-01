from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), unique=True, nullable=False)
    lastname = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    user_option = db.Column(db.String, nullable=False)

    def __repr__(self): 
        return f'<User {self.firstname}>'