from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="str",
    last_name="str",
    first_name="str",
    middle_name="str",
)
# Создаст пользователя с помощью метода API клиента PublicUsersClient.create_user
create_user_api_response = public_users_client.create_user(create_user_request)
authentication_user = AuthenticationUserSchema(email=create_user_request.email,
                                               password=create_user_request.password)

# запрос на получение данных о пользователе с использованием PrivateUsersClient.get_user_api
private_users_client = get_private_users_client(authentication_user)
get_user_response = private_users_client.get_user_api(create_user_api_response.user.id)

# Провалидирует JSON schema ответа метода PrivateUsersClient.get_user_api).
get_user_api_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response.json(), schema=get_user_api_response_schema)
