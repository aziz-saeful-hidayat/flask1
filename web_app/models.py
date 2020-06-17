from flask_security import UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Page(db.Model):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    tag = Column(String)
    contents = Column(String)
    url = Column(String)
    is_homepage = Column(Boolean)

    def __repr__(self):
        return self.title


class Menu(db.Model):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    order = Column(Integer)
    page_id = Column(Integer, ForeignKey('page.id'))
    page = relationship('Page', backref=backref('Linked from Menu', uselist=False))

    def __repr__(self):
        return self.title


