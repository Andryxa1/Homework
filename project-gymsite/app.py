import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_Dima'

def get_db_connection():
    conn = sqlite3.connect('C:\\Users\\Andrew\\Python\\project-gymsite\\courses.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/about')
def index():
 ##   conn = get_db_connection()
  ##  result = conn.execute('SELECT * FROM Courses').fetchall()
  ##  conn.close()
    return render_template('about.html')



@app.route('/contact.html')
def zayavka():
   conn = get_db_connection()
   result = conn.execute('SELECT * FROM Courses').fetchall()
   conn.close()
   return render_template('zayavka.html', abonements = result)



@app.post('/save-contact')
def save_zayavka():
   

    #print("CONNECTED")
    client_name = request.form['client_name']
    print(client_name)
    
    client_lastname = request.form.get('client_lastname')
    print(client_lastname)

    client_phone = request.form.get('phone')
    print(client_phone)

    abonement_id = request.form.get('abonement')
    print(abonement_id)

    conn = get_db_connection()
    result = conn.execute("insert into zayavky (client_name, last_name, phone, abonement_id) values (?, ?, ?, ?)", (client_name, client_lastname, client_phone, abonement_id))
    conn.commit()
    conn.close()

    client_info = [client_name, client_lastname]

    return render_template('zayavka_save.html', client = client_name)



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
   conn = get_db_connection()
   result = conn.execute('SELECT * FROM Pricing').fetchall()
   conn.close()
   return render_template('pricing.html', courses = result)

