# Banking Website
from flask import Flask, render_template, request, session, url_for, redirect
from flask.globals import request
from functions import Bank

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Welcome to the Deposit & Withdrawal Machine"

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = request.form['deposit']
        Bank(deposit)
        return render_template('deposit.html')
        # return "The language is".format(amount)
    else:
        return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amount = request.form['withdraw']
        return render_template('withdraw.html')
    else:
        return render_template('withdraw.html')

if __name__ == "__main__":
    app.run(debug=True)