from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    registrations = db.relationship('Registration', backref='user', lazy=True)

    def __repr__(self):
        return f"<Volunteer(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')>"

class Organization(db.Model):
    __tablename__ = 'organizations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    headquarters = db.Column(db.String, nullable=False)
    date_founded = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String)
    contact_email = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Organization(id={self.id}, name='{self.name}')>"

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), nullable=False)

    registrations = db.relationship('Registration', backref='event', lazy=True)

    def __repr__(self):
        return f"<Event(id={self.id}, name='{self.name}'), date='{self.date}')>"
    
class Registration(db.Model):
    __tablename__ = 'registrations'

    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)