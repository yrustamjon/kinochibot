import os
import json

def get_json(filename):
    try:
        data={}
        if os.path.exists(filename):
            with open(filename,"r") as file:
                data=json.load(file)
                if data is None:
                    return {"error":"data is not"}
        return data
                
    except Exception as e:
        print(e)

def add_json(filename,newdata):
    try:
        data=get_json(filename)   
        if newdata["tg_id"] in [i['tg_id'] for i in data.values()]:
            return {"error":"this user is alrdy added"}
        
        id_next=1
        if data:
            id_list=[int(i) for i in data.keys() ]
            id_next+=max(id_list)
        data[str(id_next)]=newdata
            
        
        with open(filename,'w') as file:
            json.dump(data,file,indent=2)
        return {"success": True, "id": id_next}
    except Exception as e:
        print(e)

def get_id_json(filename,id):
    try:
        data=get_json(filename)      
        if not str(id) in data.keys():
            return {"error":"data is not"}
        return data[str(id)]
                
    except Exception as e:
        print(e)
    
    
def edit_json(filename,id,newdata):
    try:
        data=get_json(filename)        
        if not str(id) in data.keys():
            return {"error":"data is not"}
        
        data[str(id)]=newdata
        with open(filename,"w") as file:
            json.dump(data,file,indent=2)
        return {"success": True, "id": id} 
    except Exception as e:
        print(e)


