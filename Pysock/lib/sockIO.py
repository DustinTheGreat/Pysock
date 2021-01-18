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




