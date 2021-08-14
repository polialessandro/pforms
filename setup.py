from pforms import db, create_app
from pforms.models import User

db.create_all(app=create_app())