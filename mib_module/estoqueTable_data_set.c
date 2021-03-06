/*
 * Note: this file originally auto-generated by mib2c using
 *       version $ of $
 *
 * $Id:$
 *
 */
/* standard Net-SNMP includes */
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/net-snmp-features.h>
#include <net-snmp/net-snmp-includes.h>
#include <net-snmp/agent/net-snmp-agent-includes.h>

/* include our parent header */
#include "estoqueTable.h"


/** @defgroup data_set data_set: Routines to set data
 *
 * These routines are used to set the value for individual objects. The
 * row context is passed, along with the new value.
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
    /*
     * NOTE: if you update this chart, please update the versions in
     *       local/mib2c-conf.d/parent-set.m2i
     *       agent/mibgroup/helpers/baby_steps.c
     * while you're at it.
     */
    /*
     ***********************************************************************
     * Baby Steps Flow Chart (2004.06.05)                                  *
     *                                                                     *
     * +--------------+    +================+    U = unconditional path    *
     * |optional state|    ||required state||    S = path for success      *
     * +--------------+    +================+    E = path for error        *
     ***********************************************************************
     *
     *                        +--------------+
     *                        |     pre      |
     *                        |   request    |
     *                        +--------------+
     *                               | U
     *                        +==============+
     *       +----------------||  object    ||
     *       |              E ||  lookup    ||
     *       |                +==============+
     *       |                       | S
     *       |                +==============+
     *       |              E ||   check    ||
     *       |<---------------||   values   ||
     *       |                +==============+
     *       |                       | S
     *       |                +==============+
     *       |       +<-------||   undo     ||
     *       |       |      E ||   setup    ||
     *       |       |        +==============+
     *       |       |               | S
     *       |       |        +==============+
     *       |       |        ||    set     ||-------------------------->+
     *       |       |        ||   value    || E                         |
     *       |       |        +==============+                           |
     *       |       |               | S                                 |
     *       |       |        +--------------+                           |
     *       |       |        |    check     |-------------------------->|
     *       |       |        |  consistency | E                         |
     *       |       |        +--------------+                           |
     *       |       |               | S                                 |
     *       |       |        +==============+         +==============+  |
     *       |       |        ||   commit   ||-------->||     undo   ||  |
     *       |       |        ||            || E       ||    commit  ||  |
     *       |       |        +==============+         +==============+  |
     *       |       |               | S                     U |<--------+
     *       |       |        +--------------+         +==============+
     *       |       |        | irreversible |         ||    undo    ||
     *       |       |        |    commit    |         ||     set    ||
     *       |       |        +--------------+         +==============+
     *       |       |               | U                     U |
     *       |       +-------------->|<------------------------+
     *       |                +==============+
     *       |                ||   undo     ||
     *       |                ||  cleanup   ||
     *       |                +==============+
     *       +---------------------->| U
     *                        +--------------+
     *                        |    post      |
     *                        |   request    |
     *                        +--------------+
     *
     */

/**
 * Setup up context with information needed to undo a set request.
 *
 * This function will be called before the individual node undo setup
 * functions are called. If you need to do any undo setup that is not
 * related to a specific column, you can do it here.
 *
 * Note that the undo context has been allocated with
 * estoqueTable_allocate_data(), but may need extra
 * initialization similar to what you may have done in
 * estoqueTable_rowreq_ctx_init().
 * Note that an individual node's undo_setup function will only be called
 * if that node is being set to a new value.
 *
 * If there is any setup specific to a particular column (e.g. allocating
 * memory for a string), you should do that setup in the node's undo_setup
 * function, so it won't be done unless it is necessary.
 *
 * @param rowreq_ctx
 *        Pointer to the table context (estoqueTable_rowreq_ctx)
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error. set will fail.
 */
int
estoqueTable_undo_setup( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    int rc = MFD_SUCCESS;

    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_undo_setup","called\n"));

    /** we should have a non-NULL pointer */
    netsnmp_assert( NULL != rowreq_ctx );

    /*
     * TODO:451:M: |-> Setup estoqueTable undo.
     * set up estoqueTable undo information, in preparation for a set.
     * Undo storage is in (* amount_val_ptr )*
     */

    return rc;
} /* estoqueTable_undo_setup */

