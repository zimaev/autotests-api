from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

# Создать пользователя с помощью метода клиента
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(email=get_random_email(),
                                              password="str",
                                              last_name="str",
                                              first_name="str",
                                              middle_name="str")

create_user_api_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_api_response)

authentication_user = AuthenticationUserSchema(email=create_user_request.email,
                                               password=create_user_request.password)

# Загрузить файл
files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)

# Создать курс
courses_client = get_courses_client(authentication_user)
create_course_request = CreateCourseRequestSchema(title="Python",
                                                  max_score=100,
                                                  min_score=1,
                                                  description="test description",
                                                  estimated_time="2 weeks",
                                                  preview_file_id=create_file_response.file.id,
                                                  created_by_user_id=create_user_api_response.user.id)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создать задание
create_exercise_request = CreateExerciseRequestSchema(title="Python",
                                                      courseId=create_course_response.course.id,
                                                      max_score=100,
                                                      min_score=1,
                                                      order_index=1,
                                                      description="test description",
                                                      estimated_time="2 weeks")
exercise_client = get_exercises_client(authentication_user)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
