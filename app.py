from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
