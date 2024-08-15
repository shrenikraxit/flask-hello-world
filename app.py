from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']   

        return render_template('result.html', number=number)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
