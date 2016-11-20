#!/bin/sh

MIBDIRS="/lib/mibs:/usr/share/mibs/ietf:/lib/mibs/:/usr/share/mibs/iana/:/usr/share/mibs/ietf/:/usr/share/snmp/mibs:"$(pwd)
export MIBDIRS


#env MIBS="+RestCtrl-MIB" mib2c -c mib2c.scalar.conf capacidade
#echo env MIBS="+RestCtrl-MIB" mib2c -c mib2c.scalar.conf lotAtual
#env MIBS="+RestCtrl-MIB" mib2c -c mib2c.scalar.conf lotAtual
#env MIBS="+RestCtrl-MIB" mib2c -c mib2c.mfd.conf mesasTable
#env MIBS="+RestCtrl-MIB" mib2c -c mib2c.mfd.conf ordersTable
env MIBS="+RestCtrl-MIB" mib2c -c mib2c.mfd.conf menuTable
#env MIBS="+ALIGERA-MIB" mib2c -c mib2c.notify.conf e1Traps

#$MIBDIRS MIBS="+ALIGERA-MIB" mib2c -c mib2c.scalar.conf chan
#$MIBDIRS MIBS="+ALIGERA-MIB" mib2c -c mib2c.mfd.conf chanTable
#$MIBDIRS MIBS="+ALIGERA-MIB" mib2c -c mib2c.notify.conf chanTraps

#MIBS="+ALIGERA-MIB" mib2c -c mib2c.scalar.conf chan
#MIBS="+ALIGERA-MIB" mib2c -c mib2c.mfd.conf chanTable
#MIBS="+ALIGERA-MIB" mib2c -c mib2c.notify.conf chanTraps

