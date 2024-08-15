from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This is just for testing, remove later

@app.route('/send_number', methods=['POST'])
def send_number():
    number = request.form['number']
    # Process the number here (e.g., store it, display it)
    return render_template('result.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
