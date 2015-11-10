# -*- coding: utf-8 -*-
from app import app, cursor, functions
import json

@app.route("/db/api/forum/create/", methods = ['POST'])
def createForum():
    data = functions.get_right_json()
    if data.has_key("code"):
        response = json.dumps(data)
        return response
    answer = {}
    cursor.execute("SELECT idUser FROM User WHERE User.email = %s", (data["user"]))
    id_User = cursor.fetchone()
    print("user_id : ", id_User)
    print(id_User)
    if (id_User != None):
        id_User = id_User[0]
        sql = "INSERT INTO Forum (name, short_name, idFounder) VALUES (%s, %s, %s)"
        cursor.execute(sql, (data["name"], data["short_name"], id_User))
        sql = "SELECT max(idForum) FROM Forum"
        cursor.execute(sql)
        idF = cursor.fetchone()[0]
        data["id"]         = idF
        answer["code"]     = 0
        answer["response"] = data
    else:
        answer["code"] = 1
        answer["response"] = functions.error_messages[1]
    response = json.dumps(answer)
    return response
    
@app.route("/db/api/forum/details", methods = ['GET'])
def forumDetails():
    response = json.dumps({ "code": 0, "response": "details" })
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
