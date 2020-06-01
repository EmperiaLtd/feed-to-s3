import json

import pytest

from src.eventbridge_function import app


@pytest.fixture()
def eventbridge_event():
    """ Generates EventBridge Event"""

    return {
        "version": "0",
        "id": "7507af39-d274-390b-d951-1b5a3a1bd2cc",
        "detail-type": "myDetailType",
        "source": "com.mycompany.myapp",
        "account": "123456789012",
        "time": "2020-05-12T01:53:46Z",
        "region": "us-west-2",
        "resources": [
            "resource1",
            "resource2"
        ],
        "detail": {
            "key1": "value1",
            "key2": "value2"
        }
    }


def test_lambda_handler(eventbridge_event, mocker):

    ret = app.lambda_handler(eventbridge_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "event received"
