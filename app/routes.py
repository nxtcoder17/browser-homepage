from app import app
from flask import render_template, send_file
from app import models

@app.route ('/')
def index():
    return render_template ("index.html", 
                    cp_sites = models.cp_sites(),
                    study_sites = models.study_sites(),
                    linux_sites = models.linux_sites())

@app.route ('/favicon.ico')
def favicon():
    return send_file ('./static/images/ab.jpg', mimetype='image/jpg')
