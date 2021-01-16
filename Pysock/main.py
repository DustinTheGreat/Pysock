#!/usr/bin/env python3
import asyncio
import pathlib
import ssl
import websockets







# async def consumer_handler(websocket, path):
#     async for message in websocket:
#         await consumer(message)






# async def producer_handler(websocket, path):
#     while True:
#         message = await producer()
#         await websocket.send(message)








async def connection():
	uri = "ws://localhost:5678"
	async with websockets.connect(uri) as websocket:
		##add the dictonary that you want to test against
		name = input("Im in")

		await websocket.send(name)
		print(f"> {name}")

		greeting = await websocket.recv()
		print(f"< {greeting}")



	
async def main():
	print("Starting...")
	await connection()
	print("Finishing")


if __name__ == "__main__":
	# import cli runner
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
	# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
	# ssl_context.load_verify_locations(localhost_pem)	
