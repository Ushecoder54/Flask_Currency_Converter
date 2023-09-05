from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key from ExchangeRate-API
API_KEY = '8cbf3cd6a8d1df81a4560ce9'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['fromCurrency']
    to_currency = request.form['toCurrency']

    # Make an API request to get the exchange rate
    api_url = f'https://v6.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][to_currency]
        converted_amount = round(amount * rate, 2)
        return jsonify({'result': converted_amount})
    else:
        return jsonify({'error': 'Failed to fetch exchange rate'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
