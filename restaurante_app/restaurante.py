import argparse


tables_capacity_list = ['4p', '2p']
CONFIG_PATH = "/home/rocordoni/Documentos/gerencia/restaurante_app/config/"
MESAS_CONFIG_FILE = "mesas.conf"

def getCurrentCapacity():
	count = 0
	with open(CONFIG_PATH + MESAS_CONFIG_FILE) as f:
		for line in f:
			# We expect something as: mesa=2
			if 'mesa=' in line:
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

def main():
	#~ The argparse generates the software usage automatically
	parser = argparse.ArgumentParser(description='Controle de restaurante')
	#~ parser.add_argument('-p', dest='pedido', action='store', nargs=2, help='Adiciona pedido')
	parser.add_argument('-c', dest='c', action='store_true', help='Obtem capacidade atual')
	parser.add_argument('-m', dest='max_capacity', action='store_true', help='Obtem capacidade maxima')
	args = parser.parse_args()
	#~ print args


	if args.c:
		print getCurrentCapacity()
		
	if args.max_capacity:
		print getMaxCapacity()
	
if __name__ == "__main__":
	main()

