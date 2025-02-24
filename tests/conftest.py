import pytest

@pytest.fixture()
def client(app):
    return app.test_client()