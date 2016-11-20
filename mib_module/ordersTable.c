/*
 * Note: this file originally auto-generated by mib2c using
 *       version $ of $ 
 *
 * $Id:$
 */
/** \page MFD helper for ordersTable
 *
 * \section intro Introduction
 * Introductory text.
 *
 */
/* standard Net-SNMP includes */
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/net-snmp-features.h>
#include <net-snmp/net-snmp-includes.h>
#include <net-snmp/agent/net-snmp-agent-includes.h>

/* include our parent header */
#include "ordersTable.h"

#include <net-snmp/agent/mib_modules.h>

#include "ordersTable_interface.h"

const oid ordersTable_oid[] = { ORDERSTABLE_OID };
const int ordersTable_oid_size = OID_LENGTH(ordersTable_oid);

    ordersTable_registration  ordersTable_user_context;

void initialize_table_ordersTable(void);
void shutdown_table_ordersTable(void);


/**
 * Initializes the ordersTable module
 */
void
init_ordersTable(void)
{
    DEBUGMSGTL(("verbose:ordersTable:init_ordersTable","called\n"));

    /*
     * TODO:300:o: Perform ordersTable one-time module initialization.
     */
     
    /*
     * here we initialize all the tables we're planning on supporting
     */
    if (should_init("ordersTable"))
        initialize_table_ordersTable();

} /* init_ordersTable */

/**
 * Shut-down the ordersTable module (agent is exiting)
 */
void
shutdown_ordersTable(void)
{
    if (should_init("ordersTable"))
        shutdown_table_ordersTable();

}

/**
 * Initialize the table ordersTable 
 *    (Define its contents and how it's structured)
 */
void
initialize_table_ordersTable(void)
{
    ordersTable_registration * user_context;
    u_long flags;

    DEBUGMSGTL(("verbose:ordersTable:initialize_table_ordersTable","called\n"));

    /*
     * TODO:301:o: Perform ordersTable one-time table initialization.
     */

    /*
     * TODO:302:o: |->Initialize ordersTable user context
     * if you'd like to pass in a pointer to some data for this
     * table, allocate or set it up here.
     */
    /*
     * a netsnmp_data_list is a simple way to store void pointers. A simple
     * string token is used to add, find or remove pointers.
     */
    user_context = netsnmp_create_data_list("ordersTable", NULL, NULL);
    
    /*
     * No support for any flags yet, but in the future you would
     * set any flags here.
     */
    flags = 0;
    
    /*
     * call interface initialization code
     */
    _ordersTable_initialize_interface(user_context, flags);
} /* initialize_table_ordersTable */

/**
 * Shutdown the table ordersTable 
 */
void
shutdown_table_ordersTable(void)
{
    /*
     * call interface shutdown code
     */
    _ordersTable_shutdown_interface(&ordersTable_user_context);
}

/**
 * extra context initialization (eg default values)
 *
 * @param rowreq_ctx    : row request context
 * @param user_init_ctx : void pointer for user (parameter to rowreq_ctx_allocate)
 *
 * @retval MFD_SUCCESS  : no errors
 * @retval MFD_ERROR    : error (context allocate will fail)
 */
int
ordersTable_rowreq_ctx_init(ordersTable_rowreq_ctx *rowreq_ctx,
                           void *user_init_ctx)
{
    DEBUGMSGTL(("verbose:ordersTable:ordersTable_rowreq_ctx_init","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);
    
    /*
     * TODO:210:o: |-> Perform extra ordersTable rowreq initialization. (eg DEFVALS)
     */

    return MFD_SUCCESS;
} /* ordersTable_rowreq_ctx_init */

/**
 * extra context cleanup
 *
 */
void ordersTable_rowreq_ctx_cleanup(ordersTable_rowreq_ctx *rowreq_ctx)
{
    DEBUGMSGTL(("verbose:ordersTable:ordersTable_rowreq_ctx_cleanup","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);
    
    /*
     * TODO:211:o: |-> Perform extra ordersTable rowreq cleanup.
     */
} /* ordersTable_rowreq_ctx_cleanup */

/**
 * pre-request callback
 *
 *
 * @retval MFD_SUCCESS              : success.
 * @retval MFD_ERROR                : other error
 */
int
ordersTable_pre_request(ordersTable_registration * user_context)
{
    DEBUGMSGTL(("verbose:ordersTable:ordersTable_pre_request","called\n"));

    /*
     * TODO:510:o: Perform ordersTable pre-request actions.
     */

    return MFD_SUCCESS;
} /* ordersTable_pre_request */

/**
 * post-request callback
 *
 * Note:
 *   New rows have been inserted into the container, and
 *   deleted rows have been removed from the container and
 *   released.
 *
 * @param user_context
 * @param rc : MFD_SUCCESS if all requests succeeded
 *
 * @retval MFD_SUCCESS : success.
 * @retval MFD_ERROR   : other error (ignored)
 */
int
ordersTable_post_request(ordersTable_registration * user_context, int rc)
{
    DEBUGMSGTL(("verbose:ordersTable:ordersTable_post_request","called\n"));

    /*
     * TODO:511:o: Perform ordersTable post-request actions.
     */

    return MFD_SUCCESS;
} /* ordersTable_post_request */


/** @{ */