from fastapi.testclient import TestClient

def test_me(client: TestClient, headers_with_authorization: dict):
    response = client.get("/me", headers=headers_with_authorization)
    if response.status_code != 200:
        print(response.text)
    assert response.status_code == 200