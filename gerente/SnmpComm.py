from random import randint
import subprocess 

class SnmpComm(object):
	MIBDIRS = "/lib/mibs:/usr/share/mibs/ietf:/usr/share/mibs/netsnmp:/usr/share/snmp/mibs/"
	IPADDR = "localhost"
	@staticmethod
	def getSnmpVar(variableName):
		if variableName == "lotAtual":
			return "9"
		elif variableName == "capacidade":
			return "30"
		else:
			return "var not found"

	@staticmethod
	def getTableStatus(tableId):
		return randint(0,3)

	@staticmethod
	def getTable(tableId):
		table = Table(tableId,9,9,TableStatusEnum.Ocupy)
		return table

	@staticmethod
	def setTable(tableObj):
		#change tableObj on agente
		print "Updating table"

	@staticmethod
	def _executeCmd(cmd):
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		return proc.stdout.read()


class TableStatusEnum:
	Free,Ocupy,Reserved,Unavailable = range(4)


class Table(object):
	def __init__(self,id,capacity,clients,status):
		self.id = id
		self.capacity = capacity
		self.clients = clients
		self.status = status

	def getStatusStr(self):
		dict = {TableStatusEnum.Free: 'Free', TableStatusEnum.Ocupy: 'Ocupy', TableStatusEnum.Reserved: 'Reserved', TableStatusEnum.Unavailable: 'Unavailable'}
		return dict[self.status]
