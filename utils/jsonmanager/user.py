import os
import json
from main import get_json

def get_user_id_tg_id(filename,tg_id):
    data=get_json(filename)
    for i in data.keys():
        if data.get(i).get("tg_id") == tg_id:
            return i
    return None




# def get_user_phone(filename,phone):
#     data=get_json(filename)
#     for i in data.keys():
#         if data.get(i).get("phone") == phone:
#             return i
#     return None

# def edit_user(filename,phone,newdata):
#     id=get_user_phone(filename,phone)
#     data=get_json(filename)
#     data[id]=newdata
#     with open(filename,"w") as file:
#         json.dump(data,file,indent=2)
    
#     print("success")
    
