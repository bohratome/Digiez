import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"
# SQLALCHEMY_DATABASE_URI = "sqlite:///app.db" # For SqLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')