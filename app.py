from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__, static_url_path='/static/css/style.css')


@app.route("/", methods=['GET', 'POST'])
def rain_prediction():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        print(dict(request.form))
        rain_features = dict(request.form).values()
        rain_features = np.array([float(x) for x in rain_features])
        print(rain_features)
        model = pickle.load(open('predict_rain_model_logreg_fix.pkl', 'rb'))
        result = model.predict([rain_features])
        rains = {
            '0': 'Tomorrow Will Not Rain',
            '1': 'Tomorrow Will Rain'
        }
        result = rains[str(result[0])]
        return render_template('index.html', result=result)
    else:
        return "Unsupported Request Method"


if __name__ == '__main__':
    app.run(port=5000, debug=True)

