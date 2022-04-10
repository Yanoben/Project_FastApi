import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_all_users():
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
        response = await ac.get("/users")
    assert response.status_code == 200


# from fastapi.testclient import TestClient

# from main import app

# client = TestClient(app)


# def test_read_main():
#     response = client.get("/apples")
#     assert response.status_code == 200


# def test_read_users():
#     response = client.get("/users")
#     assert response.status_code == 200


# def test_read_user():
#     response = client.get("/users/1")
#     assert response.status_code == 200


# def test_create_user():
#     response = client.post(
#         "/users",
#         json={
#             "name": "test",
#             "email": "test@example.com",
#             "role": "buyer",
#             "password": "testtesttest",
#             "password2": "testtesttest"
#             })
#     assert response.status_code == 200


# def test_get_apples():
#     response = client.get("/apples")
#     assert response.status_code == 200
