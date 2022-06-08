# Banking Website
from flask import Flask, render_template, request, session, url_for, redirect
from flask.globals import request
from functions import Bank

app = Flask(__name__)
jy = Bank()

@app.route('/')
def index():
    return "Hello! Welcome to the Deposit & Withdrawal Machine"

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = request.form['deposit']
        print(amount)
        add = jy.deposit(amount)
        print(add)
        return render_template('deposit.html')
        # return "The language is".format(amount)
    else:
        return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amount = request.form['withdraw']
        print(amount)
        reduce = jy.withdraw(amount)
        print(reduce)
        return render_template('withdraw.html')
    else:
        return render_template('withdraw.html')

@app.route('/bankloan', methods=['GET', 'POST'])
def bankloan():
    if request.method == 'POST':
        req = request.form
        loanamount = req.get("loanamount")
        rate = req.get("rate")
        period = req.get("period")
        interest = jy.bankloan(loanamount,rate,period)
        print(interest)
        return render_template('bankloan.html')
    else:
        return render_template('bankloan.html')

if __name__ == "__main__":
    app.run(debug=True)