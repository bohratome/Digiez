from marshmallow import Schema, fields, pre_load, validate
from digiez_api.extensions import db, ma
from . base_model import BaseModel, now


class Mall(db.Model):
    __tablename__ = 'malls'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    creation_date = db.Column(
        'CREATION_DATE', db.DateTime, default=now, nullable=False)
    last_modification_date = db.Column(
        'LAST_MODIFICATION_DATE', db.DateTime, default=now, onupdate=now, nullable=False)

    def __init__(self, name):
        self.name = name

class MallSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    account_id = fields.Integer()

mall_schema = MallSchema()
malls_schema = MallSchema(many=True)
