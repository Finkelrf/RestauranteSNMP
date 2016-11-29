#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "lib_restaurante.h"

/*
 * get_number_tables()
 * 
 * Retorno: number_tables (unsignd long). 
 * 
 * Essa funcao eh responsavel por obter o numero total de mesas do restaurante.
 * Esse valor eh obtido utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
unsigned long get_number_tables() {
	FILE *output;
	unsigned long   number_tables=0;
    char app_path[120] = APP_PYTHON_PATH;	//Caminho para executar o software auxiliar
    char buffer[20];
	strcat(app_path, "-n");					// Concatena na string o argumento necessario para o software auxiliar
	output = popen (app_path, "r"); 		// Faz a chamada ao aplicativo, e analisa o resultado
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, 10, output);
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
 * a capacidade total dela e tambem o status (livre, ocupada, indisponivel ou reservada).
 * As informacoes obtidas sao armazenadas em um ponteiro para um um array da estrutura mesa_info,
 * passado como argumento para essa funcao.
 * 
 * Esses valore sao obtidos utilizando um aplicativo auxiliar. Esse software eh invocado 
 * atraves da rotina popen().
 * */
void get_mesas_info(struct mesa_info *mesas) {
	FILE *output;
	unsigned long   number_tables=0;
	unsigned long   mesa_num;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[BUFF_SIZE];
    char *r;
	strcat(app_path, "-s");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	while(fgets(buffer, BUFF_SIZE, output)) {
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

unsigned long get_number_orders() {
	FILE *output;
	unsigned long   number_orders=0;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
	strcat(app_path, "-np");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, 10, output);
	number_orders = strtoul(buffer, NULL, 10);
	pclose(output);
	return number_orders;
}

void get_orders_info(struct order_info *orders) {
	FILE *output;
	unsigned long   number_tables=0;
	unsigned long   mesa_num, item;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
    char *r;
    int i, status;
	strcat(app_path, "-p");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	i = 0;
	while(fgets(buffer, 100, output)) {
		syslog(LOG_INFO, "buffer: %s", buffer);
		r = strtok(buffer, ",");
		mesa_num = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		item = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		status = atoi(r);
		orders[i].table = mesa_num;
		orders[i].item = item;
		orders[i].status = status;
		syslog(LOG_INFO, "Table: %lu", mesa_num);
		syslog(LOG_INFO, "item: %lu", item);
		syslog(LOG_INFO, "Status: %d", status);
		i++;
	}
	pclose(output);
}

unsigned long getNumFunc() {
    FILE *output;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
    unsigned long num_func;
    strcat(app_path, "-f");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, 10, output);
	num_func = strtoul(buffer, NULL, 10);
	pclose(output);
	return num_func;

}

int getRestStatus() {
	FILE *f;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
    int status;
    char *r;
    char path[500];
	strncpy(path, CONFIG_PATH, sizeof(path));
	strncat(path,"/rest.conf",sizeof(path));
	f = fopen(path, "r");
	if (!f) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, 10, f);
	r = strtok(buffer, "=");
	r = strtok(NULL, "=");
	status = atoi(r);
	fclose(f);
	return status;
}

int setRestStatus(int status) {
	FILE *f;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
    char path[500];
	strncpy(path, CONFIG_PATH, sizeof(path));
	strncat(path,"/rest.conf",sizeof(path));
	syslog(LOG_INFO, "%s", path);
	f = fopen(path, "r+");
	if (!f) {
		syslog (LOG_INFO,"errno: %s", strerror(errno));
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fprintf(f, "status=%d",status); 
	fclose(f);
	return status;
}

int getNumItemsEstoque() {
	FILE *output;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;
    char buffer[BUFF_SIZE];
    unsigned long num_items;
    strcat(app_path, "-ne");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	num_items = strtoul(buffer, NULL, 10);
	pclose(output);
	return num_items;
}

void getEstoque(struct estoque_item_info *estoque) {
	FILE *output;
	int i=0;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;
    char buffer[BUFF_SIZE];
    char *r;
	strcat(app_path, "-e");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	while(fgets(buffer, BUFF_SIZE, output)) {
		r = strtok(buffer, ",");
		strncpy(estoque[i].item_name, r, BUFF_SIZE);
		r = strtok(NULL, ",");
		estoque[i].amount = strtoul(r, NULL, 10);
		//syslog(LOG_INFO, "item_name: %s", estoque[i].item_name);
		//syslog(LOG_INFO, "amount: %lu", estoque[i].amount );
		i++;
	}
	pclose(output);
}

int getNumDailyOrdersEntries() {
	FILE *output;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;
    char buffer[BUFF_SIZE];
    unsigned long num_entries;
    strcat(app_path, "-nd");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, BUFF_SIZE, output);
	num_entries = strtoul(buffer, NULL, 10);
	pclose(output);
	return num_entries;
}

void getDailyOrdersInfo(struct daily_orders_info *info) {
	FILE *output;
	int i=0;
    char app_path[MAX_SIZE] = APP_PYTHON_PATH;
    char buffer[BUFF_SIZE];
    char *r;
	strcat(app_path, "-d");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
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
		syslog(LOG_INFO, "year: %lu", info[i].year);
		syslog(LOG_INFO, "month: %lu", info[i].month);
		syslog(LOG_INFO, "day: %lu", info[i].day);
		syslog(LOG_INFO, "orders: %lu", info[i].orders);
		i++;
	}
	pclose(output);
}


