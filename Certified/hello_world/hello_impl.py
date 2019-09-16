# Copyright 2020 BlueCat Networks. All rights reserved.
from flask import jsonify
from bluecat import route
from main_app import app

@route(app, "/hello_world/say")
hello():  # missing keyword `def`
    return jsonify({"message": "Hello, World!"})
