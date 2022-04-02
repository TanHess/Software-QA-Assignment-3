# Tanner Hess
# tmh648
# Software Testing Q & A: Assignment 3

import pytest
from app import create_app




# =================================Fixtures=================================
@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client


# =================================Tests=================================
# Ensures webapp working
def test_home_exists(client):
    res = client.get("/")
    assert res.status_code == 200


# Uses test cause for normal weght to ensure the functionality still works in the webapp
def test_bmi_interface(client):
    data=dict(feet='5', inches='5', weight='123')

    response = client.post("/", data=data)
    assert b"<h4 align=\"center\">Your BMI: 21.0 </h4>" in response.data