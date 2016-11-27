import argparse

LIVRE="0"
OCUPADA="1"
INDISPONIVEL="2"

ENCAMINHADO = "0"
EM_PREPARO = "1"
PRONTO = "2"

tables_capacity_list = ['4p', '2p']
CONFIG_PATH = "/home/rocordoni/Documentos/gerencia/RestauranteSNMP/restaurante_app/config/"
MESAS_CONFIG_FILE = "mesas.conf"
PEDIDOS_CONFIG_FILE = "pedidos.conf"
FUNCIONARIOS_CONFIG_FILE = "funcionarios.conf"
ESTOQUE_CONFIG_FILE = "estoque.conf"

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
				count += 1
	return count
	
def getNumPedidos():
	count = 0
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		for line in f:
			count += 1
	return count

def getPedidos():
	with open(CONFIG_PATH + PEDIDOS_CONFIG_FILE) as f:
		for line in f:
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
		f.write(table_num + "," + item + ",encaminhado")

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
		
def main():
	
	#~ The argparse generates the software usage automatically
	
	parser = argparse.ArgumentParser(description='Controle de restaurante')
	parser.add_argument('-c', action='store_true', dest='c',  			 					help='Obtem capacidade atual')
	parser.add_argument('-m', action='store_true', dest='max_capacity',  					help='Obtem capacidade maxima')
	parser.add_argument('-t', action='store_true', dest='tables_occupied',  				help='Obtem mesas ocupadas')
	parser.add_argument('-n', action='store_true', dest='number_of_tables_occupied',		help='Obtem numero de mesas ocupadas')
	parser.add_argument('-s', action='store_true', dest='status',  							help='Obtem status de todas as mesas')
	parser.add_argument('-np',action='store_true', dest='num_pedidos',  					help='Obtem numero total de pedidos')
	parser.add_argument('-p', action='store_true', dest='pedido',  							help='Obtem pedidos de todas as mesas')
	parser.add_argument('-f', action='store_true', dest='num_func',  						help='Obtem numero de funcionarios')
	parser.add_argument('-fi', action='store_true', dest='func_info',  						help='Obtem info de funcionarios')
	parser.add_argument('-ne', action='store_true', dest='num_items_estoque',  				help='Obtem numero de items no estoque')
	parser.add_argument('-e', action='store_true', dest='estoque_info',  					help='Obtem info do estoque')
	parser.add_argument('-a', nargs=2, type=str, metavar=('MESA', 'ITEM'),dest='addOrder',	help='Cria pedido do item ITEM para a mesa MESA')
	args = parser.parse_args()
	
	if args.c:
		print getCurrentCapacity()
	if args.max_capacity:
		print getMaxCapacity()
	if args.number_of_tables_occupied:
		print getNumberOfOccupiedTables()
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
	if args.num_func:
		print getNumFunc()
	if args.func_info:
		 getFuncInfo()
	if args.addOrder:
		setPedido(args.a)
	if args.num_items_estoque:
		print getNumItemsEstoque()
	if args.estoque_info:
		getEstoqueInfo()
		
		
			
if __name__ == "__main__":
	main()

