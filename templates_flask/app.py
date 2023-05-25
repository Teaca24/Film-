from flask import render_template
from flask import Flask
import mysql.connector

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ghiblidata"
)
mycursor = mydb.cursor()



app = Flask(__name__)


@app.route('/')
def hello():
    mycursor.execute("SELECT * FROM movies")
    myresult = mycursor.fetchall()
    return render_template('ghibli.html', movies=myresult)

@app route()