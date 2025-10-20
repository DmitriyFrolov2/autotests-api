# autotests-api

Запустите сервер командой:

`python -m grpc_course_server`

Запустите клиент командой:

`python -m grpc_course_client`


Запуск сервера websocket

`python -m websocket_users_server`

// Создаём подключение к WebSocket-серверу по адресу ws://localhost:8765
const websocket = new WebSocket("ws://localhost:8765")

// Добавляем обработчик входящих сообщений от сервера
websocket.onmessage = (message) => console.log(`Получили сообщение от сервера: "${message.data}"`)