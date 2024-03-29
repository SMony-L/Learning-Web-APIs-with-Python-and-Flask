
from flask import Flask, request, jsonify

from app import app
from app.model.expense import Expense, ExpenseSchema
from app.model.income import Income, IncomeSchema
from app.model.transaction_type import TransactionType



transactions = [
    Income('Salary', 5000), Income('Dividends', 200), Expense('Pizza', 50), Expense('Rock Concert', 100)
]

@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(filter(lambda t: t.type == TransactionType.INCOME, transactions))
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return request.get_json(), 201

@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(filter(lambda t: t.type == TransactionType.EXPENSE, transactions))
    
    return jsonify(expenses)

@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return request.get_json(), 201