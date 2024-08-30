import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma
from libraries import LibrariesSchema

class Users(db.Model):
  __tablename__= 'users'
  user_id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
  first_name = db.Column(db.String(), nullable = False)
  last_name = db.Column(db.String())
  email = db.Column(db.String(), nullable =False, unique = True)
  phone = db.Column(db.String())
  city = db.Column(db.String())
  state = db.Column(db.String())
  lib_id = db.Column(db.ForeignKey('libraries.lib_id'), nullable = False)
  active = db.Column(db.Boolean(), default = True)

  library = db.relationship('Libraries', back_populates='users')
  def __init__(self, first_name, last_name, email, phone, city, state, lib_id, active):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone = phone
    self.city = city
    self.state = state
    self.lib_id = lib_id
    self.active = active

class UsersSchema(ma.Schema):
  class Meta:
    fields = ['user_id', 'first_name', 'last_name', 'email', 'phone', 'city', 'state', 'library', 'active']

  library = ma.fields.Nested(LibrariesSchema())

user_schema = UsersSchema()
users_schema = UsersSchema(many = True)