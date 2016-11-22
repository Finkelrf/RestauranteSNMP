from random import randint


class SnmpComm(object):

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


class TableStatusEnum:
	Free,Ocupy,Reserved,Unavailable = range(4)
