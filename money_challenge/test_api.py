import frappe

@frappe.whitelist(allow_guest=True)
def test_query(item_code, warehouse):
    latest_sle = frappe.db.sql("""Select qty_after_transaction from `tabStock Ledger Entry`
            where item_code = %s and warehouse = %s order by name desc limit 1""", (item_code, warehouse))
    print latest_sle[0][0]
    return latest_sle[0][0]