from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/products')
def products():
    return 'Hello, Product Page!'


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
