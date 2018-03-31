from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return "Hello World!! Test App"

@app.route('/about')
def about():
    return "About Yora"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True, port=3000)