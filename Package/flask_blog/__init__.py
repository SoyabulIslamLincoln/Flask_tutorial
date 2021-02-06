from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY']= 'b95cdeda326355d16bc1a85e8877a88e'
### DAtabase Location
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)


from flask_blog import routes