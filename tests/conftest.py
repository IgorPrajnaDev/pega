import pytest
from fastapi.testclient import TestClient

from pega.app import app


@pytest.fixture
def client():
    return TestClient(app)
