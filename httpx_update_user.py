import httpx

from tools.fakers import get_random_email

# Создаем пользователя
print("********************** CREATE USER Создаем пользователя **********************\n")
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
print("********************** LOGIN Проходим аутентификацию **********************\n")
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login user data:', login_response_data)

print("********************** UPDATE Обновить пользователя **********************\n")
# Обновить пользователя
update_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
token = login_response.json()["token"]["accessToken"]
headers = {"Authorization": f"Bearer {token}"}
update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
                              json=update_user_payload)
update_response_data = login_response.json()
print('Update user data:', login_response_data)
