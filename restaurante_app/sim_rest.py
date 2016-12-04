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

"""
Simulador do Restaurante! 

Simula o funcionamento de um restaurante. Esse programa roda eternamente em um loop, randomicamente escolhendo uma das funcoes para executar: 
	- Adicionar mesa
	- Adicionar pedido
	- Adicionar clientes a uma mesa
	- Atualizar status de um pedido

O simulador se utiliza do programa restaurante.py para operar sobre os arquivos de configuracao. Por isso, em qualquer uma das funcoes citadas acima
iremos observar uma execucao da funcao subprocess.call(), que chama o programa restaurante.py com os devidos argumentos."""
def main():
	while(1):
		# Randomicamente escolhe uma das 4 funcoes para executar e dorme por 5 segundos antes de continuar.
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
		
"""
function: addMesa()

Essa funcao adiciona uma nova mesa vazia no restaurante. No nosso restaurante, limitamos a mesas de quatro ou duas pessoas. Entao, randomicamente ele escolhe 
uma dessas capacidades (4 ou 2 pessoas) para a nova mesa. Alem disso, o simulador tambem randomicamente escolhe um status inicial para essa mesa (livre, indisponivel ou 
reservada). Finalmente, ele faz a chamada ao programa restaurante.py para operar sobre os arquivos de configuracao."""
def addMesa():
	num_pessoas = random.choice(MESA_CAP)
	status_mesa = random.choice(STATUS_MESA)
	print "Adicionando mesa com capacidade=" + num_pessoas + " status = " + status_mesa
	# cmd = python restaurante.py -at NUM_PESSOAS STATUS
	subprocess.call([PYTHON, RESTAURANTE, ADD_MESA, num_pessoas, status_mesa])
	
"""
function: addPedido()

Essa funcao adiciona um pedido no arquivo de pedidos. Um pedido eh identificado por uma mesa, numero do item pedido e seu status.
Para simular a adicao de um pedido, escolhemos randomicamente uma das mesas ja ocupadas e tambem randomicamente 
escolhemos um dos itens do menu. Essas escolhas serao passadas para o programa restaurante.py para operar sobre o arquivo de configuracao dos pedidos."""
def addPedido():
	# Obtem o numero de mesas ja ocupadas
	num_mesas_ocupadas = getNumberOfOccupiedTables()
	# Obtem o numero de itens no menu
	num_itens = getNumItemsMenu()
	# Randomicamente escolher um de cada
	mesa = random.randint(1,num_mesas_ocupadas)
	item = random.randint(1,num_itens)
	print "Adicinando para mesa=" + str(mesa) + " pedido do item=" + str(item)
	# cmd = python restaurante.py -ao MESA ITEM
	subprocess.call([PYTHON, RESTAURANTE, ADD_PEDIDO, str(mesa) , str(item)])

"""
function: addPedido()

Essa funcao aloca uma mesa para um certo numero de clientes. O simulador randomicamente escolhe um numero de clientes que quer ocupar uma mesa 
e chama o programa restaurante.py informando esse numero. O restaurante.py eh responsavel por verificar se existe alguma mesa livre que suporte o numero de 
clientes especificado."""
def addCliente():
	num_clientes = random.randint(1,4)
	print "Alocando uma mesa para " + str(num_clientes) + " clientes"
	# cmd = python restaurante.py -ac NUM_CLIENTES
	subprocess.call([PYTHON, RESTAURANTE, ADD_CLIENTE, str(num_clientes)])

"""
function: atualizaPedido()

Essa funcao atualiza o status de um pedido nao pronto. Nao eh preciso especificar nada por parametros, o programa restaurante.py 
randomicamente seleciona um pedido e atualiza seu status. Se o status do pedido escolhido eh "pronto", nao faz nada."""
def atualizaPedido():
	print "Atualizando Pedido"
	subprocess.call([PYTHON, RESTAURANTE, ATUALIZA_PEDIDO])

"""
funcao herdada do programa restaurante.py. Ela eh responsavel por analisar o arquivo de configuracao de mesas e retornar 
o numero de mesas ocupadas."""
def getNumberOfOccupiedTables():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa_1=2
			if 'mesa_' in line:
				if int(line.strip().split('=')[1]) != 0: 
					count += 1
	return count

"""
funcao herdade do programa resutaurante.py. Ela eh responsavel por analisar o arquivo de configuracao do menu e retornar 
o numero de itens no menu."""	
def getNumItemsMenu():
	count = 0
	with open(CONFIG_PATH + MENU_CONFIG_FILE) as f:
		for line in f:
			if line.strip():
				count += 1
	return count

if __name__ == "__main__":
	main()
