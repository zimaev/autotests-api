from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_exercises_client
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Создать пользователя с помощью метода клиента
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="str",
    lastName="str",
    firstName="str",
    middleName="str",
)

create_user_api_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_api_response)

authentication_user = AuthenticationUserDict(email=create_user_request["email"],
                                             password=create_user_request["password"])

# Загрузить файл
files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)

# Создать курс
courses_client = get_courses_client(authentication_user)
create_course_request = CreateCourseRequestDict(title="Python",
                                                maxScore=100,
                                                minScore=1,
                                                description="test description",
                                                estimatedTime="2 weeks",
                                                previewFileId=create_file_response["file"]["id"],
                                                createdByUserId=create_user_api_response["user"]["id"])

create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создать задание
create_exercise_request = CreateExerciseRequestDict(
    title="Python",
    courseId=create_course_response["course"]["id"],
    maxScore=100,
    minScore=1,
    orderIndex=1,
    description="test description",
    estimatedTime="2 weeks"
)
exercise_client = get_exercises_client(authentication_user)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
