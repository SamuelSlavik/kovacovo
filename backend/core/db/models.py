from .databases import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean, UUID, LargeBinary, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)


class DocumentORM(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    document = Column(String(255), nullable=False)