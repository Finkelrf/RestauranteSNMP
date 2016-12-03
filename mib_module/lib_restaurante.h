#include <syslog.h>
#include <unistd.h>

#define BUFF_SIZE 20
#define MAX_SIZE 100
#define MAX_MESAS 20
#define MAX_ESTOQUE 100
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

struct estoque_item_info {
	char item_name[BUFF_SIZE];
	unsigned long amount;	
};

struct daily_orders_info {
	unsigned long year;
	unsigned long month;	
	unsigned long day;
	unsigned long orders;
};

unsigned long get_number_tables();
void get_mesas_info(struct mesa_info *mesas);

unsigned long get_number_orders();
void get_orders_info(struct order_info *orders);

int getRestStatus();
int setRestStatus(int status);

int getNumItemsEstoque();
void getEstoque(struct estoque_item_info *estoque);

int getNumDailyOrdersEntries();
void getDailyOrdersInfo(struct daily_orders_info *info);




