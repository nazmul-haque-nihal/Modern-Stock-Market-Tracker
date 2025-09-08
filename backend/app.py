from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Alpha Vantage API configuration
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

@app.route('/')
def home():
    return jsonify({"message": "Stock Market Tracker API"})

@app.route('/api/stock/<symbol>')
def get_stock_quote(symbol):
    """Get real-time stock quote"""
    try:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol.upper(),
            'apikey': API_KEY
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if 'Global Quote' in data:
            quote = data['Global Quote']
            return jsonify({
                'symbol': quote['01. symbol'],
                'price': quote['05. price'],
                'change': quote['09. change'],
                'change_percent': quote['10. change percent'],
                'volume': quote['06. volume'],
                'latest_trading_day': quote['07. latest trading day']
            })
        else:
            return jsonify({'error': 'Stock not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Add this new route after the existing routes
@app.route('/api/stock/<symbol>/historical')
def get_historical_data(symbol):
    """Get historical stock data for charting"""
    try:
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol.upper(),
            'apikey': API_KEY
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if 'Time Series (Daily)' in data:
            time_series = data['Time Series (Daily)']
            
            # Get last 30 days of data
            dates = list(time_series.keys())[:30]
            prices = []
            
            for date in dates:
                prices.append(float(time_series[date]['4. close']))
            
            return jsonify({
                'dates': dates[::-1],  # Reverse for chronological order
                'prices': prices[::-1]
            })
        else:
            return jsonify({'error': 'Historical data not available'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Add this route to your backend/app.py
@app.route('/api/stocks/batch', methods=['POST'])
def get_batch_stock_data():
    """Get multiple stock quotes in one request"""
    try:
        data = request.get_json()
        symbols = data.get('symbols', [])
        
        results = []
        for symbol in symbols:
            try:
                params = {
                    'function': 'GLOBAL_QUOTE',
                    'symbol': symbol.upper(),
                    'apikey': API_KEY
                }
                response = requests.get(BASE_URL, params=params)
                quote_data = response.json()
                
                if 'Global Quote' in quote_data:
                    quote = quote_data['Global Quote']
                    results.append({
                        'symbol': quote['01. symbol'],
                        'price': quote['05. price'],
                        'change': quote['09. change'],
                        'change_percent': quote['10. change percent'],
                        'volume': quote['06. volume'],
                        'latest_trading_day': quote['07. latest trading day']
                    })
            except Exception as e:
                # Skip individual stock if there's an error
                continue
                
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)