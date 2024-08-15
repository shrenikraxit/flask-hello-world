from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template('index.html')  # Assuming you have an 'index.html' in the templates folder

@app.route('/send', methods=['POST'])
def send_text():
    try:
        data = request.json
        received_text = data.get('text', '')
        return jsonify({'response': 'Message received'})
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({'response': 'Error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode

