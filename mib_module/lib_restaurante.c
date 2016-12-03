#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "lib_restaurante.h"

/*
 * get_number_tables()
 * 
 * Retorno: number_tables (unsigned long). 
 * 
 * Essa funcao eh responsavel por obter o numero total de mesas do restaurante.
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
unsigned long get_number_tables() {
	FILE *output;
	char *ret;
	unsigned long   number_tables;
    char app_path[120] = APP_PYTHON_PATH;	//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
	strcat(app_path, "-n");					// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 		// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	number_tables = strtoul(buffer, NULL, 10);
	pclose(output);
	return number_tables;
}

/*
 * get_mesas_info(struct mesa_info *mesas)
 * 
 * Retorno: void. 
 * 
 * Essa funcao eh responsavel por obter informacoes sobre as mesas do restaurante. 
 * As informacoes sao: numero da mesa, numero de clientes atualmente sentados nesta mesa, 
 * a capacidade total da mesa e tambem o status (livre, ocupada, indisponivel ou reservada).
 * As informacoes obtidas sao armazenadas em um ponteiro para um um array da estrutura mesa_info,
 * passado como argumento para essa funcao.
 * 
 * Esses valores sao obtidos utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * A rotina gera um csv (comma separated values), que eh analisado utilizando a rotina strtok().
 * */
void get_mesas_info(struct mesa_info *mesas) {
	FILE *output;
	unsigned long   number_tables=0;
	unsigned long   mesa_num;
    char app_path[120] = APP_PYTHON_PATH;	//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    char *r;
	strcat(app_path, "-s");					// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 		// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	while(fgets(buffer, BUFF_SIZE, output)) {	// Loop pelas linhas de resultado da chamada ao aplicativo
		r = strtok(buffer, ",");
		mesa_num = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		mesas[mesa_num].num_clientes = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		mesas[mesa_num].capacidade = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		mesas[mesa_num].status = atoi(r);	
	}
	pclose(output);
}

/*
 * get_number_orders()
 * 
 * Retorno: number_orders (unsigned long). 
 * 
 * Essa funcao eh responsavel por obter o numero total de pedidos ainda nao entregues.
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
unsigned long get_number_orders() {
	FILE *output;
	unsigned long   number_orders=0;
    char app_path[120] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
	strcat(app_path, "-np");					// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 			// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	number_orders = strtoul(buffer, NULL, 10);
	pclose(output);
	return number_orders;
}

/*
 * get_orders_info(struct order_info *orders)
 * 
 * Retorno: void. 
 * 
 * Essa funcao eh responsavel por obter informacoes sobre os pedidos feitos. 
 * As informacoes sao: numero da mesa na qual o pedido foi feito, o numero do item do cardapio e  
 * o status do preparamento do pedido (encaminhadoParaCozinha(0), emPreparo(1), pronto(2)).
 * As informacoes obtidas sao armazenadas em um ponteiro para um um array da estrutura order_info,
 * passado como argumento para essa funcao.
 * 
 * Esses valores sao obtidos utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * A rotina gera um csv (comma separated values), que eh analisado utilizando a rotina strtok().
 * */
void get_orders_info(struct order_info *orders) {
	FILE *output;
	unsigned long   number_tables=0;
	unsigned long   mesa_num, item;
    char app_path[120] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    char *r;
    int i, status;
	strcat(app_path, "-p");						// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 			// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	i = 0;
	while(fgets(buffer, BUFF_SIZE, output)) {			// Loop pelas linhas de resultado da chamada ao aplicativo
		r = strtok(buffer, ",");
		mesa_num = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		item = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		status = atoi(r);
		orders[i].table = mesa_num;
		orders[i].item = item;
		orders[i].status = status;
		i++;
	}
	pclose(output);
}

