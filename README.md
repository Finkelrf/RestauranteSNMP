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
		
		
		
		Dirija-se ate o diretorio mib-module:
			- cd path/to/RestauranteSNMP/mib-module
			
		Modifique as variaveis em lib_restaurante.h para o caminho correto em sua maquina:
		
			#define APP_PYTHON_PATH "python path/to/RestauranteSNMP/restaurante_app/restaurante.py " -- deixe um espaco em branco no final dessa string.
			#define CONFIG_PATH "path/to/RestauranteSNMP/restaurante_app/config"

		Compile o codigo fonte:
			- ../mib-module> make
			
		Instale os arquivos executando como root:
			- ../mib-module> make install
			
		E finalmente reinicie o servico snmpd:
			- > sudo service snmpd restart

-- Uso:
	
		Apos executar a configuracao do agente, ele esta apto a receber/enviar requisicoes/respostas SNMP.
			

