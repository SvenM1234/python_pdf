import re
from flask import Flask
from flask import render_template, request
from livereload import Server
import os



app = Flask(__name__)
app.config.from_pyfile('config.py')

# print(app.config)

@app.route('/')
def hello():
    
    return render_template('index.html')

    

@app.route('/accueil')
def accueil():

    return render_template('index.html')


@app.route('/pdf', methods = ['POST'])
def pdf():

    print(request.form)
    print(request.files)

    request.files["tex"].save(os.path.join(app.config['UPLOAD_FOLDER'],"tex.pdf"))

    return render_template('traitement_pdf.html')


