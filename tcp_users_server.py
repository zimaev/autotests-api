import socket


def server():
    # Список для хранения истории сообщений
    messages = []

    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений на localhost:12345")

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode().strip()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        # Добавляем сообщение в историю
        messages.append(data)

        # Отправляем клиенту всю историю сообщений, каждое с новой строки
        client_socket.send('\n'.join(messages).encode())

        client_socket.close()


if __name__ == '__main__':
    server()
