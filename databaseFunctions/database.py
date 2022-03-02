# pip install python-dotenv
# pip install mysql-connector-python
from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os
import json

# Hiding password video: https://www.youtube.com/watch?v=YdgIWTYQ69A
load_dotenv()


def get_connection1():
    try:
        connection_pool = pooling.MySQLConnectionPool(
            pool_name = "testForPooling",
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
        connection = get_connection1()
        cursor = connection.cursor(buffered=True)
        # This is an example: cursor.execute("SELECT id, name, username FROM member WHERE username=%s", ('test',))
        cursor.execute(query,(whereValue,))
        userNameQuery = cursor.fetchall()
        return(userNameQuery)
    except Error as e:
            print("Connection failed:", e)
    finally:
        cursor.close()
        connection.close()

# # The below two are for testing purpose.
# query_1 ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE nextPage=%s;" 
# # for i in selectData(query_1, 4):
# #     print(i)

# page = 4
# data = []
# for i in selectData(query_1, page):
#     jsonToList = json.loads(i[9])
#     # print(jsontolist)
#     # print(type(jsontolist))
    
  
#     eachRow = {
#                 "images": jsontolist}
#     data.append(eachRow)
#     print(eachRow)
#     print()
# print(data)
# test11 = json.loads(data)
# test22 = {"nextPage": page, "data": data}
# print(test22)
# print(data)


# rr = ["https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000788.jpg", "https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000789.jpg", "https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000790.jpg"]
# print(type(rr))