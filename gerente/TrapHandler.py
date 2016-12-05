
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import sys
from PyQt4 import QtGui
from threading import Thread
from time import sleep
from TrapHandler import *
from teste import *

IP = '192.168.1.11'

class TrapHandler():
    def __init__(self,out_q):    
        # Create SNMP engine with autogenernated engineID and pre-bound
        # to socket transport dispatcher
        snmpEngine = engine.SnmpEngine()


        # Transport setup

        # UDP over IPv4, first listening interface/port
        config.addTransport(
            snmpEngine,
            udp.domainName + (1,),
            udp.UdpTransport().openServerMode((IP, 162))
        )

        # SNMPv1/2c setup

        # SecurityName <-> CommunityName mapping
        config.addV1System(snmpEngine, 'my-area', 'public')


        # Callback function for receiving notifications
        # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
        def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
                  varBinds, cbCtx):
            print('Notification from ContextEngineId "%s", ContextName "%s"' % (contextEngineId.prettyPrint(),
                                                                                contextName.prettyPrint()))
            for name, val in varBinds:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            
            out_q.put("teste")


        # Register SNMP Application at the SNMP engine
        if ntfrcv.NotificationReceiver(snmpEngine, cbFun):
        	print "HEEEE"

        snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

        # Run I/O dispatcher which would receive queries and send confirmations
        try:
            snmpEngine.transportDispatcher.runDispatcher()
        except:
            snmpEngine.transportDispatcher.closeDispatcher()
            raise





