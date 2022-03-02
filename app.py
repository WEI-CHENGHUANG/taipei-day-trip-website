from flask import *
from databaseFunctions.database import selectData
from flask_restful import Resource, Api



app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")

# 前端再拿fetch data時 url的page number 要+1 因為database的資料是nextPage
class attractions(Resource):
    def get(self):
        # This page is from the JS url query string or from a post sent url query, then the rest of code can use this to do the extended work.
        # indirect refterence: https://www.youtube.com/watch?v=yTbKm_6PsxY
        page = request.args.get('page')
        keywordQuery = request.args.get('keyword', None)
        
        # Check the database.py file under week7assignment folder.
        # query_1 ="SELECT id, name, username FROM member WHERE username=%s;"
        queryPage ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE page=%s;"  
        queryPageResult = selectData(queryPage, page)
        queryKeyWord ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE name like %s;"  
        # Reference: https://www.w3schools.com/mysql/mysql_like.asp
        NewkeywordQuery = f'%{keywordQuery}%'
        queryKeyWordResult = selectData(queryKeyWord, NewkeywordQuery)
        if (page != None) and (keywordQuery == None):
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
            return {"nextPage": queryPageResult[-1][-1], "data": data}, 500
        elif (page != None) and (keywordQuery != None):
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
                    
        return {"error": True, "message": "No Result"}, 500

class attractionId(Resource):
    # Check Udemy class section 65
    def get(self, attractionId):
        queryId ="SELECT id, name, category, description, address, transport, mrt, latitude, longitude, images, nextPage FROM taipeiAttractions WHERE id=%s;" 
        queryIdResult = selectData(queryId, attractionId)
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
    
    
api = Api(app)
api.add_resource(attractions, '/api/attractions')
api.add_resource(attractionId, '/api/attraction/<attractionId>')
    

if __name__ == "__main__":
    app.run(port=3000,debug=True)