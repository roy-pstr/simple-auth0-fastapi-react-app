from fastapi.testclient import TestClient

def test_ping_route(client: TestClient):
    response = client.get("/debug/ping")
    assert response.status_code == 200
    assert response.json() == "pong"