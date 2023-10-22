from flask import Flask,request, render_template
from joblib import load
import numpy as np
import os

img_f = os.path.join('static', 'img')

app = Flask(__name__,template_folder="website")
app.config['UPLOAD_FOLDER'] = img_f

model = load('Final_KNN_Model.pkl')

@app.route('/')
@app.route('/home.html')
def hello():
    home = os.path.join(app.config['UPLOAD_FOLDER'], 'hero.png')
    return render_template("home.html", h = home)


@app.route('/about.html')
def hello_about():
    about = os.path.join(app.config['UPLOAD_FOLDER'], 'about.png')
    team1 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-1.jpg')
    team2 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-2.jpg')
    team3 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-3.jpg')
    
    return render_template("about.html", ab =about,t1 = team1, t2 = team2, t3 = team3)


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