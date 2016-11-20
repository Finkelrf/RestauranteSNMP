#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "lib_restaurante.h"

unsigned long get_number_tables() {
	FILE *output;
	unsigned long   number_tables=0;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
	strcat(app_path, "-n");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	fgets(buffer, 10, output);
	number_tables = strtoul(buffer, NULL, 10);
	pclose(output);
	return number_tables;
}

void get_mesas_info(struct mesa_info *mesas) {
	FILE *output;
	unsigned long   number_tables=0;
	unsigned long   mesa_num;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
    char *r;
	strcat(app_path, "-s");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output) {
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	while(fgets(buffer, 100, output)) {
		syslog(LOG_INFO, "buffer: %s", buffer);
		r = strtok(buffer, ",");
		syslog(LOG_INFO, "r= %s", r);
		mesa_num = strtoul(r, NULL, 10);
		syslog(LOG_INFO, "444");
		syslog(LOG_INFO, "%s", r);
		r = strtok(NULL, ",");
		mesas[mesa_num].num_clientes = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		mesas[mesa_num].capacidade = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		syslog(LOG_INFO, "status r = %s", r);
		mesas[mesa_num].status = atoi(r);	
		syslog(LOG_INFO, "mesa_num: %lu", mesa_num);
		syslog(LOG_INFO, "num_cliente: %lu", mesas[mesa_num].num_clientes);
		syslog(LOG_INFO, "capacidade: %lu", mesas[mesa_num].capacidade);
		syslog(LOG_INFO, "status: %d", mesas[mesa_num].status);
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

