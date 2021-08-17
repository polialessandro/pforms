from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pforms_role:12345@localhost/pforms'

    db.init_app(app)

    from pforms.site.routes import site
    app.register_blueprint(site)

    from pforms.api.routes import api
    app.register_blueprint(api)

    return app