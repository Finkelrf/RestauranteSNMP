import argparse
import subprocess
import random

ERROR = 1
OK = 0

LIVRE="0"
OCUPADA="1"
RESERVADA="2"
INDISPONIVEL="3"

ENCAMINHADO = "0"
EM_PREPARO = "1"
PRONTO = "2"

tables_capacity_list = ['4p', '2p']
#CONFIG_PATH = "/home/finkel/Documents/RestauranteSNMP/restaurante_app/config/"
CONFIG_PATH = "/home/rocordoni/Documentos/gerencia/RestauranteSNMP/restaurante_app/config/"
#CONFIG_PATH = "config/"
MESAS_CONFIG_FILE = "mesas.conf"
PEDIDOS_CONFIG_FILE = "pedidos.conf"
FUNCIONARIOS_CONFIG_FILE = "funcionarios.conf"
ESTOQUE_CONFIG_FILE = "estoque.conf"
DAILY_ORDERS_CONFIG_FILE = "pedidos_diarios.conf"
CURR_ORDERS_CONFIG_FILE = "pedidos_atual.conf"
REST_CONFIG_FILE = "rest.conf"
MENU_CONFIG_FILE = "menu.conf"

def getCurrentCapacity():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa_1=2
			if 'mesa_' in line:
				count += int(line.strip().split('=')[1])	# strip = Take off trailing chars from line. Split = split the line, separating by '='
	return count

def getMaxCapacity():
	count = 0
	d = {}
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesas_4p=2
			if 'mesas' in line:
				if line.strip().split('_')[1].split('=')[0] in tables_capacity_list:
					count += int(line.strip().split('_')[1].split('=')[0].split('p')[0])*int(line.strip().split('_')[1].split('=')[1])
	return count
	
def getOccupiedTables():
	count = 0
	d = {}
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa_1=2
			if 'mesa_' in line:
				table_number = line.strip().split('=')[0].split('_')[1]
				num_people = line.strip().split('=')[1]
				if num_people != '0':
					d[table_number] = []
					d[table_number].append(num_people)
					d[table_number].append(getTableCapacity(table_number))
					d[table_number].append(OCUPADA)
	return d
		
def getFreeTablesStatus(d):
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			if 'status_' in line:
				table_number = line.strip().split('=')[0].split('_')[1]
				status = line.strip().split('=')[1]
				if table_number not in d:
					d[table_number] = []
					d[table_number].append('0')
					d[table_number].append(getTableCapacity(table_number))
				if status == "livre":
					d[table_number].append(LIVRE)
				elif status == "reservada":
					d[table_number].append(RESERVADA)
				else:
					d[table_number].append(INDISPONIVEL)
	
def getAllTablesStatus():
	d = getOccupiedTables()
	getFreeTablesStatus(d)
	return d

def getTableCapacity(table_num):
	cap = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: capacidade_1=2
			if 'capacidade_' in line:
				if line.strip().split('=')[0].split('_')[1] == table_num:
					cap = line.strip().split('=')[1]
	return cap
	
def getNumberOfOccupiedTables():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa_1=2
			if 'mesa_' in line:
				if int(line.strip().split('=')[1]) != 0: 
					count += 1
	return count

def getTotalNumTables():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa_1=2
			if 'mesa_' in line:
				count += 1
	return count

	
def getNumPedidos():
	count = 0
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		for line in f:
			if line.strip():
				count += 1
	return count

def getPedidos():
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		for line in f:
			if line.strip():
				line_split = line.strip().split(',')
				table_number = line_split[0]
				item = line_split[1]
				status = line_split[2]
				if status == "encaminhado":
					status = ENCAMINHADO
				elif status == "preparo":
					status = EM_PREPARO
				else:
					status = PRONTO
				print table_number + ',' + item + ',' + status
			
def getStatus():
	with open(CONFIG_PATH + REST_CONFIG_FILE) as f:
		for line in f:
			if "status=" in line:
				return line.strip().split('=')[1]
				
def setStatus(new_status):
	with open(CONFIG_PATH + REST_CONFIG_FILE, 'w') as f:
		pass
		f.write("status=" + new_status[0])

