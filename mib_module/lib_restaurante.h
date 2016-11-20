#include <syslog.h>
#include <unistd.h>

#define MAX_MESAS 20
#define MAX_ORDERS 100
#define APP_PYTHON_PATH "python /home/rocordoni/Documentos/gerencia/RestauranteSNMP/restaurante_app/restaurante.py "
#define CONFIG_PATH "/home/rocordoni/Documentos/gerencia/RestauranteSNMP/restaurante_app/config"

struct mesa_info {
	unsigned long capacidade;
	unsigned long num_clientes;
	int status;
};

struct order_info {
	unsigned long item;
	unsigned long table;
	int status;
	
};

unsigned long get_number_tables();
void get_mesas_info(struct mesa_info *mesas);

unsigned long get_number_orders();
void get_orders_info(struct order_info *orders);

int getRestStatus();
int setRestStatus(int status);




