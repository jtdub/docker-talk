#!/usr/bin/env python

import json
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def accounts():
	return json.dumps(requests.get('http://ntc1:5000').json(), indent=2)


if __name__ == "__main__":
	app.run()
