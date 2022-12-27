import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_Dima'

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@app.route('/about')
def index():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM posts').fetchall()
  ##  conn.close()
    return render_template('about.html')
    
@app.route('/')
def home():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM posts').fetchall()
  ##  conn.close()
    return render_template('about.html')


@app.route('/courses')
def courses():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM posts').fetchall()
  ##  conn.close()
    return render_template('courses.html')

# def homepage():
#   return redirect(url_for('about'))

# @app.route('/home')
# def homepage():
#   return render_template('about.html')
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

