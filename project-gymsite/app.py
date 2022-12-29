import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_Dima'

def get_db_connection():
    conn = sqlite3.connect('C:\\Users\\Andrew\\Desktop\\courses')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/about')
def index():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM Courses').fetchall()
  ##  conn.close()
    return render_template('about.html')
    
@app.route('/')
def home():
   return render_template('about.html')


@app.route('/courses')
def courses():
   conn = get_db_connection()
   result = conn.execute('SELECT * FROM Courses').fetchall()
   conn.close()
   return render_template('courses.html', courses = result)



@app.route('/gallery')
def gallery():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM posts').fetchall()
  ##  conn.close()
    return render_template('gallery.html')

@app.route('/pricing')
def pricing():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM posts').fetchall()
  ##  conn.close()
    return render_template('pricing.html')

