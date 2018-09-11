from flask import Flask, render_template, request, redirect, Response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # run!
    app.run(host= '0.0.0.0')