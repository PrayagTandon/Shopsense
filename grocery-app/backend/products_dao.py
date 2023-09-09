import mysql.connector


def get_all_products():
    cnx = mysql.connector.connect(
        user="root", password="Pray@#2010", host="127.0.0.1", database="shopsense"
    )

    cursor = cnx.cursor()

    query = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom_table.uom_name FROM shopsense.products inner join shopsense.uom_table on products.uom_id=uom_table.uom_id"

    cursor.execute(query)

    response = []

    for product_id, name, uom_id, price_per_unit, uom_name in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "uom_id": uom_id,
                "price_per_unit": price_per_unit,
                "uom_name": uom_name,
            }
        )

    cnx.close()

    return response
