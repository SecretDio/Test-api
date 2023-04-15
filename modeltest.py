from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
import requests
import spacy
nlp=spacy.load("elec_v01/model-best")


app = Flask(__name__)
app.secret_key = "secret"




@app.errorhandler(404)
def page_not_found(e):
    return "404 not found<br><a href='/index'>return to home</a>"



@app.route('/index')
def index():
    nlp=spacy.load("elec_v01/model-best")
 
    address_list = [request.args.get('address',default="Molin Hardware Shop, situated at Royal Road, Union park",  type=str)]

    #address_list = "Molin Hardware Shop, situated at Royal Road, Union park"   
    #Checking predictions for the NER model

    for address in address_list:

        doc=nlp(address)

        ent_list=[(ent.text, ent.label_) for ent in doc.ents]

        output= "Address string -> "+address+"<br>Parsed address -> "+str(ent_list)

    
    return output


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    address_list = {request.form['address']}
    
    for address in address_list:

        doc=nlp(address)

        ent_list=[(ent.text, ent.label_) for ent in doc.ents]

        output= "Address string -> "+address+"<br>Parsed address -> "+str(ent_list)

    
    return output


@app.errorhandler(404)
def page_not_found(e):
    return "404 not found<br><a href='/form'>return to home</a>"