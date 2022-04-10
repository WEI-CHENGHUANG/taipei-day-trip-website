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

def queryOneClause(query, condition):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, (condition,))
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return {"error": True, "message": e}, 500

    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()
# 因為發現舊的query在錯誤回覆時 在API檔案中的if statement有問題，不管是否有結果或是回覆錯誤到API file 都是True 所以那邊都是沒有公用的
# 但是因為前面已經有再多地方使用舊有的功能  所以在這邊先做一個斷點，在這後續都用新的
def queryOneClauseNew(query, condition):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, (condition,))
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return "Wrong"

    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()


def queryMultileClauses(query, *args):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, *args)
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return {"error": True, "message": e}, 500

    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()
def queryMultileClausesNew(query, *args):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, *args)
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return "Wrong"

    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()



def queryKeyword(query, *args):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(query, *args)
        userNameQuery = cursor.fetchall()
        return userNameQuery
    
    except Error as e:
        return {"error": True, "message": e}, 500
    
    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()
        
        
def insertNewMembers(insert, *args):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(insert, *args)
        oneConnection.commit()
        
    except Error as e:
        return "Wrong"
    
    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()
        
        
def deleteOldrecord(deleterecord, *args):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(deleterecord, *args)
        oneConnection.commit()
        
    except Error as e:
        return "Wrong"
    
    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()

def updateRecored(insert, *args):
    try:
        oneConnection = pickOneConnection()
        cursor = oneConnection.cursor(buffered=True)
        cursor.execute(insert, *args)
        oneConnection.commit()
        
    except Error as e:
        return "Wrong"
    
    finally:
        if oneConnection.in_transaction:
            oneConnection.rollback()
        oneConnection.close()