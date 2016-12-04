# RestauranteSNMP

Implementação de um Agente, Gerente SNMP assim como um Simulador da operação de um restaurante.


-- Configuracao:

		Primeiramente, instale os seguintes pacotes no agente:
		- libsnmp-base
		- libsnmp-dev
		- ibsnmp-perl
		- libsnmp30
		- snmp
		- snmp-mibs-downloader
		- snmpd
		
		Depois disso, copie o arquivo snmpd.conf disponibilizado nesse projeto para /etc/snmp/snmpd.conf
		
		Dirija-se ate o diretorio mib-module e compile os arquivos necessarios:
			- ../mib-module> make
			
		Instale os arquivos executando como root:
			- ../mib-module> make install
			
		E finalmente reinicie o servico snmpd:
			- > sudo service snmpd restart
			

