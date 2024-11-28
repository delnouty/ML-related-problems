from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

def predict_expenses(data):
    significant_coefficients = {
        "Intercept": 13041.15169847328,
        "age": 3031.133367457519,
        "bmi": 462.8933240358457,
        "children": 666.8734098322169,
        "smoker": 5165.31080344811,
        "region": -277.93606962268314,
        "heavyCase": 6057.491938649431
    }
    prediction = significant_coefficients["Intercept"]
    for key in data:
        prediction += significant_coefficients[key] * data[key]
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        "age": float(request.form['age']),
        "bmi": float(request.form['bmi']),
        "children": int(request.form['children']),
        "smoker": int(request.form['smoker']),
        "region": int(request.form['region']),
        "heavyCase": int(request.form['heavyCase'])
    }
    predicted_expense = predict_expenses(data)
    return render_template('result.html', predicted_expense=predicted_expense)

if __name__ == '__main__':
    app.run(debug=True)
