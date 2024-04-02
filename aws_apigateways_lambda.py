import json 

def lambda_handler(event,handler):
    
    #Sample response
    response = {
        "statusCode":200,
        "header":{
            "Content-Type":"application/json"
        },
        "body":json.dumps({"message":"Hello World!"})
    } 
    return response