from fastapi.testclient import TestClient

def test_ping_route(client: TestClient):
    response = client.get("/debug/ping")
    assert response.status_code == 200
    assert response.json() == "pong"

def test_private(test_client_auth: TestClient):
    response = test_client_auth.get("/debug/private")
    if response.status_code != 200:
        print(response.text)
    assert response.status_code == 200
        
def test_private_scoped(test_client_auth: TestClient):
    response = test_client_auth.get("/debug/private-scoped")
    if response.status_code != 200:
        print(response.text)
    assert response.status_code == 200