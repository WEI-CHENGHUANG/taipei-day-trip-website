# This article is really important cuz it diplays how the RESTful api interact with Flask_Blueprint.
# https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93#:~:text=Blueprint%3A%20It%20is%20used%20to,quickly%20and%20following%20best%20practices.

from databaseFunctions.database import queryOneCaluse, queryKeyword
from flask_restful import Resource
from flask  import *
import json

def queryPageResultFunction(queryPageResult):
    try :
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
        return data
    except:
        response = make_response(jsonify({"error": True, "message": "Internal Server Error, we are working on it, sorry"}),500)
        return response
        

def responseQueryResult(nextPage, data):
    response = jsonify({"nextPage": nextPage, "data": queryPageResultFunction(data)})
    return response



# 前端再拿fetch data時 url的page number 要+1 因為database的資料是nextPage
class attractions(Resource):
    def get(self):
        # This page is from the JS url query string or from a post sent url query, then the rest of code can use this to do the extended work.
        # indirect refterence: https://www.youtube.com/watch?v=yTbKm_6PsxY
        # Page
        page = request.args.get('page')
        # This If is to check the only keyword input situation
        if page is None:
            page = 0
        # This try is to avoid the user to provide a character as a page number.
        try:
            offsetPage = int(page)*12
        except:
            response = make_response(jsonify({"error": True, "message": "Wrong number input"}),500)

            return response
        # LIMIT means every query only returns 13 rows result and OFFSET means the system will skip how many rows first. 
        queryPage ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images FROM taipeiAttractions LIMIT 13 OFFSET %s;"
        queryPageResult = queryOneCaluse(queryPage, offsetPage)[0:12]
        # Keyword
        keywordQuery = request.args.get('keyword')
        queryKeyWord ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images FROM taipeiAttractions WHERE name like %s LIMIT 13 OFFSET %s;"
        NewkeywordQuery = f'%{keywordQuery}%'
        queryKeyWordResult = queryKeyword(queryKeyWord, (NewkeywordQuery, offsetPage))[0:12]
        try: 
            # Only Page
            # This IF is to detect how kind of input we get from user.
            if (page != None) and (keywordQuery == None):
                # This IF is to make sure that the query result is not empty.
                if queryPageResult:
                    # This IF is to check the result whether last page or not.
                    if len(queryOneCaluse(queryPage, offsetPage))<13:
                        return responseQueryResult(None, queryPageResult)
                    else:
                        return responseQueryResult(int(page)+1, queryPageResult)
                
                else:
                    response = make_response(jsonify({"error": True, "message": "Out of range"}),500)
        
                    return response
            # Page and Keyword
            elif (page != None) and (keywordQuery != None):
                if queryPageResult and queryKeyWordResult:
                    if len(queryKeyword(queryKeyWord, (NewkeywordQuery, offsetPage)))<13:
                        return responseQueryResult(None, queryKeyWordResult)
                    else:
                        return responseQueryResult(int(page)+1, queryKeyWordResult)
                    
                else:
                    response = make_response(jsonify({"error": True, "message": "Page or keyword may be wrong"}),200)
        
                    return response
        except:       
            response = make_response(jsonify({"error": True, "message": "Internal Server Error, we are working on it, sorry"}),500)

            return response
    
    
    
class attractionId(Resource):
    # Check Udemy class section 65
    def get(self, attractionId):
        
        queryId ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images FROM taipeiAttractions WHERE id=%s;" 
        queryIdResult = queryOneCaluse(queryId, attractionId)
        try:
            if queryIdResult:
                response = jsonify({"data": queryPageResultFunction(queryIdResult)[0]})
    
                return response
                
            else:
                response = make_response(jsonify({"error": True, "message": f"Sorry, could not find ID:{attractionId}"}),400)
    
                return response
        except:
            response = make_response(jsonify({"error": True, "message": "Internal Server Error, we are working on it, sorry"}),500)

            return response


