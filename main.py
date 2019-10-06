from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.js')
def index_js():
    return render_template('src/index.js')

if __name__ == '__main__':
    app.run(debug=True)