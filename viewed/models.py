from sqlalchemy import Column, Integer, SmallInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import mapper
from viewed.database import Base
from werkzeug.security import generate_password_hash, \
     check_password_hash

class FOI(Base):
    __tablename__ = 'options_foi'
    id = Column(String(36), primary_key=True)
    name = Column(String(120), nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, uid=None, user=None, updated_at=None):
        self.id = uid
        self.user = user
        self.updated_at = updated_at      
        
    def __repr__(self):
        return 'FOI' + self.__dict__        


class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    company = Column(String(120), nullable=True)
    phone = Column(String(32), nullable=True)
    address1 = Column(String(120), nullable=True)
    address2 = Column(String(120), nullable=True)
    city = Column(String(120), nullable=True)
    state = Column(String(120), nullable=True)
    postal = Column(String(32), nullable=True)
    country = Column(String(120), nullable=True)
    foi = Column(String(36), ForeignKey(FOI.id), nullable=True)
    experience = Column(SmallInteger, nullable=True)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, uid=None, name=None, email=None, password=None, postal=None, foi=None, \
        experience=None, updated_at=None):
        self.id = uid
        self.name = name
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        else:
            self.password = password
        self.postal = postal
        self.foi = foi
        self.experience = experience
        self.updated_at = updated_at      
        
    def __repr__(self):
        return 'User' + self.__dict__

    def check_password(self, password):
        return check_password_hash(self.password, password)
