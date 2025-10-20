import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        # Получаем 5 сообщений от сервера
        for i in range(5):
            response = await websocket.recv()
            print(response)

asyncio.run(client())