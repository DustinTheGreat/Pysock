import socketio

class SocketIO(socketio.ClientNamespace):
	#This is the base class that other classes
	#will adopt from
	def __init__(self):
		self.connected = False
		self.authenticated = False
		self.status = ""
		self.attack = 1
		self.port = 8000
		self.certs = ""
		self.pingInterval = 5000
		self.mode = ""
		self.uID = ""
		self.body = []
		self.channel = ""

	async def on_connect(self):
		try:
			await sio.connect('http://localhost:5000')
			self.connected = True
		
		except:
			self.connected = False




		

	def on_disconnect(self):
		self.connected = False

	async def on_my_event(self, data):
			await self.emit('my_response', data)
			

		# Upon connection, the server assigns the client a unique session identifier. 
		# The applicaction can find this identifier in the sid attribute


if __name__ == "__main__":
	sio = socketio.AsyncClient()
	test = SocketIO()
	print(test.pingInterval)
#Find time and factor this in, SocketIO sucking fucking ass and is incompatible with other versions
#this is for V2

# from socketIO_client_nexus import SocketIO, BaseNamespace


# def on_aaa_response(*args):
#         print('[Trying to join a specified room...')
# 				SocketIO.emit('join', {'channel': '3809A4000011h7EXbbWXWugKo'}, )

# def on_bbb_response(*args):
#         print('Just emitted bbb...')





# with SocketIO("https://.com",verify=False) as SocketIO:
#         print("conencted")
#         SocketIO.on('reqIdentity', on_aaa_response)
#         SocketIO.wait()


