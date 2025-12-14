import os
import json
from main import get_json


def get_admin_id_tg_id(filename,tg_id):
    data=get_json(filename)
    for i in data.keys():
        if data.get(i).get("tg_id") == tg_id:
            return i
    return None
