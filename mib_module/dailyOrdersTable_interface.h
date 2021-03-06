/*
 * Note: this file originally auto-generated by mib2c using
 *       version $ of $
 *
 * $Id:$
 */
/** @ingroup interface: Routines to interface to Net-SNMP
 *
 * \warning This code should not be modified, called directly,
 *          or used to interpret functionality. It is subject to
 *          change at any time.
 * 
 * @{
 */
/*
 * *********************************************************************
 * *********************************************************************
 * *********************************************************************
 * ***                                                               ***
 * ***  NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE  ***
 * ***                                                               ***
 * ***                                                               ***
 * ***       THIS FILE DOES NOT CONTAIN ANY USER EDITABLE CODE.      ***
 * ***                                                               ***
 * ***                                                               ***
 * ***       THE GENERATED CODE IS INTERNAL IMPLEMENTATION, AND      ***
 * ***                                                               ***
 * ***                                                               ***
 * ***    IS SUBJECT TO CHANGE WITHOUT WARNING IN FUTURE RELEASES.   ***
 * ***                                                               ***
 * ***                                                               ***
 * *********************************************************************
 * *********************************************************************
 * *********************************************************************
 */
#ifndef DAILYORDERSTABLE_INTERFACE_H
#define DAILYORDERSTABLE_INTERFACE_H

#ifdef __cplusplus
extern "C" {
#endif


#include "dailyOrdersTable.h"


/* ********************************************************************
 * Table declarations
 */

/* PUBLIC interface initialization routine */
void _dailyOrdersTable_initialize_interface(dailyOrdersTable_registration * user_ctx,
                                    u_long flags);
void _dailyOrdersTable_shutdown_interface(dailyOrdersTable_registration * user_ctx);

dailyOrdersTable_registration *
dailyOrdersTable_registration_get( void );

dailyOrdersTable_registration *
dailyOrdersTable_registration_set( dailyOrdersTable_registration * newreg );

netsnmp_container *dailyOrdersTable_container_get( void );
int dailyOrdersTable_container_size( void );

    dailyOrdersTable_rowreq_ctx * dailyOrdersTable_allocate_rowreq_ctx(void *);
void dailyOrdersTable_release_rowreq_ctx(dailyOrdersTable_rowreq_ctx *rowreq_ctx);

int dailyOrdersTable_index_to_oid(netsnmp_index *oid_idx,
                            dailyOrdersTable_mib_index *mib_idx);
int dailyOrdersTable_index_from_oid(netsnmp_index *oid_idx,
                              dailyOrdersTable_mib_index *mib_idx);

/*
 * access to certain internals. use with caution!
 */
void dailyOrdersTable_valid_columns_set(netsnmp_column_info *vc);


#ifdef __cplusplus
}
#endif

#endif /* DAILYORDERSTABLE_INTERFACE_H */
/** @} */
