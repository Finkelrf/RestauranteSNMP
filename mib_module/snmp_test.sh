#!/bin/sh

MIBDIRS="/lib/mibs:/usr/share/mibs/ietf:/usr/share/mibs/netsnmp:/usr/share/snmp/mibs/:/usr/local/share/snmp/mibs"
#MIBDIRS="/lib/mibs:/usr/share/mibs/ietf:/usr/share/mibs/iana:/usr/share/mibs/netsnmp:/usr/share/snmp/mibs/:"$(pwd)

IPADDR=localhost

#snmptable $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB mesasTable
snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB mesasTable
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB ordersTable
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB menuTable
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB estoqueTable
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB dailyOrdersTable
#snmpwalk $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB 1.3.6.1.4.1.12619.1.0
#~ echo snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB capacidade.0
#snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB capacidade.0
#snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB currNumOrders.0
#snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB lotAtual.0
#snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB numFunc.0
#snmpget $IPADDR -c public -v2c -M$MIBDIRS -mRestCtrl-MIB status.0


#snmpset -c private -v2c -M$MIBDIRS -mRestCtrl-MIB $IPADDR status.0 i 0

#snmptrap -v 2c -c public -M $MIBDIRS -m ALIGERA-MIB $IPADDR "" ALIGERA-MIB::e1AlarmsChange e1Index i 1

