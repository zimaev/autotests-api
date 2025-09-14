from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
import jsonschema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="str",
    last_name="str",
    first_name="str",
    middle_name="str",
)

create_user_api_response = public_users_client.create_user_api(create_user_request)
print('Create user data:', create_user_api_response)
create_user_api_response_schema = CreateUserResponseSchema.model_json_schema()
validate_json_schema(instance=create_user_api_response.json(), schema=create_user_api_response_schema)



# authentication_user = AuthenticationUserSchema(email=create_user_request.email,
#                                                password=create_user_request.password)
#
# private_users_client = get_private_users_client(authentication_user)
# get_user_response = private_users_client.get_user(create_user_api_response.user.id)
# print('Get user data:', get_user_response)
