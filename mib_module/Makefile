CFLAGS=-O2 -Wall -g -fPIC -shared -DDEVICE_NAME=\"Aligera\ AG800\" 
LDFLAGS= -lm -lnetsnmp -lnetsnmpagent -lnetsnmphelpers -lnetsnmpmibs -Wl,--rpath,/usr/local/lib

OBJS_capacidade=capacidade.o
OBJS_lotAtual=lotAtual.o
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

all: capacidade.so lotAtual.so mesasTable.so ordersTable.so menuTable.so

clean:
	rm -vf *.o *.so 
	
capacidade.so: $(OBJS_capacidade)
	$(CC) $(CFLAGS) $(LDFLAGS) -o capacidade.so $(OBJS_capacidade)
lotAtual.so: $(OBJS_lotAtual)
	$(CC) $(CFLAGS) $(LDFLAGS) -o lotAtual.so $(OBJS_lotAtual)
lib_restaurante.so: $(OBJS_lib_restaurante)	
	$(CC) $(CFLAGS) $(LDFLAGS) -o lib_restaurante.so $(OBJS_lib_restaurante)	
mesasTable.so:$(OBJS_mesasTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o mesasTable.so lib_restaurante.c $(OBJS_mesasTable)
ordersTable.so:$(OBJS_ordersTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o ordersTable.so lib_restaurante.c $(OBJS_ordersTable)
menuTable.so:$(OBJS_menuTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o menuTable.so lib_restaurante.c $(OBJS_menuTable)

install:
	mkdir -p $(ROOTFS_DIR)/lib/snmp/dlmod/
	mkdir -p $(ROOTFS_DIR)/lib/mibs/
	cp -avf *.so $(ROOTFS_DIR)/lib/snmp/dlmod/
	cp -avf RestCtrl-MIB.my $(ROOTFS_DIR)/lib/mibs/

