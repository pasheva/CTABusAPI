from flask import Blueprint, jsonify
import requests

main = Blueprint("main", __name__)

#Request Template http://ctabustracker.com/bustime/api/v2/[query component]?[key]=[value]&[key]=[value]
URL = "http://ctabustracker.com/bustime/api/v2/"
API_KEY="?key=RYBrriz5rJkSSqL7igvELwJsT"
QUERY_COMPONENTS = ["getdirections", "getstops", "getpredictions"]
FORMAT = "format=json"


#------------------------------------------------------------------------------------------------------

@main.route('/', methods=["GET"])
def home()->str:
    return "DemonHacks19"


@main.route('/<routeNumber>', methods=["GET"])
def getDirectionsByRouteNumber(routeNumber)->dict:
    """
    Getting the directions based on the unser's route number
    Param: Route Number
    Return: str
    """
    routeDirections = {}
    routeValue = routeNumber
    res = requests.get(URL+QUERY_COMPONENTS[0]+API_KEY+"&rt="+routeValue+"&"+FORMAT).json()
    # return routeDirections

    # {
    # "bustime-response": {
    #     "directions": [
    #     {
    #         "dir": "Northbound"
    #     },
    #     {
    #         "dir": "Southbound"
    #     }
    #     ]
    # }
    # }
    directionsList = res.get("bustime-response").get("directions")

    for i in range(len(directionsList)):
        routeDirections[str(i)+"_dir"] = directionsList[i].get("dir")

    return routeDirections


#Passing the 
@main.route("/<routeNumber>/<busDirection>", methods=["GET"])
def getBusStopID(routeNumber, busDirection)->dict:
    """
    Get stop id
    """
    busStopNameAndId = {}

    rtValue = routeNumber
    dirValue = busDirection

    # {
	# "bustime-response": {
	# 	"stops": [
	# 		{
	# 			"stpid": "12413",
	# 			"stpnm": "10602 S Vincennes",
	# 			"lat": 41.701258,
	# 			"lon": -87.658048000001
	# 		},
    # ...}

    res = requests.get(URL+QUERY_COMPONENTS[1]+API_KEY+"&rt="+rtValue+"&dir="+dirValue+"&"+FORMAT).json()

    directionsList = res.get("bustime-response").get("stops")

    for i in range(len(directionsList)):
        busStopNameAndId[directionsList[i].get("stpnm")] = directionsList[i].get("stpid")


    return busStopNameAndId