from flask import Flask, render_template, request, flash, redirect, Markup
import sys
import os
import glob
import re
import pickle
import numpy as np

app = Flask(__name__)


from werkzeug.utils import secure_filename




diabetespkl=pickle.load(open("diabetesfinalpipeline.pkl","rb"))
heartpkl=pickle.load(open("heartfinalpipeline.pkl","rb"))
kidneypkl=pickle.load(open("kidneyfinalensem.pkl","rb"))
liverpkl=pickle.load(open("liverfinalpipeline.pkl","rb"))



@ app.route('/')
def home():
    return render_template('home.html')




@ app.route('/kidney')
def kidney():
    return render_template('kidney.html')



@ app.route('/liver')
def liver():
    return render_template('liver.html')


@ app.route('/heart')
def heart():
    return render_template('heartml.html')
@ app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')



@app.route("/diabetes_predict", methods = ['POST'])
def diabetespredict():
  
    try:
        if request.method == 'POST':
            int_features=[float(x) for x in request.form.values()]
            final_features=[np.array(int_features)]
            prediction=diabetespkl.predict(final_features)
            if prediction==1:
                return render_template('diabetes.html',prediction_text='you have diabetes')
            else:
                return render_template('diabetes.html',prediction_text='you are fine')
            
    except:
            return render_template("diabetes.html", prediction= 'Please enter valid Data')
    
@app.route("/kidney_predict", methods = ['POST'])
def kidneypredict():
    
    try:
        if request.method == 'POST':
            int_features=[float(x) for x in request.form.values()]
            final_features=[np.array(int_features)]
            prediction=kidneypkl.predict(final_features)
            if prediction==1:
                return render_template('kidney.html',prediction_text='you have kidney related issue')
            else:
                return render_template('kidney.html',prediction_text='you are fine')
            
    except:
        return render_template("kidney.html", prediction= 'Please enter valid Data')
@app.route('/liver_predict', methods=['GET', 'POST'])
def liverpredict():
    
    try:
        if request.method == 'POST':
            int_features=[float(x) for x in request.form.values()]
            final_features=[np.array(int_features)]
            prediction=liverpkl.predict(final_features)
            if prediction==1:
                return render_template('liver.html',prediction_text='you have liver related issue')
            else:
                return render_template('liver.html',prediction_text='you are fine')
            
    except:
        return render_template("liver.html", prediction= 'Please enter valid Data')
@app.route('/heart_predict', methods=['GET', 'POST'])
def heartpredict():
    try:
        if request.method == 'POST':
            int_features=[float(x) for x in request.form.values()]
            final_features=[np.array(int_features)]
            prediction=heartpkl.predict(final_features)
            if prediction==1:
                return render_template('heartml.html',prediction_text='you have heart related issue')
            else:
                return render_template('heartml.html',prediction_text='you are fine')
            
    except:
        return render_template("heartml.html", prediction= 'Please enter valid Data')
if __name__ == '__main__':
    app.run(debug=False)