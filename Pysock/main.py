#!/usr/bin/env python3
import asyncio
import pathlib
import ssl
import websockets
import cli






# async def consumer_handler(websocket, path):
#     async for message in websocket:
#         await consumer(message)






# async def producer_handler(websocket, path):
#     while True:
#         message = await producer()
#         await websocket.send(message)








async def connection(url):
	port = "5678"
	uri = "ws://{}:{}".format(url, port)
	async with websockets.connect(uri) as websocket:
		##add the dictonary that you want to test against
		name = input("Im in")

		await websocket.send(name)
		print(f"> {name}")

		greeting = await websocket.recv()
		print(f"< {greeting}")



	
async def main(url):
	print("Starting...")
	await connection(url)
	print("Finishing")


if __name__ == "__main__":
	# import cli runner
	args = cli.main()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main(args))
	# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
	# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
	# ssl_context.load_verify_locations(localhost_pem)	
