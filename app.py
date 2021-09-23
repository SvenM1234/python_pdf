import re
from flask import Flask
from flask import render_template, request
from livereload import Server
import os
from datetime import datetime




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
    print(request.files)
    for file in request.files.getlist('resume'):
        print(file)
        print(file.headers.get('Content-Disposition').split(';')[2].split("=")[1].replace('"',''))
        # name + datetime : 
        # file.headers.get('Content-Disposition').split(';')[2].split("=")[1].replace('"','')) + "_" + str(datetime.now())
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(file.headers.get('Content-Disposition').split(';')[2].split("=")[1].replace('"','')) + "_" + str(datetime.now())).replace(" ", "_").replace(":", "_")+".pdf")

    return render_template('traitement_pdf.html')


