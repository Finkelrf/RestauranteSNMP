import argparse
import subprocess
import random
import time

CONFIG_PATH = "config/"
MENU_CONFIG_FILE = "menu.conf"
MESAS_CONFIG_FILE = "mesas.conf"
PYTHON = "python"
RESTAURANTE =  "restaurante.py"
ADD_MESA = "-at"
ADD_PEDIDO = "-ao"
ADD_CLIENTE = "-ac"
ATUALIZA_PEDIDO = "-up"
MESA_CAP = ["4", "2"]
STATUS_MESA = ["livre", "indisponivel", "reservada"]

def main():
	
	while(1):
		op = random.randint(1, 4)
		if op == 1:
			addMesa()
		elif op == 2:
			addPedido()
		elif op ==3:
			addCliente()
		elif op == 4:
			atualizaPedido()
		time.sleep(5)
		
def addMesa():
	num_pessoas = random.choice(MESA_CAP)
	status_mesa = random.choice(STATUS_MESA)
	print "Adicionando mesa com capacidade=" + num_pessoas + " status = " + status_mesa
	subprocess.call([PYTHON, RESTAURANTE, ADD_MESA, num_pessoas, status_mesa])

def addPedido():
	num_mesas_ocupadas = getNumberOfOccupiedTables()
	num_itens = getNumItemsMenu()
	mesa = random.randint(1,num_mesas_ocupadas)
	item = random.randint(1,num_itens)
	print "Adicinando para mesa=" + str(mesa) + " pedido do item=" + str(item)
	subprocess.call([PYTHON, RESTAURANTE, ADD_PEDIDO, str(mesa) , str(item)])
	
def addCliente():
	num_clientes = random.randint(1,4)
	print "Alocando uma mesa para " + str(num_clientes) + " clientes"
	subprocess.call([PYTHON, RESTAURANTE, ADD_CLIENTE, str(num_clientes)])
	
def atualizaPedido():
	print "Atualizando Pedido"
	subprocess.call([PYTHON, RESTAURANTE, ATUALIZA_PEDIDO])

def getNumberOfOccupiedTables():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa_1=2
			if 'mesa_' in line:
				if int(line.strip().split('=')[1]) != 0: 
					count += 1
	return count
	
def getNumItemsMenu():
	count = 0
	with open(CONFIG_PATH + MENU_CONFIG_FILE) as f:
		for line in f:
			if line.strip():
				count += 1
	return count


	


if __name__ == "__main__":
	main()
