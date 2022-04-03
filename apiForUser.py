from databaseFunctions.database import queryOneClause,insertNewMembers, queryMultileClauses
from flask_restful import Resource
from flask import *
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
import datetime
import jwt




class userIdentification(Resource):

    def get(self):
        cookies = request.cookies
        if cookies: 
            decoded = jwt.decode(request.cookies['access_token_cookie'],'taiwan', algorithms=['HS256'])
            return make_response(decoded["sub"],200)
        else:
            return "null"
        # =====================================
        # # This is for session method, write it in the notion.
        # if ("email" and "password") in session:
        #     print(session["email"], session["password"])
        #     return "ok"
        # # print(session["email"], session["password"])
        # return "null"
       

    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.get_json()
            name = json["name"]
            email = json["email"]
            password = json["password"]
            query ="SELECT name FROM member WHERE email=%s;"
            queryResult = queryOneClause(query, email)
            # This is to check if the name exists or not.
            if queryResult:
                response = make_response(jsonify({"error": True, "message": f'{email} 已是註冊帳戶.'}), 400)
                return response
            else:
                insert ="INSERT INTO member (name, email, password) VALUES(%s, %s, %s)"
                try:
                    insertNewMembers(insert, (name, email, password))
                    response = make_response(jsonify({"ok": True}),200)
                    
                    return response 
                except:
                    response = make_response(jsonify({"error": True, "message": "Internal Server Error, we are working on it, sorry"}),500)
                    return response         
        else:
            return 'Content-Type not supported!(This info is for engineer)'
       
    def patch(self):

        content_type = request.headers.get("Content-Type")
        if (content_type == 'application/json'):
            json = request.get_json()
            email = json["email"]
            password = json["password"]
            queryEmail ="SELECT email FROM member WHERE email=%s;"
            try:
                queryEmailResult = queryMultileClauses(queryEmail, (email, ))
                if queryEmailResult:
                    try:
                        finalQuery ="SELECT id, name, email FROM member WHERE email=%s and password=%s;"
                        finalQueryResult = queryMultileClauses(finalQuery, (email, password))
                        if finalQueryResult:
                            expires = datetime.timedelta(days=7)
                            accessToken = create_access_token(identity={"data":{"id":finalQueryResult[0][0],"name":finalQueryResult[0][1],"email":finalQueryResult[0][2]}}, expires_delta=expires)
                            # # This is for session method, write it in the notion.
                            # session["email"] = queryResult[0][0]
                            # session["password"] = queryResult[0][1]

                            response = make_response(jsonify({"ok": True}), 200)
                            set_access_cookies(response, accessToken)

                            return response
                        else:
                            response = make_response(jsonify({"error": True, "message": "密碼錯誤"}), 400)
                            return response
                    except:
                        response = make_response(jsonify({"error": True, "message": "Internal Server Error, we are working on it, sorry"}),500)
                        return response
                else:
                    response = make_response(jsonify({"error": True, "message": "此電子郵件尚未註冊"}), 400)
                    return response
                    
            except:
                response = make_response(jsonify({"error": True, "message": "Internal Server Error, we are working on it, sorry"}),500)
                return response
                 
    def delete(self):
        # Delete JWT token
        try:
            # del session["email"]
            # del session["password"]
            response = make_response(jsonify({"ok": True}),200)
            unset_jwt_cookies(response)
            return response
        except:
            return "wrong"
                

        
