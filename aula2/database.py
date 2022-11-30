from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert
from models import Usuario, Base
from sqlalchemy import Column, Integer, String, MetaData
from settings import DATABASE_PASSWORD, DATABASE_USER

database_url = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:5432/aula2"

engine = create_engine(database_url)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)


def add_usuario():
    Session = sessionmaker(engine)
    session = Session()

    query = (
        insert(Usuario).
        values(
            nome='Joao',
            email='joao@teste.com'
        )
    )
    conn = engine.connect()
    result = conn.execute(query)

    session.commit()


def add_usuario_json(json_usuario):
    Session = sessionmaker(engine)
    session = Session()

    query = (
        insert(Usuario).
        values(
            nome=json_usuario['nome'],
            email=json_usuario['email']
        )
    )
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"status": "User has been added"}

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret


def get_all_users():
    Session = sessionmaker(engine)
    session = Session()

    s = select(Usuario).where(Usuario.id == 1)
    conn = engine.connect()
    res = conn.execute(s)
    for row in res:
        print(row['nome'])


# class Usuario(Base):
#     __tablename__ = 'usuario'
#     id = Column(Integer, primary_key=True)
#     nome = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)

#     def __init__(self, nome=None, email=None):
#         self.name = nome
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % (self.nome)
