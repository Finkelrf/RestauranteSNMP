#include <stdio.h>
#include <stdlib.h>
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
	//syslog(LOG_INFO, "1111");
	FILE *output;
	unsigned long   number_tables=0;
	unsigned long   mesa_num;
    char app_path[120] = APP_PYTHON_PATH;
    char buffer[20];
    char *r;
	strcat(app_path, "-t");
	output = popen (app_path, "r"); // Call the restaurante app, and parse the ouput
	if (!output)
	{
		syslog (LOG_INFO,"incorrect parameters or too many files.\n");
		return EXIT_FAILURE;
	}
	//syslog(LOG_INFO, "1111");
	while(fgets(buffer, 100, output)) {
		syslog(LOG_INFO, "buffer: %s", buffer);
		r = strtok(buffer, ",");
		mesa_num = strtoul(r, NULL, 10);
		syslog(LOG_INFO, "%s", r);
		r = strtok(NULL, ",");
		mesas[mesa_num].num_clientes = strtoul(r, NULL, 10);
		r = strtok(NULL, ",");
		mesas[mesa_num].capacidade = strtoul(r, NULL, 10);
		syslog(LOG_INFO, "%s", r);
		syslog(LOG_INFO, "mesa_num: %lu", mesa_num);
		syslog(LOG_INFO, "num_cliente: %lu", mesas[mesa_num].num_clientes);
		syslog(LOG_INFO, "capacidade: %lu", mesas[mesa_num].capacidade);
	}
	
	
}
