from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.model import Base

DATABASE_URI = "sqlite:///rental_system.db"

# Create a connection to the database
engine = create_engine(DATABASE_URI)

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()
