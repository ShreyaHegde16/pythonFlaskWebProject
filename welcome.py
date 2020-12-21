from flask import Flask, jsonify, abort
from util.load_emp_data import data

from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to my webapp:" + str(datetime.now())


@app.route("/api/v1/employees")
def get_employees():
    return jsonify(data)


@app.route("/api/v1/employees/<int:emp_index>")
def get_employees_by_id(emp_index):
    try:
        return data[emp_index]
    except IndexError:
        abort(404)
