from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
# def predict(x): #w1x+w0

with open("model.pkl", "rb") as f:
    w0,w1 = pickle.load(f)
    

    # return y
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    y=0
    if request.method == 'POST':
        name = request.form['name']
        n=int(name)
        y=w1*n+w0
        # y=predict(n)
        return f'Price:, {y}!'
    return render_template('index.html', Y=y)
                           

if __name__ == '__main__':
    app.run()
