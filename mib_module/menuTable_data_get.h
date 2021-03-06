/*
 * Note: this file originally auto-generated by mib2c using
 *       version $ of $
 *
 * $Id:$
 *
 * @file menuTable_data_get.h
 *
 * @addtogroup get
 *
 * Prototypes for get functions
 *
 * @{
 */
#ifndef MENUTABLE_DATA_GET_H
#define MENUTABLE_DATA_GET_H

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
 *** Table menuTable
 ***
 **********************************************************************
 **********************************************************************/
/*
 * RestCtrl-MIB::menuTable is subid 5 of restCtrl.
 * Its status is Current.
 * OID: .1.3.6.1.4.1.12619.5, length: 8
*/
    /*
     * indexes
     */

    int description_get( menuTable_rowreq_ctx *rowreq_ctx, char **description_val_ptr_ptr, size_t *description_val_ptr_len_ptr );


int menuTable_indexes_set_tbl_idx(menuTable_mib_index *tbl_idx, long menuIndex_val);
int menuTable_indexes_set(menuTable_rowreq_ctx *rowreq_ctx, long menuIndex_val);




#ifdef __cplusplus
}
#endif

#endif /* MENUTABLE_DATA_GET_H */
/** @} */
