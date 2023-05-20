from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/home/', methods=['POST', 'GET'])
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print(url_for('home'))
    print(url_for('static', filename='style.css'))