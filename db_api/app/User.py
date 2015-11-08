from app import app, cursor, functions
from flask import request
import json

@app.route("/db/api/user/create", methods = ['POST'])
def createUser():
    data = functions.get_right_json()
    if data.has_key("code"):
        response = json.dumps(data)
        return response

    if (data.has_key("isAnonymous")):
        sql = "INSERT INTO User(username, email, name, about, isAnonymous) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (data["username"], data["email"], data["name"], data["about"], data["isAnonymous"]))
    else:
        sql = "INSERT INTO User(username, email, name, about) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (data["username"], data["email"], data["name"], data["about"]))
    sql = "SELECT MAX(idUser) FROM User"
    cursor.execute(sql)
    idU = cursor.fetchone()[0]
    data["id"] = idU
    answer = {"code": 0, "response": data}
    response = json.dumps(answer)
    return response

@app.route("/db/api/user/details", methods = ['GET'])
def userDetails():
    response = json.dumps({ "code": 0 })
    return response

@app.route("/db/api/user/follow", methods = ['POST'])
def follow():
    response = json.dumps({ "code": 0 })
    return response

@app.route("/db/api/user/listFollowers", methods = ['GET'])
def listFollowers():
    response = json.dumps({ "code": 0 })
    return response

@app.route("/db/api/user/listFollowing", methods = ['GET'])
def listFollowing():
    response = json.dumps({ "code": 0 })
    return response

@app.route("/db/api/user/listPosts", methods = ['GET'])
def userListPosts():
    response = json.dumps({ "code": 0 })
    return response

@app.route("/db/api/user/unfollow", methods = ['POST'])
def unfollow():
    response = json.dumps({ "code": 0 })
    return response

@app.route("/db/api/user/updateProfile", methods = ['POST'])
def updateProfile():
    response = json.dumps({ "code": 0 })
    return response