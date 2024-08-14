from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask server is running"

@app.route('/send', methods=['POST'])
def send_text():
    data = request.json
    received_text = data.get('text', '')
    response_text = f"Server received: {received_text}"
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
