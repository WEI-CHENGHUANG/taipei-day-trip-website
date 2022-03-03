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
        
        

    