def getNumFunc():
	count = 0;
	with open(CONFIG_PATH + FUNCIONARIOS_CONFIG_FILE) as f:
		for line in f:
			num = line.strip().split('=')[1]
			count += int(num)
	return count

def getFuncInfo():
	with open(CONFIG_PATH + FUNCIONARIOS_CONFIG_FILE) as f:
		for line in f:
			print line.strip()

def setPedido(arg_list):
	table_num = arg_list[0]
	item = arg_list[1]
	#Open file as "a", to append text at the end of the file
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE, "a") as f:
		f.write("\n" + table_num + "," + item + ",encaminhado")

def getNumItemsEstoque():
	count = 0
	with open(CONFIG_PATH + ESTOQUE_CONFIG_FILE) as f:
		for line in f:
			count += 1
	return count
	
def getEstoqueInfo():
	with open(CONFIG_PATH + ESTOQUE_CONFIG_FILE) as f:
		for line in f:
			print line.strip()
			
def getDailyOrdersEntries():
	count = 0
	with open(CONFIG_PATH + DAILY_ORDERS_CONFIG_FILE) as f:
		for line in f:
			count += 1
	return count
	
def getDailyOrdersInfo():
	with open(CONFIG_PATH + DAILY_ORDERS_CONFIG_FILE) as f:
		for line in f:
			print line.strip()
			
def getCurrOrders():
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		count = 0
		for line in f:
			if line.strip():
				if line.strip().split(',')[2] != "pronto":
					count += 1
		return count
		
def getNumItemsMenu():
	count = 0
	with open(CONFIG_PATH + MENU_CONFIG_FILE) as f:
		for line in f:
			if line.strip():
				count += 1
	return count
		
def getNextTableId():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			if "mesas_" in line:
				count += int(line.strip().split('=')[1])
	return count+1
	
def addTable(new_cap,status):
	search_str = "mesas_" + new_cap
	cap_dict = {}
	dump_str = ""
	add_str = ""
	new_id = getNextTableId()
	with open(CONFIG_PATH + MESAS_CONFIG_FILE, 'r') as f:
		f.seek(0)
		for line in f:
			""" O arquivo de configuracao contem entradas do tipo: mesas_4p=2:
			 Significando que existem 2 mesas com capacidade para 4 pessoas. Para atualizar a quantidade de mesas com uma certa capacidade,
			 criamos um dicionario mapeando {capacidade-da-mesa : numero-de-mesas-com-essa-capacidade}
			 Essa parte do codigo atualiza o numero de mesas configuradas:
			"""
			if "mesas_" in line:
				# Adiciona uma entrada no dicionario, fazendo um parse na linha lida, exemplo: mesas_(4p)=(2) --> {4p : 2}
				table_cap = line.strip().split('_')[1].split('=')[0]
				num_table_cap = line.strip().split('=')[1]
				cap_dict[table_cap] = int(num_table_cap)
				if new_cap == table_cap[0]:
					cap_dict[table_cap] = int(num_table_cap) + 1
			else:
				dump_str += line				
	add_str += "\nmesa_" + str(new_id) + "=0" 
	add_str += "\ncapacidade_" + str(new_id) + "=" + new_cap
	add_str += "\nstatus_" + str(new_id) + "=" + status
	with open(CONFIG_PATH + MESAS_CONFIG_FILE + ".temp", 'w') as f:
		for key, value in cap_dict.items():
			f.write("mesas_" + key + "=" + str(value) + '\n')
		f.write(dump_str.strip())
		f.write('\n' + add_str.strip())
	subprocess.call(['mv', CONFIG_PATH + MESAS_CONFIG_FILE + ".temp", CONFIG_PATH + MESAS_CONFIG_FILE])
	
