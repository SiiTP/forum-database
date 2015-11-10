from app import app, cursor
from flask import request, jsonify
from functions import *
import json

@app.route("/db/api/user/create/", methods = ['POST'])
def createUser():
    try:

        email    = request.json["email"]
        print("email :" + email)
    except:
        print("exception on parsing json EMAIL")
        print("_____________________")
        print('\n''\n')
        return json.dumps({"code": 2, "response": error_messages[2]})

    try:
        name     = request.json["name"]
    except:
        name     = None
        print("NAME IS None")
        print("_____________________")
    try:
        username = request.json["username"]
    except:
        username = None
        print("USERNAME IS None")
        print("_____________________")
    try:
        about    = request.json["about"]
    except:
        about    = None
        print("ABOUT IS None")
        print("_____________________")

    if (not isString([name, email, username, about])):
        print("one or more params not string")
        return json.dumps({"code": 2, "response": error_messages[2]})

    sql = "SELECT idUser FROM User WHERE email = %s"
    cursor.execute(sql, email)
    if (cursor.fetchone() != None):
        print(email + " is not found in User")
        return json.dumps({"code": 5, "response": error_messages[5]})
    print("_____________________")
    print('\n''\n')
    isAnonymous = False
    if ("isAnonymous" in request.json):
        isAnonymous = request.json["isAnonymous"]

    sql = "INSERT INTO User(username, email, name, about, isAnonymous) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, [username, email, name, about, isAnonymous])

    sql = "SELECT MAX(idUser) FROM User"
    cursor.execute(sql)
    idU = cursor.fetchone()[0]

    data = {}
    data['about'] = about
    data['email'] = email
    data['id'] = idU
    data['isAnonymous'] = isAnonymous
    data['name'] = name
    data['username'] = username
    answer = {"code": 0, "response": data}
    response = json.dumps(answer)
    return response

@app.route("/db/api/user/details/", methods = ['GET'])
def userDetails():
    try:
        email = request.args.get("user")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})
    print(email)
    if (isString([email])):
        return json.dumps({"code": 2, "response": error_messages[2]})

    sql = "SELECT * FROM User WHERE email = %s"
    cursor.execute(sql, email)

    print("RESULT")
    q_result = cursor.fetchone()
    print(q_result)

    if (q_result != None):
        data = {}
        data['id'] = q_result[0]
        data['username'] = q_result[1]
        data['email'] = q_result[2]
        data['name'] = q_result[3]
        data['about'] = q_result[4]
        data['isAnonymous'] = q_result[5]
        response = json.dumps({ "code": 0, "response": data })
        return response
    else:
        return json.dumps({ "code": 1, "response": error_messages[1]})

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