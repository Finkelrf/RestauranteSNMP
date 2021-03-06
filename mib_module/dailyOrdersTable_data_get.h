/*
 * Note: this file originally auto-generated by mib2c using
 *       version $ of $
 *
 * $Id:$
 *
 * @file dailyOrdersTable_data_get.h
 *
 * @addtogroup get
 *
 * Prototypes for get functions
 *
 * @{
 */
#ifndef DAILYORDERSTABLE_DATA_GET_H
#define DAILYORDERSTABLE_DATA_GET_H

#ifdef __cplusplus
extern "C" {
#endif

/* *********************************************************************
 * GET function declarations
 */

/* *********************************************************************
 * GET Table declarations
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
    /*
     * indexes
     */

    int year_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * year_val_ptr );
    int month_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * month_val_ptr );
    int day_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * day_val_ptr );
    int orders_get( dailyOrdersTable_rowreq_ctx *rowreq_ctx, long * orders_val_ptr );


int dailyOrdersTable_indexes_set_tbl_idx(dailyOrdersTable_mib_index *tbl_idx, long dailyOrdersIndex_val);
int dailyOrdersTable_indexes_set(dailyOrdersTable_rowreq_ctx *rowreq_ctx, long dailyOrdersIndex_val);




#ifdef __cplusplus
}
#endif

#endif /* DAILYORDERSTABLE_DATA_GET_H */
/** @} */