"""
function updateMesasConf(table_num, table_cap, num_clients)
params: (str) table_num : o numero da mesa que foi encontrada como livre e com capacidade suportada
	    (str) table_cap : capacidade da mesa encontrada
		(str) num_clients : numero de clientes a serem alocados para essa mesa

Essa funcao tem por objetivo atualizar o arquivo contendo as configuracoes das mesas do restaurante. A funcao procura pelas linhas onde estao definidas
as configuracoes da mesa livre encontrada e as modifica para alocar os novos clientes nessa mesa."""
def updateMesasConf(table_num, table_cap, num_clients):
	dump_str = ""
	add_str = ""
	with open(CONFIG_PATH + MESAS_CONFIG_FILE, 'r') as f:
		for line in f:
			if "mesas_" in line:
				dump_str += line
			elif "mesa_" + table_num in line:
				add_str = "mesa_" + table_num + "=" + num_clients
			elif "capacidade_" + table_num in line:
				add_str += "\n" + line
			elif "status_" + table_num in line:
				#Essa linha nao eh mais necessaria 
				dump_str = dump_str
			else:
				dump_str += line
				
	with open(CONFIG_PATH + MESAS_CONFIG_FILE + ".temp", 'w') as f:
		f.write(dump_str)
		f.write(add_str)
	subprocess.call(['mv', CONFIG_PATH + MESAS_CONFIG_FILE + ".temp", CONFIG_PATH + MESAS_CONFIG_FILE])

""" 
function: addClients(num_clients)
params: (str) num_clients

Aloca um certo numero de clientes a uma mesa livre.
A funcao procura por uma mesa livre que suporte o numero de clientes desejados e chama a funcao updateMesasConf para fazer 
a atualizacao do arquivo de configuracao. Se nao acha nenhuma mesa disponivel, nao aloca nada e retorna erro. """
def addClients(num_clients):
	found = False
	d = getAllTablesStatus()
	# example: d = {'1' : ['2','2','0'] } where { table_num : [<num clientes atualmente sentados>,<max capacidade mesa>,<status>]
	for key, value in d.items():
		#Se o numero de clientes novos for menor ou igual a capacidade da mesa, e se a mesa estiver livre: salva os dados da mesa.
		if int(num_clients) <= int(value[1]) and value[2] == '0':
			found = True
			table_num = key
			table_cap = value[1]
			break
	# Se achou alguma mesa livre
	if found == True:
		updateMesasConf(table_num, table_cap, num_clients)
		return OK
	else:
		return ERROR
		
"""
function updateOrder()
params: None

Essa funcao eh responsavel por atualizar o arquivo de configuracao que contem as informacoes dos pedidos feitos.
Ela escolhe randomicamente um pedido, dentre o total de pedidos no arquivo e o atualiza.
O arquivo contem linhas do tipo: 1,1,encaminhado --> onde cada item representa: <numero-da-mesa>,<item-pedido>,<status-do-pedido>"""
def updateOrder():
	count = 0
	i = 1
	dump_str = ""
	add_str = ""
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		for line in f:
			count += 1
			
	# Randomicamente escolhe um pedido para atualizar
	random_line = random.randint(1, count)
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		for line in f:
			if i == random_line:
				line_split = line.strip().split(',')
				table_number = line_split[0]
				item = line_split[1]
				status = line_split[2]
				if status == "encaminhado":
					status = "preparo"
				elif status == "preparo":
					status = "pronto"
				add_str = "\n" + table_number + "," + item + "," + status
				i += 1
			else:
				dump_str += line
				i += 1
				
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE, "w") as f:
		f.write(dump_str.strip())
		f.write(add_str)		
			
