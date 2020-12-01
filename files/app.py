#!/usr/bin/env python3

import json
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_balance():
	data = [
		{"id": 1, "name": "joe", "balance": 10},
		{"id": 2, "name": "bob", "balance": -1},
		{"id": 3, "name": "fred", "balance": 40},
	]

	return json.dumps(data, indent=4)


if __name__ == "__main__":
	app.run()
