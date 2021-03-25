import pymysql.cursors
import pymysql

# Connect to the database

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='ega_orders',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor=connection.cursor() 

def get_order_status(order_number):
    # Read a single record
    sql = "SELECT `order_status` FROM `orders` WHERE `order_id`=%s"
    cursor.execute(sql, (int(order_number),))
    result = cursor.fetchone()
    if result is not None:
        return result['order_status']
    else:
        return None    


def get_eta_status(order_number):
    # Read a single record
    sql = "SELECT `eta` FROM `orders` WHERE `order_id`=%s"
    cursor.execute(sql, (int(order_number),))
    result = cursor.fetchone()
    if result is not None:
        return result['eta']
    else:
        return None 

def get_ets_status(order_number):
    # Read a single record
    sql = "SELECT `ets` FROM `orders` WHERE `order_id`=%s"
    cursor.execute(sql, (int(order_number),))
    result = cursor.fetchone()
    if result is not None:
        return result['ets']
    else:
        return None 

def get_order_value(order_number):
    # Read a single record
    sql = "SELECT `order_value` FROM `orders` WHERE `order_id`=%s"
    cursor.execute(sql, (int(order_number),))
    result = cursor.fetchone()
    if result is not None:
        return result['order_value']
    else:
        return None 

    

