import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    text = Column(String(250))
    img = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", foreign_keys=["user_id"])


class Follow(Base):
    __tablename__ = "follow"
    id = Column(Integer, primary_key=True)
    follower_user = Column(Integer, ForeignKey("user.id"))
    following_user = Column(Integer, ForeignKey("user.id"))
    follower = relationship("User", foreign_keys=["follower_user"])
    following = relationship("User", foreign_keys=["following_user"])


class PostComment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship("User", foreign_keys=["user_id"])
    post = relationship("Post", foreign_keys=["post_id"])

class PostLike(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship("User", foreign_keys=["user_id"])
    post = relationship("Post", foreign_keys=["post_id"])


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", foreign_keys=["post_id"])


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
