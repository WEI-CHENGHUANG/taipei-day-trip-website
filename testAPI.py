# import urllib.request as request
# import json
# import threading



# class sendToTapPay(threading.Thread):
  
#   def run(self):
#     url = 'https://sandbox.tappaysdk.com/tpc/payment/pay-by-prime'
#     headers = {'Content-Type': 'application/json', 'x-api-key': 'partner_nCmeig3rxFHOpsSTqDoRcYApSXdAXOXRkxGB7E4oT3IMTSCk7sSj8bit'}

#     values = {
#       "prime": 'd5f0a1cb8c5aa9ef0919e869db02cbe19ba6673a84ff046f18946b192b111485',
#       "partner_key":'partner_nCmeig3rxFHOpsSTqDoRcYApSXdAXOXRkxGB7E4oT3IMTSCk7sSj8bit',
#       "merchant_id": "WilsonHuang_ESUN",
#       "details":"TapPay Test",
#       "amount": 100,
#       "cardholder": {
#           "phone_number": "+886923456789",
#           "name": "王小明",
#           "email": "LittleMing@Wang.com"
#       },
#       "remember": False
#     }

#     req = request.Request(url)
#     req.add_header('Content-Type', 'application/json')
#     req.add_header('x-api-key', 'partner_nCmeig3rxFHOpsSTqDoRcYApSXdAXOXRkxGB7E4oT3IMTSCk7sSj8bit')
#     data = json.dumps(values)
#     jsondataasbytes = data.encode('utf-8')
#     with request.urlopen(req, jsondataasbytes) as response:
#         result = response.read().decode('utf-8')
    
#     # print("result")
#     return "123"

# send = sendToTapPay()
# send.start()
# # print(send.run())
# print("test")

# import uuid

# test = uuid.uuid4()
# test = str(test)[:8]
# # test = str(test)+"0921"
# print(test)

# import re
# test = "0442345678"

# checkNumber = re.match("(^[0][9]\d{8})$", test)
# if z:
#   print("YES")
# else:
#   print("NO")




# from databaseFunctions.database import insertNewMembers,updateRecored
# import uuid

# amount = 2000
# attractionId = 1
# attractionName = "新北投溫泉區"
# attractionAddress = "臺北市  北投區中山路、光明路沿線"
# travelDate = "05 Apr 2022"
# travelTime = "morning"
# contactName =  "Wilson Huang"
# contactEmail = "test@gmail.com"
# contactPhone =  "0921635411"
# # ==============================================================================
# randomNumber = uuid.uuid4()
# orderNumber = str(randomNumber)[:8]+ contactPhone
# insert ="INSERT INTO ordersInfo (attractionId, price, attractionName, attractionAddress, \
#         travelDate, travelTime, contactName, contactemail, contactPhone, orderNumber) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# insertResult = insertNewMembers(insert, (attractionId, amount, attractionName, attractionAddress, \
#                                         travelDate, travelTime, contactName, contactEmail, contactPhone, orderNumber))
# if insertResult == "Wrong":
#    print("wrong")
# else:
#   print("pass")













        # =================testing purpose============================
        # abc = {
        # "prime": "4a994d1a770aadbaa14151d9fc6ec69cd26d783902cdf50f615843bdfb0f5918",
        # "order": {
        #     "price": 2000,
        #     "trip": {
        #     "attraction": {
        #         "id": 10,
        #         "name": "平安鐘",
        #         "address": "臺北市大安區忠孝東路 4 段",
        #         "image": "https://yourdomain.com/images/attraction/10.jpg"
        #     },
        #     "date": "2022-01-31",
        #     "time": "afternoon"
        #     },
        #     "contact": {
        #     "name": "彭彭彭",
        #     "email": "ply@ply.com",
        #     "phone": "0912345678"
        #     }
        # }
        # }
        # prime = abc["prime"]
        # amount = abc["order"]["price"]
        # attractionId = abc["order"]["trip"]["attraction"]["id"]
        # attractionName = abc["order"]["trip"]["attraction"]["name"]
        # attractionAddress = abc["order"]["trip"]["attraction"]["address"]
        # travelDate = abc["order"]["trip"]["date"]
        # travelTime = abc["order"]["trip"]["time"]
        # contactName =  abc["order"]["contact"]["name"]
        # contactEmail =  abc["order"]["contact"]["email"]
        # contactPhone =  abc["order"]["contact"]["phone"]
        # ==============================================================================