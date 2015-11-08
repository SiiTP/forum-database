# -*- coding: utf-8 -*-
from flask import request
import json

#сообщения к кодам ответов (код сообщения равен индексу в массиве)
error_messages = ["OK",
         u"Запрашиваемый объект не найден",
         u"невалидный запрос"]

def get_right_json():
    try:
        data = request.get_json()
        return data
    except:
        return {"code": 2, "response": error_messages[2]}