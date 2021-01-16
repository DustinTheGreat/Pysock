class ClientClass(object):
	#This is the base class that other classes
	#will adopt from
	def __init__(self, arg):
		self.connected = False
		self.authenticated = False
		self.status = ""
		self.attack = 1
		self.port = arg.port || 8000
		self.certs = ""
		self.pingInterval = 5000
		self.mode = getMode()

	def getMode(self):
		if args.mode = 2:
			url = '/socket.io/'
			transport = "websockets"
			pingInterval = 3000
			sid = ""
		else:
			self.mode = 1
			#barebone instead of socketio
	def changeHeaders(self):
		pass

	def adjustInterval(self, pt):
		self.pingInterval = pt
		return

	def connect(self):
		self.connected = True

	def autheticate(self):
		self.autheticated = True