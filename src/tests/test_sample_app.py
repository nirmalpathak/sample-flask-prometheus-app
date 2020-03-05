#!/usr/bin/env python3

# test_sample_app.py
import os
from sample_app import app

def test_hello():
    response = app.test_client().get('/')
    VER = os.environ.get('VERSION')
    HOST = os.uname()[1]

    if VER is None:
        STRING = "Hello World! \n"
    else:
        STRING = "Hello World! Running on Host: " + HOST + " Version: " + VER + "\n"


    assert response.status_code == 200
    assert response.data.decode() == STRING
