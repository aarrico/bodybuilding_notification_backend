import os
import tempfile

import pytest

from flaskr import flaskr


@pytest.fixture
def client():
    flaskr.app.config["TESTING"] = True

    with flaskr.app.test_client() as client:
        with flaskr.app.app_context():
            pass
        yield client


def test_empty_db(client):
    rv = client.get("/")
    assert rv.data == ""