/**
 * Undo a set request.
 *
 * This function will be called before the individual node undo
 * functions are called. If you need to do any undo that is not
 * related to a specific column, you can do it here.
 *
 * Note that an individual node's undo function will only be called
 * if that node is being set to a new value.
 *
 * If there is anything  specific to a particular column (e.g. releasing
 * memory for a string), you should do that setup in the node's undo
 * function, so it won't be done unless it is necessary.
 *
 * @param rowreq_ctx
 *        Pointer to the table context (estoqueTable_rowreq_ctx)
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error. set will fail.
 */
int
estoqueTable_undo( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    int rc = MFD_SUCCESS;

    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_undo","called\n"));

    /** we should have a non-NULL pointer */
    netsnmp_assert( NULL != rowreq_ctx );

    /*
     * TODO:451:M: |-> estoqueTable undo.
     * estoqueTable undo information, in response to a failed set.
     * Undo storage is in (* amount_val_ptr )*
     */

    return rc;
} /* estoqueTable_undo_setup */

/**
 * Cleanup up context undo information.
 *
 * This function will be called after set/commit processing. If you
 * allocated any resources in undo_setup, this is the place to release
 * those resources.
 *
 * This function is called regardless of the success or failure of the set
 * request. If you need to perform different steps for cleanup depending
 * on success or failure, you can add a flag to the rowreq_ctx.
 *
 * @param rowreq_ctx
 *        Pointer to the table context (estoqueTable_rowreq_ctx)
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error
 */
int
estoqueTable_undo_cleanup( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    int rc = MFD_SUCCESS;

    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_undo_cleanup","called\n"));

    /** we should have a non-NULL pointer */
    netsnmp_assert( NULL != rowreq_ctx );

    /*
     * TODO:452:M: |-> Cleanup estoqueTable undo.
     * Undo storage is in (* amount_val_ptr )*
     */

    return rc;
} /* estoqueTable_undo_cleanup */

/**
 * commit new values.
 *
 * At this point, you should have done everything you can to ensure that
 * this commit will not fail.
 *
 * Should you need different behavior depending on which columns were
 * set, rowreq_ctx->column_set_flags will indicate which writeable columns were
 * set. The definitions for the COLUMN_*_FLAG bits can be found in
 * estoqueTable_oids.h.
 * A new row will have the MFD_ROW_CREATED bit set in rowreq_flags.
 *
 * @param estoqueTable_rowreq_ctx
 *        Pointer to the users context.
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error
 */
int
estoqueTable_commit( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    int rc = MFD_SUCCESS;
    int             save_flags;

    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_commit","called\n"));

    /** we should have a non-NULL pointer */
    netsnmp_assert( NULL != rowreq_ctx );

    /*
     * save flags, then clear until we actually do something
     */
    save_flags = rowreq_ctx->column_set_flags;
    rowreq_ctx->column_set_flags = 0;

    /*
     * commit estoqueTable data
     * 1) check the column's flag in save_flags to see if it was set.
     * 2) clear the flag when you handle that column
     * 3) set the column's flag in column_set_flags if it needs undo
     *    processing in case of a failure.
     */
    if (save_flags & COLUMN_NAME_FLAG) {
       save_flags &= ~COLUMN_NAME_FLAG; /* clear name */
       /*
        * TODO:482:o: |-> commit column name.
        */
       rc = -1;
       if(-1 == rc) {
           snmp_log(LOG_ERR,"estoqueTable column name commit failed\n");
       }
       else {
            /*
             * set flag, in case we need to undo name
             */
            rowreq_ctx->column_set_flags |= COLUMN_NAME_FLAG;
       }
    }

    if (save_flags & COLUMN_AMOUNT_FLAG) {
       save_flags &= ~COLUMN_AMOUNT_FLAG; /* clear amount */
       /*
        * TODO:482:o: |-> commit column amount.
        */
       rc = -1;
       if(-1 == rc) {
           snmp_log(LOG_ERR,"estoqueTable column amount commit failed\n");
       }
       else {
            /*
             * set flag, in case we need to undo amount
             */
            rowreq_ctx->column_set_flags |= COLUMN_AMOUNT_FLAG;
       }
    }

    /*
     * if we successfully commited this row, set the dirty flag.
     */
    if (MFD_SUCCESS == rc) {
        rowreq_ctx->rowreq_flags |= MFD_ROW_DIRTY;
    }

    if (save_flags) {
       snmp_log(LOG_ERR, "unhandled columns (0x%x) in commit\n", save_flags);
       return MFD_ERROR;
    }

    return rc;
} /* estoqueTable_commit */

