import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Libraries(db.Model):
  __tablename__= 'libraries'
  lib_id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
  name = db.Column(db.String(), nullable = False, unique = True)
  phone = db.Column(db.String())
  city = db.Column(db.String())
  state = db.Column(db.String())
  active = db.Column(db.Boolean(), default = True)
  users = db.relationship('Users', back_populates='library')

  def __init__(self, name, phone,city,state, active):
    self.name = name
    self.phone = phone
    self.city = city
    self.state = state
    self.active = active

class LibrariesSchema(ma.Schema):
  class Meta:
    fields = ['lib_id', 'name', 'phone', 'city', 'state', 'active']
  
library_schema = LibrariesSchema()
libraries_schema = LibrariesSchema(many = True)