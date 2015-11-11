# -*- coding: utf-8 -*-
from app import app, cursor
from functions import *
from User import *
from flask import request
import json

@app.route("/db/api/forum/create/", methods = ['POST'])
def createForum():
    print("\n================FORUM CREATION\n")
    # print("REQUEST :")
    # print(request.json)
    # print("SH_NAME : " + request.json["short_name"])
    # print("USER : " + request.json["user"])
    # print("NAME : " + request.json["name"].encode("UTF-8"))
    try:
        name       = request.json["name"].encode("UTF-8")
        print("NAME : " + name)
        short_name = request.json["short_name"]
        print("SHORT_NAME : " + short_name)
        user       = request.json["user"]
        print("USER : " + user)
    except:
        print("error in parsing params")
        return json.dumps({"code": 2, "response": error_messages[2]})

    cursor.execute("SELECT idUser FROM User WHERE User.email = %s", user)
    id_User = cursor.fetchone()
    if (not id_User):
        return json.dumps({"code": 1, "response": error_messages[1]})
    id_User = id_User[0]

    sql = "SELECT * FROM Forum WHERE name = %s"
    cursor.execute(sql, name)
    if (cursor.fetchone()):
        return json.dumps({"code": 5, "response": error_messages[5]})

    sql = "INSERT INTO Forum (name, short_name, idFounder) VALUES (%s, %s, %s)"
    cursor.execute(sql, [name, short_name, id_User])

    sql = "SELECT max(idForum) FROM Forum"
    cursor.execute(sql)
    idF = cursor.fetchone()[0]
    answer = {"code": 0, "response": {"id": idF, "name": name, "short_name":short_name, "user": user}}

    response = json.dumps(answer)
    print("\n================SUCCESSFUL FORUM CREATION\n")
    return response
    
@app.route("/db/api/forum/details/", methods = ['GET'])
def forumDetails():
    try:
        forum = request.args.get("forum")
        related = request.args.getlist("related")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})


    answer = getForumDetailsByShortName(forum)
    if not answer:
        return json.dumps({"code": 1, "response": error_messages[1]})

    if related:
        user = getUserInfoByID(answer["idFounder"])
        answer["user"] = user
    response = json.dumps({ "code": 0, "response": answer})
    return response
    
@app.route("/db/api/forum/listPosts", methods = ['GET'])
def forumListPosts():
    response = json.dumps({"code": 0, "response": "listPosts"})
    return response
    
@app.route("/db/api/forum/listUsers", methods = ['GET'])
def forumListUsers():
    response = json.dumps({"code": 0, "response": "listUsers"})
    return response
    
@app.route("/db/api/forum/listThreads", methods = ['GET'])
def forumListThreads():
    response = json.dumps({"code": 0, "response": "listThreads"})
    return response

def getForumDetailsByShortName(short_name):
    sql = "SELECT * FROM Forum WHERE short_name = %s"
    cursor.execute(sql, short_name)
    data = cursor.fetchone()
    if (not data):
        return None
    answer = {}
    answer["id"] = data[0]
    answer["name"] = data[1]
    answer["short_name"] = data[2]
    answer["idFounder"] = data[3]
    return answer

def getForumDetailsById(id):
    sql = "SELECT * FROM Forum WHERE idForum = %s"
    cursor.execute(sql, id)
    data = cursor.fetchone()
    if (not data):
        return None
    answer = {}
    answer["id"] = data[0]
    answer["name"] = data[1]
    answer["short_name"] = data[2]
    answer["idFounder"] = data[3]
    return answer