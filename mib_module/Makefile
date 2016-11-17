CFLAGS=-O2 -Wall -g -fPIC -shared -DDEVICE_NAME=\"Aligera\ AG800\"
LDFLAGS=-lm -lnetsnmp -lnetsnmpagent -lnetsnmphelpers -lnetsnmpmibs -Wl,--rpath,/usr/local/lib

OBJS_capacidade=capacidade.o
#OBJS_e1=e1.o 
#OBJS_chan=chan.o 

#OBJS_e1Table=e1Table.o \
#	e1Table_interface.o \
#	e1Table_data_access.o \
#	e1Table_data_get.o \
#	e1Table_data_set.o \
#	e1Traps.o

#OBJS_chanTable=chanTable.o \
#	chanTable_interface.o \
#	chanTable_data_access.o \
#	chanTable_data_get.o \
#	chanTable_data_set.o \
#	chanTraps.o

all: capacidade.so 
#all: device.so e1.so  e1Table.so chan.so chanTable.so

clean:
#	rm -vf *.o *.so *~ e1Table chanTable
	rm -vf *.o *.so 
	
#device.so: $(OBJS_device)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o device.so $(OBJS_device)
capacidade.so: $(OBJS_capacidade)
	$(CC) $(CFLAGS) $(LDFLAGS) -o capacidade.so $(OBJS_capacidade)
	
#e1.so:$(OBJS_e1)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o e1.so $(OBJS_e1)
	
#e1Table.so:$(OBJS_e1Table)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o e1Table.so $(OBJS_e1Table)
	
#chan.so:$(OBJS_chan)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o chan.so $(OBJS_chan)

#chanTable.so:$(OBJS_chanTable)
#	$(CC) $(CFLAGS) $(LDFLAGS) -o chanTable.so $(OBJS_chanTable)


install:
	mkdir -p $(ROOTFS_DIR)/lib/snmp/dlmod/
	mkdir -p $(ROOTFS_DIR)/lib/mibs/
	cp -avf *.so $(ROOTFS_DIR)/lib/snmp/dlmod/
	cp -avf RestCtrl-MIB.my $(ROOTFS_DIR)/lib/mibs/

