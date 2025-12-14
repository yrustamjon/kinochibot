def user_s(message):
    user = {
            "tg_id": message.from_user.id,
            "username": message.from_user.username or "",
            "first_name": message.from_user.first_name or "",
            "last_name": message.from_user.last_name or "",
            "phone_number":None,
            "lang": "Uzb",
            "is_premium": {
                "is_start": None,
                "is_end":None
            },
            "watch_count": 0
        }
    return user

movie = {
    "premium":False,
    "title": "",
    "name": "",
    "janr": "",
    "year": None,
    "lang": "",
    "country": "",
    "watch_count": 0,
    "act": [],
    "image": "",
    "trailer": "",
    "video": "",
    "arxive":False
}

ad = {
    "title": "",
    "dis": "",
    "image": "",
    "video": "",
    "url": "",
}

admin={
    "tg_id":None
}

sb_channels={
    "username":None,
    "name":None
} 