def main():
	
	#~ The argparse generates the software usage automatically
	
	parser = argparse.ArgumentParser(description='Controle de restaurante')
	parser.add_argument('-c', action='store_true', dest='c',  			 					help='Obtem capacidade atual')
	parser.add_argument('-m', action='store_true', dest='max_capacity',  					help='Obtem capacidade maxima')
	parser.add_argument('-t', action='store_true', dest='tables_occupied',  				help='Obtem mesas ocupadas')
	parser.add_argument('-nc',action='store_true', dest='number_of_tables_occupied',		help='Obtem numero de mesas ocupadas')
	parser.add_argument('-n', action='store_true', dest='number_of_total_tables',			help='Obtem numero total de mesas')
	parser.add_argument('-s', action='store_true', dest='status',  							help='Obtem status de todas as mesas')
	parser.add_argument('-np',action='store_true', dest='num_pedidos',  					help='Obtem numero total de pedidos')
	parser.add_argument('-p', action='store_true', dest='pedido',  							help='Obtem pedidos de todas as mesas')
	parser.add_argument('-gs',action='store_true', dest='get_status',  						help='Obtem status do restaurante (aberto/fechado)')
	parser.add_argument('-f', action='store_true', dest='num_func',  						help='Obtem numero de funcionarios')
	parser.add_argument('-fi',action='store_true', dest='func_info',  						help='Obtem info de funcionarios')
	parser.add_argument('-ne',action='store_true', dest='num_items_estoque',  				help='Obtem numero de items no estoque')
	parser.add_argument('-e', action='store_true', dest='estoque_info',  					help='Obtem info do estoque')
	parser.add_argument('-nd',action='store_true', dest='num_daily_orders',  				help='Obtem numero de pedidos no arquivo')
	parser.add_argument('-d', action='store_true', dest='daily_orders_info',  				help='Obtem info do numero de pedidos diarios')
	parser.add_argument('-o', action='store_true', dest='curr_orders',  					help='Obtem numero de pedidos nao prontos atual')
	parser.add_argument('-nm',action='store_true', dest='num_items_menu',  					help='Obtem numero de itens no menu')
	parser.add_argument('-up',action='store_true', dest='update_order',						help='Atualiza o status de um pedido')
	parser.add_argument('-ss', nargs=1, type=str, metavar='STATUS', dest='set_status',  	help='Modifica o status do restaurante')
	parser.add_argument('-ao', nargs=2, type=str, metavar=('MESA', 'ITEM'),dest='addOrder',	help='Cria pedido do item ITEM para a mesa MESA')
	parser.add_argument('-at', nargs=2, type=str, metavar=('CAPACIDADE', 'STATUS'), dest='addTable',		help='Insere nova mesa na configuracao do restaurante')
	parser.add_argument('-ac', nargs=1, type=str, metavar='NUM_CLIENTS', 			dest='addClients',		help='Aloca um certo numero de clientes a uma mesa livre que possua capacidade para o num de clientes desejado')
	args = parser.parse_args()
	
	if args.c:
		print getCurrentCapacity()
	if args.max_capacity:
		print getMaxCapacity()
	if args.number_of_tables_occupied:
		print getNumberOfOccupiedTables()
	if args.number_of_total_tables:
		print getTotalNumTables()
	if args.tables_occupied:
		d = {}
		d = getOccupiedTables()
		#print something like 1,2,2,1 where <table_num>,<num clientes atualmente sentados>,<max capacidade mesa>,<status>
		for k,v in sorted(d.items()):
			s = ""
			for i in v:
				s += ',' + i
			print k + s
	if args.status:
		d = getAllTablesStatus()
		#print something like 1,2,2,0 where <table_num>,<num clientes atualmente sentados>,<max capacidade mesa>,<status>
		for k,v in sorted(d.items()):
			s = ""
			for i in v:
				s += ',' + i
			print k + s
	if args.num_pedidos:
		print getNumPedidos()
	if args.pedido:
		#print something like 1,2,pronto where <table_num>,<item>,<status pedido>
		getPedidos()
	if args.get_status:
		print getStatus()
	if args.set_status:
		setStatus(args.set_status)
	if args.num_func:
		print getNumFunc()
	if args.func_info:
		 getFuncInfo()
	if args.addOrder:
		setPedido(args.addOrder)
	if args.num_items_estoque:
		print getNumItemsEstoque()
	if args.estoque_info:
		getEstoqueInfo()
	if args.num_daily_orders:
		print getDailyOrdersEntries()
	if args.curr_orders:
		print getCurrOrders()
	if args.num_items_menu:
		print getNumItemsMenu()
	if args.daily_orders_info:
		getDailyOrdersInfo()
	if args.addTable:
		if args.addTable[0]+"p" not in tables_capacity_list:
			print "Uma mesa com capacidade "+ args.addTable[0] + " nao eh suportada"
		else:
			addTable(args.addTable[0], args.addTable[1])
	if args.addClients:
		if addClients(args.addClients[0]) != OK:
			print "Error while adding clients to table"
	if args.update_order:
		updateOrder()
		
			
if __name__ == "__main__":
	main()

