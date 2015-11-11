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

def getOptionalParameterOrDefault(json, param, default):
    try:
        data = json[param]
        print("option parameter " + str(param) + " : " + str(data))
    except:
        data = default
    return data