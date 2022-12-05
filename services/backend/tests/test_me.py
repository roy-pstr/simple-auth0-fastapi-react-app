from fastapi.testclient import TestClient

def test_me(test_client_auth: TestClient):
    response = test_client_auth.get("/user/me")
    if response.status_code != 200:
        print(response.text)
    assert response.status_code == 200