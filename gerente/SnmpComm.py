from random import randint
import subprocess 

class SnmpComm:
	MIBDIRS = "-M/lib/mibs:/usr/share/mibs/ietf:/usr/share/mibs/netsnmp:/usr/share/snmp/mibs/:/usr/local/share/snmp/mibs "
	IPADDR = " 192.168.1.11 "
	cmdParameters = "-c public -v2c "
	mib = "-mRestCtrl-MIB "
	#SNMP_PARAMETERS = " -v1 -cpublic localhost "
	SNMP_PARAMETERS = IPADDR+cmdParameters+MIBDIRS+mib
	SNMP_PARAMETERS_SET = "-c private -v2c "+MIBDIRS+"-mRestCtrl-MIB"+IPADDR
	varNames = ["Integer32:","Counter32:","INTEGER:","STRING:","Gauge32:","Timeticks:","IpAddress"]
	statusDict = {0: "livre(0)",1: "ocupada(1)",2: "reservada(2)",3: "indisponivel(3)"}



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
		table = Table(SnmpComm.get("mesasEntry.1."+str(tableId)),SnmpComm.get("mesasEntry.2."+str(tableId)),SnmpComm.get("mesasEntry.3."+str(tableId)),SnmpComm.get("mesasEntry.4."+str(tableId)))
		return table

	@staticmethod
	def setTable(tableObj):
		#change tableObj on agente
		print "SnmpComm Updating table OBJ"

	@staticmethod
	def executeCmd(cmd):
		cmdList = cmd.split(" ")
		# print cmdList
		proc = subprocess.Popen(cmdList, stdout=subprocess.PIPE)
		return proc.stdout.read()

	@staticmethod
	def walk(OID):
		#Return numberOfObjects,arrayOfValues.
		cmdString = "snmpwalk"+SnmpComm.SNMP_PARAMETERS+OID
		# print "cmdString: "+cmdString
		cmdOutput = SnmpComm.executeCmd(cmdString)
		n,listOfResp = SnmpComm.parseResponse(cmdOutput)
		if(n != -1):
			return n,listOfResp
		else:
			return None
		
	@staticmethod
	def get(OID):
		#Return value of requested OID
		cmdString = "snmpget"+SnmpComm.SNMP_PARAMETERS+OID
		# print "cmdString: "+cmdString
		cmdOutput = SnmpComm.executeCmd(cmdString)
		n,listOfResp = SnmpComm.parseResponse(cmdOutput)
		# print listOfResp
		if(n != -1):
			return listOfResp[0]
		else:
			return None

	@staticmethod
	def set(OID,inputValue):
		#Return value of requested OID
		cmdString = "snmpset "+SnmpComm.SNMP_PARAMETERS_SET+OID+" "+"i "+str(inputValue)
		# print "cmdString: "+cmdString
		cmdOutput = SnmpComm.executeCmd(cmdString)
		n,listOfResp = SnmpComm.parseResponse(cmdOutput)
		if(n != -1):
			return listOfResp[0]
		else:
			return None

	@staticmethod
	def parseResponse(inputString):
		objCounter = 0
		retString = []

		if inputString == "":
			return -1,retString
		#check for error 
		errMsg = ["No Such Object available"]
		for i in range(0,len(errMsg)):
			if inputString.find(errMsg[i]) != -1:
				print "Error found"
				return -1,retString
		#break into lines
		line = inputString.split("\n")
		#fix empty line bug
		if line[-1] == "":
			del line[-1]
		numOfResp = len(line)
		#find a variable type
		for i in range(0,numOfResp):
			for j in range(0,len(SnmpComm.varNames)+1):
				if j == len(SnmpComm.varNames):
					#variable is from a unknown type
					print "variable type not found in line "+line[i]+" from "+str(numOfResp)+" lines"
					# print line
					return objCounter,retString
				#compare with a list of variables
				if line[i].find(SnmpComm.varNames[j]) != -1: 
					break
			objCounter = objCounter+1
			index = line[i].find(SnmpComm.varNames[j]) + len(SnmpComm.varNames[j])+1
			retString.append(line[i][index:])

		return objCounter,retString




class TableStatusEnum:
	Free,Occupied,Reserved,Unavailable = range(4)


class Table(object):
	def __init__(self,id,capacity,clients,status):
		self.id = id
		self.capacity = capacity
		self.clients = clients
		self.status = status

	def getStatusStr(self):
		dict = {"livre(0)": 'Free', "ocupada(1)": 'Occupied', "reservada(2)": 'Reserved', "indisponivel(3)": 'Unavailable'}
		return dict[self.status]
