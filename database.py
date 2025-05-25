from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión usando pymysql (modo síncrono)
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/test1234"

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear la sesión (modo síncrono)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para los modelos
Base = declarative_base()

# Metadata usada por Alembic
target_metadata = Base.metadata