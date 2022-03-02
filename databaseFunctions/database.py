# pip install python-dotenv
# pip install mysql-connector-python
from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os
import json

# Hiding password video: https://www.youtube.com/watch?v=YdgIWTYQ69A
load_dotenv()

def pickOneConnection():
    try:
        connection_pool = pooling.MySQLConnectionPool(
            pool_name = "myWeHelpPool",
            pool_size = 5,
            pool_reset_session = True,
            host = "localhost",
            database = "website",
            user = "root",
            passwd = os.getenv("passwd")

        )
        connection = connection_pool.get_connection()
        return connection
    except Error as e:
        print("Connection failed:", e)
        
        
# ========================================#
def selectData(query, whereValue):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        # This is an example: cursor.execute("SELECT id, name, username FROM member WHERE username=%s", ('test',))
        cursor.execute(query,(whereValue,))
        userNameQuery = cursor.fetchall()
        return(userNameQuery)
    except Error as e:
            print("Connection failed:", e)
    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()

# # The below two are for testing purpose.
# query_1 ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE nextPage=%s;" 
# for i in selectData(query_1, 4):
#     print(i)