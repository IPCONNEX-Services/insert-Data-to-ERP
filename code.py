import requests
# TODO : insert personal data here
URL_API=""  # api url
URL_LOGIN=URL_API+"/method/login"
username="" #email
password="" #password
doctype_name="" #doctype
URL=URL_API+"/resource/"+doctype_name

response = requests.post(URL_LOGIN, data={'usr': username, 'pwd': password})
############################### LOGIN ###############################
if response.status_code==200:
    cookies = "sid="+ response.cookies.get("sid")
    print(cookies)

else:
    print('Login failed.')
    quit()
############################### INSERT data ###############################
header={
    "Authorization":"Bearer "+cookies,
    "Cookie":"full_name=API;"+cookies+"; system_user=yes; user_id="+username+"; user_image="
    }

dataset=[] # TODO : put all data here 
success_count=0

for instance in dataset:
    # TODO : edit the data dictionnary ([key]=value) bellow depending on the doctype 
    data= {
        "key":instance["key"],
    }
    response = requests.post(URL,data=data,headers=header)
    if response.status_code!= 200:
        print("error:",instance)
    else: 
        success_count+=1

print("Success: "+str(success_count)+"/"+str(len(dataset)))
    