/*
 * getNumFunc()
 * 
 * Retorno: num_func (unsigned long). 
 * 
 * Essa funcao eh responsavel por obter o numero total de funcionarios que trabalham no restaurante.
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
unsigned long getNumFunc() {
    FILE *output;
    char app_path[120] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    unsigned long num_func;
    strcat(app_path, "-f");						// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 			// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	num_func = strtoul(buffer, NULL, 10);
	pclose(output);
	return num_func;

}

/*
 * getRestStatus()
 * 
 * Retorno: status (int). 
 * 
 * Essa funcao eh responsavel por obter o status atual do restaurante (aberto(0), fechado(1)).
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
int getRestStatus() {
	FILE *output;
    char app_path[120] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    int status;
	strcat(app_path, "-gs");					// Concatena na string o argumento necessario para o software auxiliar
	output = popen(app_path, "r");				// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	status = atoi(buffer);
	fclose(output);
	return status;
}

/*
 * setRestStatus(int new_status)
 * 
 * Retorno: status (int). 
 * 
 * Essa funcao eh responsavel por setar o novo valor do status do restaurante (aberto(0), fechado(1)).
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
int setRestStatus(int new_status) {
	FILE *output;
    char app_path[120] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char aux[BUFF_SIZE];
    char buffer[BUFF_SIZE];
    int status;
    if (snprintf(aux, BUFF_SIZE, "%d", new_status) < 0) {	// Converte o novo status, que eh um inteiro, em string.
		syslog (LOG_INFO,"incorrect parameters on snprintf.\n");
		return EXIT_FAILURE;
	}
	strcat(app_path, "-ss ");					
	strcat(app_path, aux );						// Concatena na string de caminho o argumento necessario para o software auxiliar
	output = popen(app_path, "r");
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	status = atoi(buffer);
	fclose(output);
	return status;
}

/*
 * getNumItemsEstoque()
 * 
 * Retorno: num_items (unsigned long). 
 * 
 * Essa funcao eh responsavel por obter o numero de tipos de produtos contidos no estoque.
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
int getNumItemsEstoque() {
	FILE *output;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    unsigned long num_items;
    strcat(app_path, "-ne");						// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 				// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	num_items = strtoul(buffer, NULL, 10);
	pclose(output);
	return num_items;
}

/*
 * getEstoque(struct estoque_item_info *estoque
 * 
 * Retorno: void. 
 * 
 * Essa funcao eh responsavel por obter informacoes sobre os itens em estoque. 
 * As informacoes sao: nome do item e quantidade ainda presente em estoque.  
 * As informacoes obtidas sao armazenadas em um ponteiro para um um array da estrutura estoque_item_info,
 * passado como argumento para essa funcao.
 * 
 * Esses valores sao obtidos utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * A rotina gera um csv (comma separated values), que eh analisado utilizando a rotina strtok().
 * */
void getEstoque(struct estoque_item_info *estoque) {
	FILE *output;
	int i=0;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    char *r;
	strcat(app_path, "-e");							// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 				// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	while(fgets(buffer, BUFF_SIZE, output)) {
		r = strtok(buffer, ",");
		strncpy(estoque[i].item_name, r, BUFF_SIZE);
		r = strtok(NULL, ",");
		estoque[i].amount = strtoul(r, NULL, 10);
		i++;
	}
	pclose(output);
}

/*
 * getNumDailyOrdersEntries()
 * 
 * Retorno: num_entries (unsigned long). 
 * 
 * Essa funcao eh responsavel por obter o numero de dias no historico de pedidos feitos por dia.
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
int getNumDailyOrdersEntries() {
	FILE *output;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    unsigned long num_entries;
    strcat(app_path, "-nd");						// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 				// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	num_entries = strtoul(buffer, NULL, 10);
	pclose(output);
	return num_entries;
}

/*
 * getDailyOrdersInfo(struct daily_orders_info *info)
 * 
 * Retorno: void. 
 * 
 * Essa funcao eh responsavel por obter as informacoes armazenadas no historico de pedidos feitos. 
 * As informacoes sao: ano, mes, dia e numero de pedidos feitos nesse dia.  
 * As informacoes obtidas sao armazenadas em um ponteiro para um um array da estrutura daily_orders_info,
 * passado como argumento para essa funcao.
 * 
 * Esses valores sao obtidos utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * A rotina gera um csv (comma separated values), que eh analisado utilizando a rotina strtok().
 * */
void getDailyOrdersInfo(struct daily_orders_info *info) {
	FILE *output;
	int i=0;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;		//Caminho para executar o software auxiliar
    char buffer[BUFF_SIZE];
    char *r;
	strcat(app_path, "-d");							// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 				// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	while(fgets(buffer, BUFF_SIZE, output)) {
		r = strtok(buffer, ",");
		info[i].year = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		info[i].month = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		info[i].day = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		info[i].orders = strtoul(r, NULL, 10);
		i++;
	}
	pclose(output);
}


