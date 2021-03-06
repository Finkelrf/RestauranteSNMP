/*
 * Note: this file originally auto-generated by mib2c using
 *       version $ of $ 
 *
 * $Id:$
 */
/* standard Net-SNMP includes */
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/net-snmp-features.h>
#include <net-snmp/net-snmp-includes.h>
#include <net-snmp/agent/net-snmp-agent-includes.h>

/* include our parent header */
#include "estoqueTable.h"
#include "lib_restaurante.h"


#include "estoqueTable_data_access.h"

/** @ingroup interface
 * @addtogroup data_access data_access: Routines to access data
 *
 * These routines are used to locate the data used to satisfy
 * requests.
 * 
 * @{
 */
/**********************************************************************
 **********************************************************************
 ***
 *** Table estoqueTable
 ***
 **********************************************************************
 **********************************************************************/
/*
 * RestCtrl-MIB::estoqueTable is subid 9 of restCtrl.
 * Its status is Current.
 * OID: .1.3.6.1.4.1.12619.9, length: 8
*/

/**
 * initialization for estoqueTable data access
 *
 * This function is called during startup to allow you to
 * allocate any resources you need for the data table.
 *
 * @param estoqueTable_reg
 *        Pointer to estoqueTable_registration
 *
 * @retval MFD_SUCCESS : success.
 * @retval MFD_ERROR   : unrecoverable error.
 */
int
estoqueTable_init_data(estoqueTable_registration * estoqueTable_reg)
{
    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_init_data","called\n"));

    /*
     * TODO:303:o: Initialize estoqueTable data.
     */

    return MFD_SUCCESS;
} /* estoqueTable_init_data */

/**
 * container overview
 *
 */

/**
 * container initialization
 *
 * @param container_ptr_ptr A pointer to a container pointer. If you
 *        create a custom container, use this parameter to return it
 *        to the MFD helper. If set to NULL, the MFD helper will
 *        allocate a container for you.
 * @param  cache A pointer to a cache structure. You can set the timeout
 *         and other cache flags using this pointer.
 *
 *  This function is called at startup to allow you to customize certain
 *  aspects of the access method. For the most part, it is for advanced
 *  users. The default code should suffice for most cases. If no custom
 *  container is allocated, the MFD code will create one for your.
 *
 *  This is also the place to set up cache behavior. The default, to
 *  simply set the cache timeout, will work well with the default
 *  container. If you are using a custom container, you may want to
 *  look at the cache helper documentation to see if there are any
 *  flags you want to set.
 *
 * @remark
 *  This would also be a good place to do any initialization needed
 *  for you data source. For example, opening a connection to another
 *  process that will supply the data, opening a database, etc.
 */
void
estoqueTable_container_init(netsnmp_container **container_ptr_ptr,
                             netsnmp_cache *cache)
{
    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_container_init","called\n"));
    
    if (NULL == container_ptr_ptr) {
        snmp_log(LOG_ERR,"bad container param to estoqueTable_container_init\n");
        return;
    }

    /*
     * For advanced users, you can use a custom container. If you
     * do not create one, one will be created for you.
     */
    *container_ptr_ptr = NULL;

    if (NULL == cache) {
        snmp_log(LOG_ERR,"bad cache param to estoqueTable_container_init\n");
        return;
    }

    /*
     * TODO:345:A: Set up estoqueTable cache properties.
     *
     * Also for advanced users, you can set parameters for the
     * cache. Do not change the magic pointer, as it is used
     * by the MFD helper. To completely disable caching, set
     * cache->enabled to 0.
     */
    cache->timeout = ESTOQUETABLE_CACHE_TIMEOUT; /* seconds */
} /* estoqueTable_container_init */

/**
 * container shutdown
 *
 * @param container_ptr A pointer to the container.
 *
 *  This function is called at shutdown to allow you to customize certain
 *  aspects of the access method. For the most part, it is for advanced
 *  users. The default code should suffice for most cases.
 *
 *  This function is called before estoqueTable_container_free().
 *
 * @remark
 *  This would also be a good place to do any cleanup needed
 *  for you data source. For example, closing a connection to another
 *  process that supplied the data, closing a database, etc.
 */
void
estoqueTable_container_shutdown(netsnmp_container *container_ptr)
{
    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_container_shutdown","called\n"));
    
    if (NULL == container_ptr) {
        snmp_log(LOG_ERR,"bad params to estoqueTable_container_shutdown\n");
        return;
    }

} /* estoqueTable_container_shutdown */

/**
 * load initial data
 *
 * TODO:350:M: Implement estoqueTable data load
 * This function will also be called by the cache helper to load
 * the container again (after the container free function has been
 * called to free the previous contents).
 *
 * @param container container to which items should be inserted
 *
 * @retval MFD_SUCCESS              : success.
 * @retval MFD_RESOURCE_UNAVAILABLE : Can't access data source
 * @retval MFD_ERROR                : other error.
 *
 *  This function is called to load the index(es) (and data, optionally)
 *  for the every row in the data set.
 *
 * @remark
 *  While loading the data, the only important thing is the indexes.
 *  If access to your data is cheap/fast (e.g. you have a pointer to a
 *  structure in memory), it would make sense to update the data here.
 *  If, however, the accessing the data invovles more work (e.g. parsing
 *  some other existing data, or peforming calculations to derive the data),
 *  then you can limit yourself to setting the indexes and saving any
 *  information you will need later. Then use the saved information in
 *  estoqueTable_row_prep() for populating data.
 *
 * @note
 *  If you need consistency between rows (like you want statistics
 *  for each row to be from the same time frame), you should set all
 *  data here.
 *
 */
