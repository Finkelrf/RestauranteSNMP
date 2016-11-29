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
#include "dailyOrdersTable.h"


/** @defgroup data_get data_get: Routines to get data
 *
 * TODO:230:M: Implement dailyOrdersTable get routines.
 * TODO:240:M: Implement dailyOrdersTable mapping routines (if any).
 *
 * These routine are used to get the value for individual objects. The
 * row context is passed, along with a pointer to the memory where the
 * value should be copied.
 *
 * @{
 */
/**********************************************************************
 **********************************************************************
 ***
 *** Table dailyOrdersTable
 ***
 **********************************************************************
 **********************************************************************/
/*
 * RestCtrl-MIB::dailyOrdersTable is subid 8 of restCtrl.
 * Its status is Current.
 * OID: .1.3.6.1.4.1.12619.8, length: 8
*/

/* ---------------------------------------------------------------------
 * TODO:200:r: Implement dailyOrdersTable data context functions.
 */


/**
 * set mib index(es)
 *
 * @param tbl_idx mib index structure
 * @param dailyOrdersIndex_val
 *
 * @retval MFD_SUCCESS     : success.
 * @retval MFD_ERROR       : other error.
 *
 * @remark
 *  This convenience function is useful for setting all the MIB index
 *  components with a single function call. It is assume that the C values
 *  have already been mapped from their native/rawformat to the MIB format.
 */
int
dailyOrdersTable_indexes_set_tbl_idx(dailyOrdersTable_mib_index *tbl_idx, long dailyOrdersIndex_val)
{
    DEBUGMSGTL(("verbose:dailyOrdersTable:dailyOrdersTable_indexes_set_tbl_idx","called\n"));

    /* dailyOrdersIndex(1)/INTEGER32/ASN_INTEGER/long(long)//l/A/w/e/R/d/h */
    tbl_idx->dailyOrdersIndex = dailyOrdersIndex_val;
    

    return MFD_SUCCESS;
} /* dailyOrdersTable_indexes_set_tbl_idx */

/**
 * @internal
 * set row context indexes
 *
 * @param reqreq_ctx the row context that needs updated indexes
 *
 * @retval MFD_SUCCESS     : success.
 * @retval MFD_ERROR       : other error.
 *
 * @remark
 *  This function sets the mib indexs, then updates the oid indexs
 *  from the mib index.
 */
int
dailyOrdersTable_indexes_set(dailyOrdersTable_rowreq_ctx *rowreq_ctx, long dailyOrdersIndex_val)
{
    DEBUGMSGTL(("verbose:dailyOrdersTable:dailyOrdersTable_indexes_set","called\n"));

    if(MFD_SUCCESS != dailyOrdersTable_indexes_set_tbl_idx(&rowreq_ctx->tbl_idx
                                   , dailyOrdersIndex_val
           ))
        return MFD_ERROR;

    /*
     * convert mib index to oid index
     */
    rowreq_ctx->oid_idx.len = sizeof(rowreq_ctx->oid_tmp) / sizeof(oid);
    if(0 != dailyOrdersTable_index_to_oid(&rowreq_ctx->oid_idx,
                                    &rowreq_ctx->tbl_idx)) {
        return MFD_ERROR;
    }

    return MFD_SUCCESS;
} /* dailyOrdersTable_indexes_set */


/*---------------------------------------------------------------------
 * RestCtrl-MIB::dailyOrdersEntry.year
 * year is subid 2 of dailyOrdersEntry.
 * Its status is Mandatory, and its access level is ReadOnly.
 * OID: .1.3.6.1.4.1.12619.8.1.2
 * Description:
Ano
 *
 * Attributes:
 *   accessible 1     isscalar 0     enums  0      hasdefval 0
 *   readable   1     iscolumn 1     ranges 1      hashint   0
 *   settable   0
 *
 * Ranges:  1 - 2147483647;
 *
 * Its syntax is INTEGER32 (based on perltype INTEGER32)
 * The net-snmp type is ASN_INTEGER. The C type decl is long (long)
 */
/**
 * Extract the current value of the year data.
 *
 * Set a value using the data context for the row.
 *
 * @param rowreq_ctx
 *        Pointer to the row request context.
 * @param year_val_ptr
 *        Pointer to storage for a long variable
 *
 * @retval MFD_SUCCESS         : success
 * @retval MFD_SKIP            : skip this node (no value for now)
 * @retval MFD_ERROR           : Any other error
 */
