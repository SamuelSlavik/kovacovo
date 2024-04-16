import os


class Config():
    def __init__(self):
        self.BASEDIR = os.path.abspath(os.path.dirname(__file__))
        self.SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5435/postgres")
        self.FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
        self.DOCUMENTS_DIR = os.getenv("DOCUMENTS_DIR", "./documents")


config = Config()
