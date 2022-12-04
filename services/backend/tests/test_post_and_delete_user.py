import pytest
import time
from fastapi.testclient import TestClient

mark_parametrize = [
    (
        {
            "email": "user@example.com",
            "password": "secret234!@#$!@",
            "given_name": "string",
            "family_name": "string",
            "name": "string",
        }
    ),
]
@pytest.mark.parametrize("user_data", mark_parametrize)
def test_user_signup_and_remove(user_data: dict, test_client_auth: TestClient):
    response = test_client_auth.post("/user", json=user_data)
    if response.status_code != 200:
        print(response.text)
    response.raise_for_status()
    user_id = response.json()["user_id"]
    assert user_id != None
    time.sleep(2) # it takes time for the roles to be updated after create user in auth0.
    response = test_client_auth.delete(f"/user/{user_id}")
    if response.status_code != 200:
        print(response.text)
    assert response.status_code == 200