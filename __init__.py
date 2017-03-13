from flask import Flask, render_template, request, flash
from carwasher.forms import ContactForm
app = Flask(__name__)
import carwash.views

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         return render_template('success.html')
   elif request.method == 'GET':
         return render_template('contact.html', form = form)

@app.route("/hello")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)
