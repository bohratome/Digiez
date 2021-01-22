import datetime
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from digiez_api.extensions import db, ma


def now():
    return datetime.datetime.utcnow()

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    creation_date = db.Column(
        'CREATION_DATE', db.DateTime, default=now, nullable=False)
    last_modification_date = db.Column(
        'LAST_MODIFICATION_DATE', db.DateTime, default=now, onupdate=now, nullable=False)

    def __init__(self, name):
        self.name = name

class AccountSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)