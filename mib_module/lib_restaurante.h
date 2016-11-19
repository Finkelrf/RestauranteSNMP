#include <syslog.h>

#define MAX_MESAS 20
#define APP_PYTHON_PATH "python /home/rocordoni/Documentos/gerencia/RestauranteSNMP/restaurante_app/restaurante.py "

struct mesa_info {
	unsigned long capacidade;
	unsigned long num_clientes;
	int status;
};

unsigned long get_number_tables();
void get_mesas_info(struct mesa_info *mesas);
