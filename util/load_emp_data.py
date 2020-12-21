import json


def load_data():
    with open('./model/emp_data.json', mode='r') as f:
        return json.load(f)


data = load_data()
