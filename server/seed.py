from faker import Faker

from models import db,User,Organization,Event,Registration
from flask_sqlalchemy import SQLAlchemy
from app import app

#db.init_app(app)
fake = Faker()

with app.app_context():
    users = []
    for n in range(7):
        user = User(first_name=fake.first_name(),last_name=fake.last_name(),email = fake.email())
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    organizations = []
    for n in range(4):  
        organization = Organization(
            name=fake.company(),
            headquarters=fake.city(),
            date_founded=fake.date_this_decade(),
            contact_email=fake.email(),
            phone_number=fake.phone_number(),
        )
        organizations.append(organization)

    db.session.add_all(organizations)
    db.session.commit()