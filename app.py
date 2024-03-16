from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np

from src.mlReg.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            cut = int(request.form['cut'])
            color = int(request.form['color'])
            clarity = int(request.form['clarity'])
            carat = float(request.form['carat'])
            depth = float(request.form['depth'])
            table = float(request.form['table'])
            x = float(request.form['x'])
            y = float(request.form['y'])
            z = float(request.form['z'])

            data = [cut, color, clarity, carat, depth, table, x, y, z]
            data = np.array(data).reshape(1, -1)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction= str(predict))
        except Exception as e:
            return (f"The Exception Msg Is: {e}")
    



@app.route("/train", methods=['GET', 'POST'])
def training():
    os.system('python main.py')
    return 'Training Successful!'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)