#!/bin/sh

#MIBDIRS="/usr/share/mibs/iana/"
#MIBDIRS+=":/usr/share/mibs/ietf/"
#MIBDIRS+=":/usr/share/mibs/netsnmp/"
MIBDIRS+=":"$(pwd)

env MIBS="+RestCtrl-MIB" mib2c -c mib2c.scalar.conf capacidade
#env MIBS="+ALIGERA-MIB" mib2c -c mib2c.scalar.conf e1
#env MIBS="+ALIGERA-MIB" mib2c -c mib2c.mfd.conf e1Table
#env MIBS="+ALIGERA-MIB" mib2c -c mib2c.notify.conf e1Traps

#$MIBDIRS MIBS="+ALIGERA-MIB" mib2c -c mib2c.scalar.conf chan
#$MIBDIRS MIBS="+ALIGERA-MIB" mib2c -c mib2c.mfd.conf chanTable
#$MIBDIRS MIBS="+ALIGERA-MIB" mib2c -c mib2c.notify.conf chanTraps

#MIBS="+ALIGERA-MIB" mib2c -c mib2c.scalar.conf chan
#MIBS="+ALIGERA-MIB" mib2c -c mib2c.mfd.conf chanTable
#MIBS="+ALIGERA-MIB" mib2c -c mib2c.notify.conf chanTraps

