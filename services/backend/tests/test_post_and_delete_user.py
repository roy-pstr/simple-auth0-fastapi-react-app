import time
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

mark_parametrize = [
    (
        {
            "email": f"user_{str(uuid4())[-8:]}@example.com",
            "password": "secret234!@#$!@",
            "given_name": "string",
            "family_name": "string",
            "name": "string",
        },
        200
    ),
    (
        {
            "email": f"user_{str(uuid4())[-8:]}@example.com",
            "password": "this_is_weak_password",
            "given_name": "string",
            "family_name": "string",
            "name": "string",
        },
        400
    ),
    (
        {
            "email": f"unvalid_email_address",
            "password": "secret234!@#$!@",
            "given_name": "string",
            "family_name": "string",
            "name": "string",
        },
        422
    ),
]
@pytest.mark.parametrize("user_data,expected_status_code", mark_parametrize)
def test_user_signup_and_remove(user_data: dict, expected_status_code: int, test_client_auth: TestClient):
    response = test_client_auth.post("/user", json=user_data)
    if response.status_code != expected_status_code:
        print(response.text)
    if expected_status_code == 200:            
        response.raise_for_status()
        user_id = response.json()["user_id"]
        assert user_id != None
        time.sleep(2) # it takes time for the roles to be updated after create user in auth0.
        response = test_client_auth.delete(f"/user/{user_id}")
        if response.status_code != 200:
            print(response.text)
        assert response.status_code == 200