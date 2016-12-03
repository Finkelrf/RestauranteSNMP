CFLAGS=-O2 -Wall -g -fPIC -shared -DDEVICE_NAME=\"Restaurante\ Ctrl\" 
LDFLAGS= -lm -lnetsnmp -lnetsnmpagent -lnetsnmphelpers -lnetsnmpmibs -Wl,--rpath,/usr/local/lib

OBJS_capacidade=capacidade.o
OBJS_lotAtual=lotAtual.o
OBJS_numFunc=numFunc.o
OBJS_status=status.o
OBJS_currNumOrders=currNumOrders.o
OBJS_lib_restaurante=lib_restaurante.o

OBJS_mesasTable=mesasTable.o \
	mesasTable_interface.o \
	mesasTable_data_access.o \
	mesasTable_data_get.o \
	mesasTable_data_set.o \
	
OBJS_ordersTable=ordersTable.o \
	ordersTable_interface.o \
	ordersTable_data_access.o \
	ordersTable_data_get.o \
	ordersTable_data_set.o \

OBJS_menuTable=menuTable.o \
	menuTable_interface.o \
	menuTable_data_access.o \
	menuTable_data_get.o \
	menuTable_data_set.o \
	
OBJS_estoqueTable=estoqueTable.o \
	estoqueTable_interface.o \
	estoqueTable_data_access.o \
	estoqueTable_data_get.o \
	estoqueTable_data_set.o \
	estoqueTrap.o
	
OBJS_dailyOrdersTable=dailyOrdersTable.o \
	dailyOrdersTable_interface.o \
	dailyOrdersTable_data_access.o \
	dailyOrdersTable_data_get.o \
	dailyOrdersTable_data_set.o \

all: capacidade.so lotAtual.so numFunc.so status.so currNumOrders.so mesasTable.so ordersTable.so menuTable.so estoqueTable.so dailyOrdersTable.so

clean:
	rm -vf *.o *.so 
	
capacidade.so: $(OBJS_capacidade)
	$(CC) $(CFLAGS) $(LDFLAGS) -o capacidade.so $(OBJS_capacidade)
lotAtual.so: $(OBJS_lotAtual)
	$(CC) $(CFLAGS) $(LDFLAGS) -o lotAtual.so $(OBJS_lotAtual)
numFunc.so: $(OBJS_numFunc)
	$(CC) $(CFLAGS) $(LDFLAGS) -o numFunc.so lib_restaurante.c $(OBJS_numFunc)
status.so: $(OBJS_status)
	$(CC) $(CFLAGS) $(LDFLAGS) -o status.so lib_restaurante.c $(OBJS_status)
currNumOrders.so: $(OBJS_currNumOrders)
	$(CC) $(CFLAGS) $(LDFLAGS) -o currNumOrders.so lib_restaurante.c $(OBJS_currNumOrders)
lib_restaurante.so: $(OBJS_lib_restaurante)	
	$(CC) $(CFLAGS) $(LDFLAGS) -o lib_restaurante.so $(OBJS_lib_restaurante)	
mesasTable.so:$(OBJS_mesasTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o mesasTable.so lib_restaurante.c $(OBJS_mesasTable)
ordersTable.so:$(OBJS_ordersTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o ordersTable.so lib_restaurante.c $(OBJS_ordersTable)
menuTable.so:$(OBJS_menuTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o menuTable.so lib_restaurante.c $(OBJS_menuTable)
estoqueTable.so:$(OBJS_estoqueTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o estoqueTable.so lib_restaurante.c $(OBJS_estoqueTable)
dailyOrdersTable.so:$(OBJS_dailyOrdersTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o dailyOrdersTable.so lib_restaurante.c $(OBJS_dailyOrdersTable)

install:
	mkdir -p $(ROOTFS_DIR)/lib/snmp/dlmod/
	mkdir -p $(ROOTFS_DIR)/lib/mibs/
	cp -avf *.so $(ROOTFS_DIR)/lib/snmp/dlmod/
	cp -avf RestCtrl-MIB.my $(ROOTFS_DIR)/lib/mibs/

