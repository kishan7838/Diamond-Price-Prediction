from flask import Flask,request, render_template
from joblib import load
import numpy as np

app = Flask(__name__,template_folder="website")

model = load('Final_KNN_Model.pkl')


@app.route('/home.html')
def hello():
    return render_template("home.html")


@app.route('/about.html')
def hello_about():
    return render_template("about.html")

@app.route('/')
@app.route('/price.html')
def hello_price():
    return render_template("price.html")

@app.route('/contact.html')
def hello_contact():
    return render_template("contact.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    data1= request.form['a']
    data2= request.form['b']
    data3= request.form['c']
    data4= request.form['d']
    data1= float(data1)
    data2= float(data2)
    data3= int(data3)
    data4= int(data4)
    arr=np.array([[data1,data2,data3,data4]])
    pred=model.predict(arr)
    output = round(pred[0],2)
    return render_template('price.html', data=f"Price of the diamond according to the features you entered is {output}.")


if __name__ == '__main__':
    app.run(debug=True)