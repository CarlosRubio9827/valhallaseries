from flask_mysqldb import MySQL
from . import app

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3307
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "piedradelcanada2"
mysql = MySQL(app)