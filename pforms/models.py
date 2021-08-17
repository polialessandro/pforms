import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite://',echo=True)
Base=declerative_base()

class Utenti(Base):
    __tablename__='Utenti'			
    id_utente: Column(Integer, primarykey=True)

class Domande(Base):
    __tablename__='Domande'
    id_domanda: Column(Integer, primarykey=True)
    testo: Column(String)
    
    
class Risposte(Base):
    __tablename__='Risposte'
    id_risposta: Column(Integer, primarykey=True)
    testo: Column(String)
    

class Categorie(Base):
    __tablename__='Categorie'
    id_categoria: Column(Integer, primarykey=True)
    tipo: Column(String)
