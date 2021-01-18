class ClientClass(object):
	#This is the base class that other classes
	#will adopt from
	def __init__(self, arg):
		self.connected = False
		self.authenticated = False
		self.status = ""
		self.attack = 1
		self.port = arg.port or 8000
		self.certs = ""
		self.pingInterval = 5000
		self.mode = getMode()
		self.uID = ""
		self.body = []
		self.channel = ""

	def getMode(self):
		#Example URI with query params, need to refactor into lib
		#/socket.io/?EIO=4&transport=polling&t=N8hyd7H&sid=lv_VI97HAXpY6yYWAAAC

		if args.mode == 2:
			url = '/socket.io/EIO={}&transport={}'.format(str(4), "transport")
			transport = "websockets"
			pingInterval = 3000
			socket = self.socket
			sid = self.sid
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

	def getUniqueId(self):
		return("[{}:{}]".format(self.uID, self.body))
	