/**
 * undo commit new values.
 *
 * Should you need different behavior depending on which columns were
 * set, rowreq_ctx->column_set_flags will indicate which writeable columns were
 * set. The definitions for the COLUMN_*_FLAG bits can be found in
 * estoqueTable_oids.h.
 * A new row will have the MFD_ROW_CREATED bit set in rowreq_flags.
 *
 * @param estoqueTable_rowreq_ctx
 *        Pointer to the users context.
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error
 */
int
estoqueTable_undo_commit( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    int rc = MFD_SUCCESS;

    DEBUGMSGTL(("verbose:estoqueTable:estoqueTable_undo_commit","called\n"));

    /** we should have a non-NULL pointer */
    netsnmp_assert( NULL != rowreq_ctx );

    /*
     * TODO:485:M: |-> Undo estoqueTable commit.
     * check the column's flag in rowreq_ctx->column_set_flags to see
     * if it was set during commit, then undo it.
     *
     * eg: if (rowreq_ctx->column_set_flags & COLUMN__FLAG) {}
     */

    
    /*
     * if we successfully un-commited this row, clear the dirty flag.
     */
    if (MFD_SUCCESS == rc) {
        rowreq_ctx->rowreq_flags &= ~MFD_ROW_DIRTY;
    }

    return rc;
} /* estoqueTable_undo_commit */

/*
 * TODO:440:M: Implement estoqueTable node value checks.
 * TODO:450:M: Implement estoqueTable undo functions.
 * TODO:460:M: Implement estoqueTable set functions.
 * TODO:480:M: Implement estoqueTable commit functions.
 */
/*---------------------------------------------------------------------
 * RestCtrl-MIB::estoqueEntry.name
 * name is subid 2 of estoqueEntry.
 * Its status is Mandatory, and its access level is ReadWrite.
 * OID: .1.3.6.1.4.1.12619.9.1.2
 * Description:
Descricao do item
 *
 * Attributes:
 *   accessible 1     isscalar 0     enums  0      hasdefval 0
 *   readable   1     iscolumn 1     ranges 1      hashint   1
 *   settable   1
 *   hint: 255a
 *
 * Ranges:  0 - 255;
 *
 * Its syntax is DisplayString (based on perltype OCTETSTR)
 * The net-snmp type is ASN_OCTET_STR. The C type decl is char (char)
 * This data type requires a length.  (Max 255)
 */
/**
 * Check that the proposed new value is potentially valid.
 *
 * @param rowreq_ctx
 *        Pointer to the row request context.
 * @param name_val_ptr
 *        A char containing the new value.
 * @param name_val_ptr_len
 *        The size (in bytes) of the data pointed to by name_val_ptr
 *
 * @retval MFD_SUCCESS        : incoming value is legal
 * @retval MFD_NOT_VALID_NOW  : incoming value is not valid now
 * @retval MFD_NOT_VALID_EVER : incoming value is never valid
 *
 * This is the place to check for requirements that are not
 * expressed in the mib syntax (for example, a requirement that
 * is detailed in the description for an object).
 *
 * You should check that the requested change between the undo value and the
 * new value is legal (ie, the transistion from one value to another
 * is legal).
 *      
 *@note
 * This check is only to determine if the new value
 * is \b potentially valid. This is the first check of many, and
 * is one of the simplest ones.
 * 
 *@note
 * this is not the place to do any checks for values
 * which depend on some other value in the mib. Those
 * types of checks should be done in the
 * estoqueTable_check_dependencies() function.
 *
 * The following checks have already been done for you:
 *    The syntax is ASN_OCTET_STR
 *    The length is < sizeof(rowreq_ctx->data.name).
 *    The length is in (one of) the range set(s):  0 - 255
 *
 * If there a no other checks you need to do, simply return MFD_SUCCESS.
 *
 */
