import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table User.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    e_mail= Column(String(250))

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table Follower
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.id'))
    Follower = relationship (User)
    User = relationship (Follower)
    
class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table User.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    autor_id = Column(String(50))
    post_id = Column(Integer, ForeignKey('User.id'))
    Comment = relationship(User)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table User.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Comment.id'))
    Post = relationship(Comment)

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table User.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(500))
    url = Column(String(50))
    post_id = Column(String(50), ForeignKey('Post.id'))
    Media = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
