# -*- coding: utf-8 -*-
from flask import request

#сообщения к кодам ответов (код сообщения равен индексу в массиве)
error_messages = ["OK",
         "object not found",
         "incorrect query",
         "uncorrect semantic query",
         "undefined error",
         "already exists"]

def isString(args):
    for arg in args:
        if (not isinstance(arg, basestring)):
            if arg:
                return False
    return True

#THREAD
def getStringExecuteFromAmountParams(n):
    if n <= 0:
        return ""
    str = "%s"
    for i in range(0, n-2, 1):
        str += str + ", %s"
    return str

def parseItemFromDictionary(item):
    return ge
    # answer = {}
    # answer["id"] = item[0]
    # answer["title"] = item[1]
    # answer["message"] = item[2]
    # answer["slug"] = item[3]
    # answer["date"] = item[4]
    # answer["isClosed"]  = item[5]
    # answer["isDeleted"] = item[6]

#POST
def getOptionalParameterOrDefault(json, param, default):
    try:
        data = json[param]
        print("option parameter " + str(param) + " : " + str(data))
    except:
        data = default
    return data