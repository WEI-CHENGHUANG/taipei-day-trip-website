# This article is really important cuz it diplays how the RESTful api interact with Flask_Blueprint.
# https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93#:~:text=Blueprint%3A%20It%20is%20used%20to,quickly%20and%20following%20best%20practices.
from apiForAttractions import attractions, attractionId

def initialize_routes(api):
    api.add_resource(attractions, '/api/attractions')
    api.add_resource(attractionId, '/api/attraction/<attractionId>')
    


