import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Books(db.Model):
  __tablename__= 'books'
  book_id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
  title = db.Column(db.String(), nullable = False)
  author = db.Column(db.String())
  publish_date = db.Column(db.String())

  def __init__(self, title, author, publish_date):
    self.title = title
    self.author = author
    self.publish_date = publish_date

class BooksSchema(ma.Schema):
  class Meta:
    fields = ['book_id', 'title', 'author', 'publish_date']

book_schema = BooksSchema()
books_schema = BooksSchema(many = True)