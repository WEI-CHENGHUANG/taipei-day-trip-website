# This article is really important cuz it diplays how the RESTful api interact with Flask_Blueprint.
# https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93#:~:text=Blueprint%3A%20It%20is%20used%20to,quickly%20and%20following%20best%20practices.
from email.policy import HTTP
from http.client import HTTPException
from flask import *
from flask_restful import Api
from routes import initialize_routes
# from flask_cors import CORS

app=Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

# This is for RESTful api to use.
api = Api(app)
initialize_routes(api)

# Pages
@app.route("/")
def index():
    # abort(400)
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

from werkzeug.exceptions import HTTPException


  

if __name__ == "__main__":
    app.run(port=3000,debug=True)