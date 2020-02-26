# test_sample_app.py
from sample import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    #assert response.data == b'Hello, World!'
    #assert response.data == b'Hello World!'
    #assert response.data == b'"Hello World! Running on Host: " + HOST + " Version: " + VER + "\n"'
