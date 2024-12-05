from fastapi.testclient import TestClient
from app.routes import app

client = TestClient(app)

def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
