#!/usr/bin/python
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt import JWT, jwt_required, current_identity
from flask_bcrypt import Bcrypt
from werkzeug.security import safe_str_cmp


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()


FalloutApp = Flask(__name__)
FalloutApp.config.from_object('config')
bcrypt = Bcrypt(FalloutApp)
db = SQLAlchemy(FalloutApp)
ma = Marshmallow(FalloutApp)
jwt = JWT(FalloutApp, authenticate, identity)

from app import cli

from app.api.calculators import calculators
FalloutApp.register_blueprint(calculators)

from app.api.weapon import weapon
FalloutApp.register_blueprint(weapon)

from app.api.locations import locations
FalloutApp.register_blueprint(locations)

from app.api.weapon_assembler import weapon_assembler
FalloutApp.register_blueprint(weapon_assembler)

from app.models.User import User


@FalloutApp.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity
