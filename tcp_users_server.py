import socket


def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сервер к localhost и порту 12345
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Устанавливаем очередь в 10 подключений
    server_socket.listen(10)
    print('Сервер запущен и ждет подключений...')

    # Список для хранения всех сообщений
    messages = []

    while True:
        # Принимаем новое подключение
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        try:
            # Получаем сообщение от клиента
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

                # Добавляем сообщение в историю
                messages.append(data)

                # Отправляем клиенту всю историю сообщений
                response = '\n'.join(messages)
                client_socket.send(response.encode())

        except Exception as e:
            print(f"Ошибка при обработке клиента {client_address}: {e}")

        finally:
            # Закрываем соединение с клиентом
            client_socket.close()


if __name__ == '__main__':
    server()