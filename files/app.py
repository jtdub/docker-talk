#!/usr/bin/env python3

import json
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_balance():

	with open("./data/data.json") as f:
		data = json.loads(f.read())

	return json.dumps(data, indent=4)


if __name__ == "__main__":
	app.run()
