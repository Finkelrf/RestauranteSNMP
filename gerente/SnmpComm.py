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
		table = Table(tableId,9,9,TableStatusEnum.Occupied)
		print "SnmpComm refreshing table OBJ"
		return table

	@staticmethod
	def setTable(tableObj):
		#change tableObj on agente
		print "SnmpComm Updating table OBJ"

	@staticmethod
	def _executeCmd(cmd):
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		return proc.stdout.read()

	@staticmethod
	def walk(OID):
		#Return numberOfObjects,arrayOfValues.
		print "SnmpCommWalk "+OID
		arrayOfValues = []
		numberOfObjects = 50
		return numberOfObjects,arrayOfValues
	@staticmethod
	def get(OID):
		#Return value of requested OID
		value = 5 #dummy value for examples
		return value

	@staticmethod
	def set(OID,inputValue):
		#Return value of requested OID
		value = 5 #dummy value for examples
		return value




class TableStatusEnum:
	Free,Occupied,Reserved,Unavailable = range(4)


class Table(object):
	def __init__(self,id,capacity,clients,status):
		self.id = id
		self.capacity = capacity
		self.clients = clients
		self.status = status

	def getStatusStr(self):
		dict = {TableStatusEnum.Free: 'Free', TableStatusEnum.Occupied: 'Occupied', TableStatusEnum.Reserved: 'Reserved', TableStatusEnum.Unavailable: 'Unavailable'}
		return dict[self.status]
