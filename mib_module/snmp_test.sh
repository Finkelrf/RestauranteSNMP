#!/bin/sh

MIBDIRS="/lib/mibs:/usr/share/mibs/ietf"
#MIBDIRS="/lib/mibs:/usr/share/mibs/ietf:/usr/share/mibs/iana:/usr/share/mibs/netsnmp:"$(pwd)

IPADDR=localhost

#snmptable $IPADDR -c public -v2c -M$MIBDIRS -mIF-MIB ifTable
#snmptable $IPADDR -c public -v2c -M$MIBDIRS -mALIGERA-MIB e1Table
#snmptable $IPADDR -c public -v2c -M$MIBDIRS -mALIGERA-MIB chanTable
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mALIGERA-MIB aligeraMgmt
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mALIGERA-MIB e1
echo snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB capacidade.0
snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB capacidade.0

#snmptrap -v 2c -c public -M $MIBDIRS -m ALIGERA-MIB $IPADDR "" ALIGERA-MIB::e1AlarmsChange e1Index i 1

