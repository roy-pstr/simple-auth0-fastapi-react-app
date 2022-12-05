import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.core.config import get_settings

@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture(scope="session")
def headers_with_authorization(client: TestClient):
    settings = get_settings()
    response = client.post(
        "/token",
        data={"username": settings.AUTH0_TEST_USERNAME, "password": settings.AUTH0_TEST_PASSWORD},
    )
    response.raise_for_status()
    access_token = response.json().get("access_token")
    return {"Authorization": f"Bearer {access_token}"}

@pytest.fixture(scope="session")
def test_client_auth(headers_with_authorization: dict):
    with TestClient(app) as test_client:
        test_client.headers = headers_with_authorization
        yield test_client