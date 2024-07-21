from flask import Flask, render_template, request, jsonify
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_npv', methods=['POST'])
def calculate_npv():
    initial_investment = float(request.form['initial_investment'])
    cash_flows = list(map(float, request.form['cash_flows'].split(',')))
    discount_rate = float(request.form['discount_rate']) / 100

    npv = calculate_npv_value(initial_investment, cash_flows, discount_rate)
    return jsonify({'npv': npv})

def calculate_npv_value(initial_investment, cash_flows, discount_rate):
    npv = -initial_investment
    for i, cash_flow in enumerate(cash_flows):
        npv += cash_flow / ((1 + discount_rate) ** (i + 1))
    return npv

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