int
name_check_value( estoqueTable_rowreq_ctx *rowreq_ctx, char *name_val_ptr,  size_t name_val_ptr_len)
{
    DEBUGMSGTL(("verbose:estoqueTable:name_check_value","called\n"));

    /** should never get a NULL pointer */
    netsnmp_assert(NULL != rowreq_ctx);
    netsnmp_assert(NULL != name_val_ptr);

    /*
     * TODO:441:o: |-> Check for valid name value.
     */

    return MFD_SUCCESS; /* name value not illegal */
} /* name_check_value */

/**
 * Save old value information
 *
 * @param rowreq_ctx
 *        Pointer to the table context (estoqueTable_rowreq_ctx)
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error. set will fail.
 *
 * This function will be called after the table level undo setup function
 * estoqueTable_undo_setup has been called.
 *
 *@note
 * this function will only be called if a new value is set for this column.
 *
 * If there is any setup specific to a particular column (e.g. allocating
 * memory for a string), you should do that setup in this function, so it
 * won't be done unless it is necessary.
 */
int
name_undo_setup( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    DEBUGMSGTL(("verbose:estoqueTable:name_undo_setup","called\n"));

    /** should never get a NULL pointer */
    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:455:o: |-> Setup name undo.
     */
    /*
     * copy name and name_len data
     * set rowreq_ctx->undo->name from rowreq_ctx->data.name
     */
    memcpy( rowreq_ctx->undo->name, rowreq_ctx->data.name,
            (rowreq_ctx->data.name_len * sizeof(rowreq_ctx->undo->name[0])));
    rowreq_ctx->undo->name_len = rowreq_ctx->data.name_len;


    return MFD_SUCCESS;
} /* name_undo_setup */

/**
 * Set the new value.
 *
 * @param rowreq_ctx
 *        Pointer to the users context. You should know how to
 *        manipulate the value from this object.
 * @param name_val_ptr
 *        A char containing the new value.
 * @param name_val_ptr_len
 *        The size (in bytes) of the data pointed to by name_val_ptr
 */
int
name_set( estoqueTable_rowreq_ctx *rowreq_ctx, char *name_val_ptr,  size_t name_val_ptr_len )
{

    DEBUGMSGTL(("verbose:estoqueTable:name_set","called\n"));

    /** should never get a NULL pointer */
    netsnmp_assert(NULL != rowreq_ctx);
    netsnmp_assert(NULL != name_val_ptr);

    /*
     * TODO:461:M: |-> Set name value.
     * set name value in rowreq_ctx->data
     */
    memcpy( rowreq_ctx->data.name, name_val_ptr, name_val_ptr_len );
    /** convert bytes to number of char */
    rowreq_ctx->data.name_len = name_val_ptr_len / sizeof(name_val_ptr[0]);

    return MFD_SUCCESS;
} /* name_set */

/**
 * undo the previous set.
 *
 * @param rowreq_ctx
 *        Pointer to the users context.
 */
