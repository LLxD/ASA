from sqlalchemy import Column, Integer, String, MetaData
#from database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(120))

    def __init__(self, nome=None, email=None):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.nome)