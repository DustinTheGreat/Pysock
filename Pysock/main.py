#!/usr/bin/env python3
import asyncio
import pathlib
import ssl
import websockets


async def main(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f" {name}!"

    await websocket.send(payload)
    print(f"> {paylaod}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
	main()