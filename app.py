from flask import Flask,render_template,url_for,request
import numpy as np
import pandas as pd
import os
import pickle
model = pickle.load(open('capston_rf.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index1.html',title='Home')

@app.route('/predict',methods=['POST'])
def predict():
    '''For rendering results on HTML GUI
    '''
    Gender = request.form['Gender']
    Age = request.form['Age']
    Driving_License  = request.form['Driving_License']
    Region_Code = request.form['Region_Code']
    Previously_Insured =request.form['Previously_Insured']
    Vehicle_Age = request.form['Vehicle_Age']
    Vehicle_Damage = request.form['Vehicle_Damage']
    Annual_Premium = request.form['Annual_Premium']
    Policy_Sales_Channel = request.form['Policy_Sales_Channel']
    Vintage = request.form['Vintage']

    pred = pd.DataFrame(data={'Gender':[float(Gender)],'Age':[float(Age)] ,'Driving_License':[float(Driving_License)],'Region_Code':[float(Region_Code)],
                       'Previously_Insured':[float(Previously_Insured)],'Vehicle_Age':[float(Vehicle_Age)],'Vehicle_Damage':[float(Vehicle_Damage)]
                       ,'Annual_Premium': [float(Annual_Premium)],'Policy_Sales_Channel': [float(Policy_Sales_Channel)],'Vintage': [float(Vintage)]})
    prediction = model.predict(pred)
    output = prediction[0] 
    if output > 0:
        output="Genuine"
        return render_template('prediction.html', prediction_text=f'Prediction For Applied Person is {output} Person.')
    else:
        output = "Fraud"
        return render_template('prediction.html', prediction_text=f'Prediction For Applied Person is {output} Person!!')
   
port = int(os.environ.get('PORT',5000))
if __name__ == "__main__":
    app.run(debug=1,host='0.0.0.0',port=port) # or True             
