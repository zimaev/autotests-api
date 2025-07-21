import httpx

payload = {
    "email": "user@example.com",
    "password": "admin"
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)

token = response_login.json()["token"]["accessToken"]
headers = {"Authorization": f"Bearer {token}"}
response_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response_me.status_code)
print(response_me.json())
