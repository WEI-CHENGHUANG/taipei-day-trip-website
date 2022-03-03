# pip install python-dotenv
# pip install mysql-connector-python
from flask import jsonify
from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os, json


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
        return {"error": True, "message": e}, 500
        
        
# ========================================#

def queryOneCaluse(query, offset):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, (offset,))
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return {"error": True, "message": e}, 500

    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()


def queryKeyword(query, keyword, page):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, (keyword, page))
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return {"error": True, "message": e}, 500
    
    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()
        
        

        
# page = 0
# offsetPage = int(page)*12
# keywordQuery = "館"
# # LIMIT => limit the number of output and OFFSET => skip the number of ahead results.
# # queryKeyWord ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images FROM taipeiAttractions WHERE name LIKE %s ;"
# queryKeyWord ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images FROM taipeiAttractions WHERE name like %s LIMIT 13 OFFSET %s;"
# NewkeywordQuery = f'%{keywordQuery}%'
# total = (NewkeywordQuery, 0)
# try:
#     oneConnection = pickOneConnection()
#     cursor = oneConnection.cursor(buffered=True)
#     cursor.execute(queryKeyWord, total)
#     userNameQuery = cursor.fetchall()
#     for i in userNameQuery:
#         print(len(userNameQuery))
# except Error as e:
#     print({"error": True, "message": e}, 500)

# finally:
#     if oneConnection.in_transaction:
#         oneConnection.rollback()
#     oneConnection.close()


# queryKeyWordResult = queryAttractions(queryKeyWord, total)

# data = []  
# for i in queryKeyword(queryKeyWord, NewkeywordQuery)[0:12]:
#     print(i)
# for i in queryAttractions(queryKeyWord, (keywordQuery,offsetPage))[0:12]:
#     jsonToList = json.loads(i[9])
#     eachRow = {"id": i[0], 
#             "name": i[1], 
#             "category": i[2],
#             "description": i[3],
#             "address": i[4],
#             "transport": i[5],
#             "mrt": i[6],
#             "latitude": float(i[7]),
#             "longitude": float(i[8]),
#             "images": jsonToList}
#     data.append(json.dumps(eachRow, ensure_ascii=False))

#     print(type(json.dumps(eachRow, ensure_ascii=False)))
#     print()
# print(len(data))

# if len(queryAttractions(queryPage, offsetPage))<13:
#     print({"nextPage": None, "data": data[0:2]})
# else:
#     print({"nextPage": page+1, "data": data[0:2]})