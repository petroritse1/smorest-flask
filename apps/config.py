import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

 
class Config:
    load_dotenv()
    SECRET_KEY =  os.environ.get("SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "new_data.db")
    SQLALCHEMY_DATABASE_URI =  'postgres://yyfyfgrr:OrL96gzCIuA0i9EvSRITWCO04jqEZYKF@lucky.db.elephantsql.com/yyfyfgrr'
    SQLALCHEMY_TRACK_MODIFICATION = False
