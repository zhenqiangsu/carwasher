from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      con = None
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']

         nm = nm.strip()

         if len(nm) == 0:
            raise Exception('Please enter a valid name!')  

         with sql.connect("/var/www/db/database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            con.commit()
            msg = "Record successfully added"

      except Exception as e:
         if con is not None:
            con.rollback()
            con.close()
         msg = str(e)

      finally:
         return render_template("result.html",msg = msg)

@app.route('/list')
def list():
   try:
     con = sql.connect("/var/www/db/database.db")
     con.row_factory = sql.Row
   
     cur = con.cursor()
     cur.execute("select * from students")
     rows = cur.fetchall();
     return render_template("list.html",rows = rows)
   except Exception as e:
     return str(e)

if __name__ == '__main__':
   app.run(debug = True)