int
year_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * year_val_ptr )
{
   /** we should have a non-NULL pointer */
   netsnmp_assert( NULL != year_val_ptr );


    DEBUGMSGTL(("verbose:dailyOrdersTable:year_get","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

/*
 * TODO:231:o: |-> Extract the current value of the year data.
 * copy (* year_val_ptr ) from rowreq_ctx->data
 */
    (* year_val_ptr ) = rowreq_ctx->data.year;

    return MFD_SUCCESS;
} /* year_get */

/*---------------------------------------------------------------------
 * RestCtrl-MIB::dailyOrdersEntry.month
 * month is subid 3 of dailyOrdersEntry.
 * Its status is Mandatory, and its access level is ReadOnly.
 * OID: .1.3.6.1.4.1.12619.8.1.3
 * Description:
Mes
 *
 * Attributes:
 *   accessible 1     isscalar 0     enums  0      hasdefval 0
 *   readable   1     iscolumn 1     ranges 1      hashint   0
 *   settable   0
 *
 * Ranges:  1 - 2147483647;
 *
 * Its syntax is INTEGER32 (based on perltype INTEGER32)
 * The net-snmp type is ASN_INTEGER. The C type decl is long (long)
 */
/**
 * Extract the current value of the month data.
 *
 * Set a value using the data context for the row.
 *
 * @param rowreq_ctx
 *        Pointer to the row request context.
 * @param month_val_ptr
 *        Pointer to storage for a long variable
 *
 * @retval MFD_SUCCESS         : success
 * @retval MFD_SKIP            : skip this node (no value for now)
 * @retval MFD_ERROR           : Any other error
 */
int
month_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * month_val_ptr )
{
   /** we should have a non-NULL pointer */
   netsnmp_assert( NULL != month_val_ptr );


    DEBUGMSGTL(("verbose:dailyOrdersTable:month_get","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

/*
 * TODO:231:o: |-> Extract the current value of the month data.
 * copy (* month_val_ptr ) from rowreq_ctx->data
 */
    (* month_val_ptr ) = rowreq_ctx->data.month;

    return MFD_SUCCESS;
} /* month_get */

/*---------------------------------------------------------------------
 * RestCtrl-MIB::dailyOrdersEntry.day
 * day is subid 4 of dailyOrdersEntry.
 * Its status is Mandatory, and its access level is ReadOnly.
 * OID: .1.3.6.1.4.1.12619.8.1.4
 * Description:
dia
 *
 * Attributes:
 *   accessible 1     isscalar 0     enums  0      hasdefval 0
 *   readable   1     iscolumn 1     ranges 1      hashint   0
 *   settable   0
 *
 * Ranges:  1 - 2147483647;
 *
 * Its syntax is INTEGER32 (based on perltype INTEGER32)
 * The net-snmp type is ASN_INTEGER. The C type decl is long (long)
 */
/**
 * Extract the current value of the day data.
 *
 * Set a value using the data context for the row.
 *
 * @param rowreq_ctx
 *        Pointer to the row request context.
 * @param day_val_ptr
 *        Pointer to storage for a long variable
 *
 * @retval MFD_SUCCESS         : success
 * @retval MFD_SKIP            : skip this node (no value for now)
 * @retval MFD_ERROR           : Any other error
 */
int
day_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * day_val_ptr )
{
   /** we should have a non-NULL pointer */
   netsnmp_assert( NULL != day_val_ptr );


    DEBUGMSGTL(("verbose:dailyOrdersTable:day_get","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

/*
 * TODO:231:o: |-> Extract the current value of the day data.
 * copy (* day_val_ptr ) from rowreq_ctx->data
 */
    (* day_val_ptr ) = rowreq_ctx->data.day;

    return MFD_SUCCESS;
} /* day_get */

/*---------------------------------------------------------------------
 * RestCtrl-MIB::dailyOrdersEntry.orders
 * orders is subid 5 of dailyOrdersEntry.
 * Its status is Mandatory, and its access level is ReadOnly.
 * OID: .1.3.6.1.4.1.12619.8.1.5
 * Description:
Numero de pedidos do dia
 *
 * Attributes:
 *   accessible 1     isscalar 0     enums  0      hasdefval 0
 *   readable   1     iscolumn 1     ranges 1      hashint   0
 *   settable   0
 *
 * Ranges:  1 - 2147483647;
 *
 * Its syntax is INTEGER32 (based on perltype INTEGER32)
 * The net-snmp type is ASN_INTEGER. The C type decl is long (long)
 */
/**
 * Extract the current value of the orders data.
 *
 * Set a value using the data context for the row.
 *
 * @param rowreq_ctx
 *        Pointer to the row request context.
 * @param orders_val_ptr
 *        Pointer to storage for a long variable
 *
 * @retval MFD_SUCCESS         : success
 * @retval MFD_SKIP            : skip this node (no value for now)
 * @retval MFD_ERROR           : Any other error
 */
int
orders_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * orders_val_ptr )
{
   /** we should have a non-NULL pointer */
   netsnmp_assert( NULL != orders_val_ptr );


    DEBUGMSGTL(("verbose:dailyOrdersTable:orders_get","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

/*
 * TODO:231:o: |-> Extract the current value of the orders data.
 * copy (* orders_val_ptr ) from rowreq_ctx->data
 */
    (* orders_val_ptr ) = rowreq_ctx->data.orders;

    return MFD_SUCCESS;
} /* orders_get */



/** @} */