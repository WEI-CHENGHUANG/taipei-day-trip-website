# This article is really important cuz it diplays how the RESTful api interact with Flask_Blueprint.
# https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93#:~:text=Blueprint%3A%20It%20is%20used%20to,quickly%20and%20following%20best%20practices.
from urllib import response

from databaseFunctions.database import selectData
from flask_restful import Resource
from flask  import *
import json

# 前端再拿fetch data時 url的page number 要+1 因為database的資料是nextPage
class attractions(Resource):
    def get(self):
        # This page is from the JS url query string or from a post sent url query, then the rest of code can use this to do the extended work.
        # indirect refterence: https://www.youtube.com/watch?v=yTbKm_6PsxY
        page = request.args.get('page')
        keywordQuery = request.args.get('keyword', None)
        
        # Check the database.py file under week7assignment folder.
        queryPage ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE page=%s;"  
        queryPageResult = selectData(queryPage, page)
        queryKeyWord ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE name like %s;"  
        
        # Reference: https://www.w3schools.com/mysql/mysql_like.asp
        NewkeywordQuery = f'%{keywordQuery}%'
        queryKeyWordResult = selectData(queryKeyWord, NewkeywordQuery)
        
        # This is a error detecting function.
        if (page != None) and (keywordQuery == None):
            if queryPageResult:
                data = []
                for i in queryPageResult:
                    jsonToList = json.loads(i[9])
                    eachRow = {"id": i[0], 
                            "name": i[1], 
                            "category": i[2],
                            "description": i[3],
                            "address": i[4],
                            "transport": i[5],
                            "mrt": i[6],
                            "latitude": float(i[7]),
                            "longitude": float(i[8]),
                            "images": jsonToList}
                    data.append(eachRow)
                return {"nextPage": queryPageResult[-1][-1], "data": data}
            return {"error": True, "message": "something went wrong"}, 500
        elif (page != None) and (keywordQuery != None):
            if queryPageResult and queryKeyWordResult:
                data = []
                for i in queryKeyWordResult:
                    jsonToList = json.loads(i[9])
                    eachRow = {"id": i[0], 
                            "name": i[1], 
                            "category": i[2],
                            "description": i[3],
                            "address": i[4],
                            "transport": i[5],
                            "mrt": i[6],
                            "latitude": float(i[7]),
                            "longitude": float(i[8]),
                            "images": jsonToList}
                    data.append(eachRow)
                    
                lengthOfData = (abs(len(data)-1))//12
                startPoint = int(page)*12 
                endPoint = startPoint + 12
                # 這個if statement 是可以知道是不是最後一頁，所以我就不用擔心最後一頁的邏輯問題
                # 再來是elif 是處理總頁數大於 所要頁數問題，意思是代表我們還有頁數可以抓取，但是當總長度沒有大於輸入的頁數時就會出現錯誤
                # 因為超出範圍 所以就會跳出最後一個elif錯誤訊息
                if int(page) == int(lengthOfData):
                    return {"nextPage": None , "data": data[startPoint:endPoint]}
                elif int(lengthOfData) > int(page) :
                    return {"nextPage": int(page)+1, "data": data[startPoint:endPoint]}
                elif int(lengthOfData) < int(page) :
                    return {"error": True, "message": f'The last page is {lengthOfData}'}, 500
            return {"error": True, "message": 'something went wrong'},
        elif (page == None) and (keywordQuery != None):
            page = 0
            if queryKeyWordResult:
                data = []
                for i in queryKeyWordResult:
                    jsonToList = json.loads(i[9])
                    eachRow = {"id": i[0], 
                            "name": i[1], 
                            "category": i[2],
                            "description": i[3],
                            "address": i[4],
                            "transport": i[5],
                            "mrt": i[6],
                            "latitude": float(i[7]),
                            "longitude": float(i[8]),
                            "images": jsonToList}
                    data.append(eachRow)
                lengthOfData = (abs(len(data)-1))//12
                startPoint = int(page)*12
                endPoint = startPoint + 12
                if int(page) == int(lengthOfData):
                    return {"nextPage": None , "data": data[startPoint:endPoint]}
                elif int(lengthOfData) > int(page) :
                    return {"nextPage": int(page)+1, "data": data[startPoint:endPoint]}
                elif int(lengthOfData) < int(page) :
                    return {"error": True, "message": f'The last page is {lengthOfData}'}, 500
            return {"error": True, "message": "something went wrong"}, 500
                
        else:    
            return {"error": True, "message": "No Result"}, 500
    
    
    
class attractionId(Resource):
    # Check Udemy class section 65
    def get(self, attractionId):
        
        queryId ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE id=%s;" 
        queryIdResult = selectData(queryId, attractionId)
        try:
            if queryIdResult:
                data = []
                for i in queryIdResult:
                    jsonToList = json.loads(i[9])
                    eachRow = {"id": i[0], 
                            "name": i[1], 
                            "category": i[2],
                            "description": i[3],
                            "address": i[4],
                            "transport": i[5],
                            "mrt": i[6],
                            "latitude": float(i[7]),
                            "longitude": float(i[8]),
                            "images": jsonToList}
                    data.append(eachRow)
                return {"data": data}
            
            return {"error": True, "message": f"Sorry, could not find ID:{attractionId}"}, 400
        except:
            if queryIdResult["error"]== True:
                return { "error": True, "message": "Internal error"},500


