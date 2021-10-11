import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_bin='model1.bin'
dv_bin = 'dv.bin'


with open(model_bin, 'rb') as model_bin:
    model = pickle.load(model_bin)

with open(dv_bin, 'rb') as dv_bin:
    dv = pickle.load(dv_bin)

app = Flask('churn')


@app.route('/predict', methods=['POST'] )

def predict():
    customer = request.get_json()

    X_customer = dv.transform([customer])
    churn_proba = model.predict_proba(X_customer)[0, 1]
    churn = churn_proba >= 0.5

    result = {
        'churn_probability': float (churn_proba),
        'churn': bool(churn)
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port=9696)