int
estoqueTable_container_load(netsnmp_container *container)
{
	syslog(LOG_INFO, "22222");
    estoqueTable_rowreq_ctx *rowreq_ctx;
    size_t                 count = 0;

    /*
     * temporary storage for index values
     */
        /*
         * estoqueIndex(1)/INTEGER32/ASN_INTEGER/long(long)//l/A/W/e/R/d/h
         */
	long   estoqueIndex=1;
	int i=0;
	unsigned long   num_items, name_len;
	struct estoque_item_info estoque[MAX_ESTOQUE];
	num_items = getNumItemsEstoque();
	getEstoque(estoque);
    
    /*
     * this example code is based on a data source that is a
     * text file to be read and parsed.
     */

    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_container_load","called\n"));

    /*
     * TODO:351:M: |-> Load/update data in the estoqueTable container.
     * loop over your estoqueTable data, allocate a rowreq context,
     * set the index(es) [and data, optionally] and insert into
     * the container.
     */
    for(i=0; i < num_items; i++) {

        /*
         * TODO:352:M: |   |-> set indexes in new estoqueTable rowreq context.
         * data context will be set from the param (unless NULL,
         *      in which case a new data context will be allocated)
         */
        rowreq_ctx = estoqueTable_allocate_rowreq_ctx(NULL);
        if (NULL == rowreq_ctx) {
            snmp_log(LOG_ERR, "memory allocation failed\n");
            return MFD_RESOURCE_UNAVAILABLE;
        }
        else {
			if(estoque[i].amount < 100) {
				syslog(LOG_INFO, "estoque[%d], SENDING TRAP for change in amount",i);
				send_estoqueItemChange_trap(estoqueIndex, estoque[i].item_name, (unsigned long) estoque[i].amount);
			}
		}
        if(MFD_SUCCESS != estoqueTable_indexes_set(rowreq_ctx
                               , estoqueIndex
               )) {
            snmp_log(LOG_ERR,"error setting index while loading "
                     "estoqueTable data.\n");
            estoqueTable_release_rowreq_ctx(rowreq_ctx);
            continue;
        }

        /*
         * TODO:352:r: |   |-> populate estoqueTable data context.
         * Populate data context here. (optionally, delay until row prep)
         */
    /*
     * TRANSIENT or semi-TRANSIENT data:
     * copy data or save any info needed to do it in row_prep.
     */
    /*
     * setup/save data for name
     * name(2)/DisplayString/ASN_OCTET_STR/char(char)//L/A/W/e/R/d/H
     */
    /** no mapping */
    /*
     * make sure there is enough space for name data
     */
    rowreq_ctx->data.name_len = strlen(estoque[i].item_name)+1;
    strncpy( rowreq_ctx->data.name, estoque[i].item_name, rowreq_ctx->data.name_len);
    
    /*
     * setup/save data for amount
     * amount(3)/INTEGER32/ASN_INTEGER/long(long)//l/A/W/e/r/d/h
     */
    /** no mapping */
    rowreq_ctx->data.amount = estoque[i].amount;
    
        
        /*
         * insert into table container
         */
        CONTAINER_INSERT(container, rowreq_ctx);
        ++count;
        ++estoqueIndex;
    }


    DEBUGMSGT(("verbose:estoqueTable:estoqueTable_container_load",
               "inserted %d records\n", count));

    return MFD_SUCCESS;
} /* estoqueTable_container_load */

/**
 * container clean up
 *
 * @param container container with all current items
 *
 *  This optional callback is called prior to all
 *  item's being removed from the container. If you
 *  need to do any processing before that, do it here.
 *
 * @note
 *  The MFD helper will take care of releasing all the row contexts.
 *
 */
void
estoqueTable_container_free(netsnmp_container *container)
{
    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_container_free","called\n"));

    /*
     * TODO:380:M: Free estoqueTable container data.
     */
} /* estoqueTable_container_free */

/**
 * prepare row for processing.
 *
 *  When the agent has located the row for a request, this function is
 *  called to prepare the row for processing. If you fully populated
 *  the data context during the index setup phase, you may not need to
 *  do anything.
 *
 * @param rowreq_ctx pointer to a context.
 *
 * @retval MFD_SUCCESS     : success.
 * @retval MFD_ERROR       : other error.
 */
int
estoqueTable_row_prep( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_row_prep","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:390:o: Prepare row for request.
     * If populating row data was delayed, this is the place to
     * fill in the row for this request.
     */

    return MFD_SUCCESS;
} /* estoqueTable_row_prep */

/** @} */
