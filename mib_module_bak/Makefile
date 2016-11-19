CFLAGS=-O2 -Wall -g -fPIC -shared -DDEVICE_NAME=\"Aligera\ AG800\" -I/home/rocordoni/Documentos/gerencia/RestauranteSNMP/mib_module
LDFLAGS= -L/home/rocordoni/Documentos/gerencia/RestauranteSNMP/mib_module -lm -lnetsnmp -lnetsnmpagent -lnetsnmphelpers -lnetsnmpmibs -Wl,--rpath,/usr/local/lib

OBJS_capacidade=capacidade.o
OBJS_lotAtual=lotAtual.o
#OBJS_lib_restaurante=lib_restaurante.o

OBJS_mesasTable=mesasTable.o \
	mesasTable_interface.o \
	mesasTable_data_access.o \
	mesasTable_data_get.o \
	mesasTable_data_set.o \

#OBJS_chanTable=chanTable.o \
#	chanTable_interface.o \
#	chanTable_data_access.o \
#	chanTable_data_get.o \
#	chanTable_data_set.o \
#	chanTraps.o

all: capacidade.so lotAtual.so mesasTable.so 
#all: device.so e1.so  e1Table.so chan.so chanTable.so

clean:
#	rm -vf *.o *.so *~ e1Table chanTable
	rm -vf *.o *.so 
	
#device.so: $(OBJS_device)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o device.so $(OBJS_device)
capacidade.so: $(OBJS_capacidade)
	$(CC) $(CFLAGS) $(LDFLAGS) -o capacidade.so $(OBJS_capacidade)
lotAtual.so: $(OBJS_lotAtual)
	$(CC) $(CFLAGS) $(LDFLAGS) -o lotAtual.so $(OBJS_lotAtual)
#lib_restaurante.so: $(OBJS_lib_restaurante)	
#	$(CC) $(CFLAGS) $(LDFLAGS) -o lib_restaurante.so $(OBJS_lib_restaurante)
	
#e1.so:$(OBJS_e1)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o e1.so $(OBJS_e1)
	
mesasTable.so:$(OBJS_mesasTable)
	$(CC) $(CFLAGS) $(LDFLAGS) -o mesasTable.so $(OBJS_mesasTable)
	
#chan.so:$(OBJS_chan)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o chan.so $(OBJS_chan)

#chanTable.so:$(OBJS_chanTable)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o chanTable.so $(OBJS_chanTable)


install:
	mkdir -p $(ROOTFS_DIR)/lib/snmp/dlmod/
	mkdir -p $(ROOTFS_DIR)/lib/mibs/
	cp -avf *.so $(ROOTFS_DIR)/lib/snmp/dlmod/
	cp -avf RestCtrl-MIB.my $(ROOTFS_DIR)/lib/mibs/

