from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<fahrenheit>')
def convert(fahrenheit=""):
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return f"Fahrenheit is:{fahrenheit} Celsius is:{celsius:.2f}"


if __name__ == '__main__':
    app.run()
