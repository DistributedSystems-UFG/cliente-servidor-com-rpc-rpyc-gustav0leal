import rpyc
from const import *
from rpyc.utils.server import ForkingServer

class calculator(rpyc.Service):
	def exposed_add(self, a, b):
		return a+b
	
	def exposed_subtract(self, a, b):
		return a-b
	
	def exposed_multiply(self, a, b):
		return a*b

	def exposed_divide(self, a, b):
		return a/b

if __name__ == "__main__":
	server = ForkingServer(calculator(),port = PORT)
	server.start()