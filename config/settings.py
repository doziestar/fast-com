import os
from pathlib import Path

basedir = Path(__file__).parent.absolute().parent

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
