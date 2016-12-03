from random import randint
import subprocess 

class SnmpComm:
	MIBDIRS = "/lib/mibs:/usr/share/mibs/ietf:/usr/share/mibs/netsnmp:/usr/share/snmp/mibs/ "
	IPADDR = " localhost "
	cmdParameters = "-c public -v2c "
	mib = "-mRestCtrl-MIB "
	SNMP_PARAMETERS = " -v1 -cpublic localhost "
	# SNMP_PARAMETERS = IPADDR+cmdParameters+MIBDIRS+mib
	varNames = ["Integer32:","Counter32:"]
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
	def executeCmd(cmd):
		cmdList = cmd.split(" ")
		print cmdList
		proc = subprocess.Popen(cmdList, stdout=subprocess.PIPE)
		return proc.stdout.read()

	@staticmethod
	def walk(OID):
		#Return numberOfObjects,arrayOfValues.
		cmdString = "snmpwalk"+SnmpComm.SNMP_PARAMETERS+OID
		print cmdString
		cmdOutput = SnmpComm.executeCmd(cmdString)
		n,listOfResp = SnmpComm.parseResponse(cmdOutput)
		return n,listOfResp
	@staticmethod
	def get(OID):
		#Return value of requested OID
		cmdString = "snmpget"+SnmpComm.SNMP_PARAMETERS+OID
		cmdOutput = SnmpComm.executeCmd(cmdString)
		n,listOfResp = SnmpComm.parseResponse(cmdOutput)
		return listOfResp[0]

	@staticmethod
	def set(OID,inputValue):
		#Return value of requested OID
		cmdString = "snmpset"+SnmpComm.SNMP_PARAMETERS+OID
		cmdOutput = SnmpComm.executeCmd(cmdString)
		n,listOfResp = SnmpComm.parseResponse(cmdOutput)
		return listOfResp[0]

	@staticmethod
	def parseResponse(inputString):
		retString = []
		#check for error 
		errMsg = "No Such Object available"
		if inputString.find(errMsg) != -1:
			print "Error found"
			return -1,retString
		#break into lines
		line = inputString.split("\n")
		numOfResp = len(line)
		#find a variable type
		for i in range(0,numOfResp):
			for j in range(0,len(SnmpComm.varNames)):
				#compare with a list of variables
				if line[i].find(SnmpComm.varNames[j]) != -1: 
					break
			if j == len(SnmpComm.varNames[j]):
				#variable is from a unknown type
				print "variable is from a unknown type"
				return -1,retString
			else:
				index = line[i].find(SnmpComm.varNames[j]) + len(SnmpComm.varNames[j])
				retString.append(line[i][index:])

		return numOfResp,retString







		#get value from after variableType
		print "remove that"




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