int
name_undo( estoqueTable_rowreq_ctx *rowreq_ctx)
{

    DEBUGMSGTL(("verbose:estoqueTable:name_undo","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:456:o: |-> Clean up name undo.
     */
    /*
     * copy name and name_len data
     * set rowreq_ctx->data.name from rowreq_ctx->undo->name
     */
    memcpy( rowreq_ctx->data.name, rowreq_ctx->undo->name,
            (rowreq_ctx->undo->name_len * sizeof(rowreq_ctx->data.name[0])));
    rowreq_ctx->data.name_len = rowreq_ctx->undo->name_len;

    
    return MFD_SUCCESS;
} /* name_undo */

/*---------------------------------------------------------------------
 * RestCtrl-MIB::estoqueEntry.amount
 * amount is subid 3 of estoqueEntry.
 * Its status is Mandatory, and its access level is ReadWrite.
 * OID: .1.3.6.1.4.1.12619.9.1.3
 * Description:
Quantidade ainda disponivel, em kg
 *
 * Attributes:
 *   accessible 1     isscalar 0     enums  0      hasdefval 0
 *   readable   1     iscolumn 1     ranges 0      hashint   0
 *   settable   1
 *
 *
 * Its syntax is INTEGER32 (based on perltype INTEGER32)
 * The net-snmp type is ASN_INTEGER. The C type decl is long (long)
 */
/**
 * Check that the proposed new value is potentially valid.
 *
 * @param rowreq_ctx
 *        Pointer to the row request context.
 * @param amount_val
 *        A long containing the new value.
 *
 * @retval MFD_SUCCESS        : incoming value is legal
 * @retval MFD_NOT_VALID_NOW  : incoming value is not valid now
 * @retval MFD_NOT_VALID_EVER : incoming value is never valid
 *
 * This is the place to check for requirements that are not
 * expressed in the mib syntax (for example, a requirement that
 * is detailed in the description for an object).
 *
 * You should check that the requested change between the undo value and the
 * new value is legal (ie, the transistion from one value to another
 * is legal).
 *      
 *@note
 * This check is only to determine if the new value
 * is \b potentially valid. This is the first check of many, and
 * is one of the simplest ones.
 * 
 *@note
 * this is not the place to do any checks for values
 * which depend on some other value in the mib. Those
 * types of checks should be done in the
 * estoqueTable_check_dependencies() function.
 *
 * The following checks have already been done for you:
 *    The syntax is ASN_INTEGER
 *
 * If there a no other checks you need to do, simply return MFD_SUCCESS.
 *
 */
int
amount_check_value( estoqueTable_rowreq_ctx *rowreq_ctx, long amount_val)
{
    DEBUGMSGTL(("verbose:estoqueTable:amount_check_value","called\n"));

    /** should never get a NULL pointer */
    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:441:o: |-> Check for valid amount value.
     */

    return MFD_SUCCESS; /* amount value not illegal */
} /* amount_check_value */

/**
 * Save old value information
 *
 * @param rowreq_ctx
 *        Pointer to the table context (estoqueTable_rowreq_ctx)
 *
 * @retval MFD_SUCCESS : success
 * @retval MFD_ERROR   : error. set will fail.
 *
 * This function will be called after the table level undo setup function
 * estoqueTable_undo_setup has been called.
 *
 *@note
 * this function will only be called if a new value is set for this column.
 *
 * If there is any setup specific to a particular column (e.g. allocating
 * memory for a string), you should do that setup in this function, so it
 * won't be done unless it is necessary.
 */
int
amount_undo_setup( estoqueTable_rowreq_ctx *rowreq_ctx)
{
    DEBUGMSGTL(("verbose:estoqueTable:amount_undo_setup","called\n"));

    /** should never get a NULL pointer */
    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:455:o: |-> Setup amount undo.
     */
    /*
     * copy amount data
     * set rowreq_ctx->undo->amount from rowreq_ctx->data.amount
     */
    rowreq_ctx->undo->amount = rowreq_ctx->data.amount;


    return MFD_SUCCESS;
} /* amount_undo_setup */

/**
 * Set the new value.
 *
 * @param rowreq_ctx
 *        Pointer to the users context. You should know how to
 *        manipulate the value from this object.
 * @param amount_val
 *        A long containing the new value.
 */
int
amount_set( estoqueTable_rowreq_ctx *rowreq_ctx, long amount_val )
{

    DEBUGMSGTL(("verbose:estoqueTable:amount_set","called\n"));

    /** should never get a NULL pointer */
    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:461:M: |-> Set amount value.
     * set amount value in rowreq_ctx->data
     */
    rowreq_ctx->data.amount = amount_val;

    return MFD_SUCCESS;
} /* amount_set */

/**
 * undo the previous set.
 *
 * @param rowreq_ctx
 *        Pointer to the users context.
 */
int
amount_undo( estoqueTable_rowreq_ctx *rowreq_ctx)
{

    DEBUGMSGTL(("verbose:estoqueTable:amount_undo","called\n"));

    netsnmp_assert(NULL != rowreq_ctx);

    /*
     * TODO:456:o: |-> Clean up amount undo.
     */
    /*
     * copy amount data
     * set rowreq_ctx->data.amount from rowreq_ctx->undo->amount
     */
    rowreq_ctx->data.amount = rowreq_ctx->undo->amount;

    
    return MFD_SUCCESS;
} /* amount_undo */

/** @} */
