from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = 'Ph1140'
servidor = 'localhost'
database = 'doar'
SQLALCHEMY_DATABASE_URL =\
    f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# criu o banco de dados


def criar_bd_se_não_existe():
    conn = mysql.connector.connect(user=usuario, password=senha, host=servidor)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    conn.commit()
    cursor.close()
    conn.close()


def criar_bd():
    criar_bd_se_não_existe()
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
