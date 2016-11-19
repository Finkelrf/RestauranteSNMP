import argparse

LIVRE="0"
OCUPADA="1"
INDISPONIVEL="2"
tables_capacity_list = ['4p', '2p']
CONFIG_PATH = "/home/rocordoni/Documentos/gerencia/RestauranteSNMP/restaurante_app/config/"
MESAS_CONFIG_FILE = "mesas.conf"

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
		f.seek(0)
		for line in f:
			if 'status_' in line:
				table_number = line.strip().split('=')[0].split('_')[1]
				status = line.strip().split('=')[1]
				if table_number not in d:
					d[table_number] = []
					d[table_number].append(num_people)
					d[table_number].append(getTableCapacity(table_number))
				if status == "livre":
					d[table_number].append(LIVRE)
				else:
					d[table_number].append(INDISPONIVEL)
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
	

	
def main():
	
	#~ The argparse generates the software usage automatically
	
	parser = argparse.ArgumentParser(description='Controle de restaurante')
	parser.add_argument('-c', action='store_true', dest='c',  			 help='Obtem capacidade atual')
	parser.add_argument('-m', action='store_true', dest='max_capacity',  help='Obtem capacidade maxima')
	parser.add_argument('-t', action='store_true', dest='tables_occupied',  help='Obtem mesas ocupadas')
	parser.add_argument('-n', action='store_true', dest='number_of_tables_occupied',  help='Obtem numero de mesas ocupadas')
	parser.add_argument('-s', action='store_true', dest='status',  help='Obtem status de todas as mesas')
	
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
		#print something like 1,2,2 where <table_num>,<num clientes atualmente sentados>,<max capacidade mesa>,<status>
		for k,v in sorted(d.items()):
			s = ""
			for i in v:
				s += ',' + i
			print k + s
	
if __name__ == "__main__":
	main()

