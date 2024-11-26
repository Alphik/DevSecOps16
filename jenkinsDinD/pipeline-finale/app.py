from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import random

@app.route('/', methods=['GET'])
def guess_number():
  return "hello tic tac toe", 201

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)