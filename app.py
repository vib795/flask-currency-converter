from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the list of available currencies
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')  # Assuming USD as a base for fetching the list
    currencies = response.json().get('rates', {}).keys()

    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form.get('amount')
    from_currency = request.form.get('from_currency')
    to_currency = request.form.get('to_currency')

    # Fetch the list of available currencies (for dropdown)
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    currencies = response.json().get('rates', {}).keys()

    # Call the API to get the conversion rate
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    rates = response.json().get('rates', {})

    conversion_rate = rates.get(to_currency, 0)
    converted_amount = float(amount) * conversion_rate if conversion_rate else 0

    # Render the same page with conversion results
    return render_template('index.html', 
                           currencies=currencies, 
                           converted_amount=round(converted_amount, 2), 
                           from_currency=from_currency, 
                           to_currency=to_currency, 
                           amount=amount)
