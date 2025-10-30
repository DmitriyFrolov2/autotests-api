import grpc
from grpc import course_service_pb2_grpc, course_service_pb2

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))

# Выводим полученный ответ
print(f'course_id: "{response.course_id}"')
print(f'title: "{response.title}"')
print(f'description: "{response.description}"')