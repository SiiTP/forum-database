from app import app, cursor
from flask import request, jsonify
from functions import *
import json

@app.route("/db/api/user/create/", methods = ['POST'])
def createUser():
    print("\n================USER CREATION")
    try:
        email    = request.json["email"]
    except:
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
        print(email + " is already exists")
        return json.dumps({"code": 5, "response": error_messages[5]})

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
    print("================SUCCESSFUL USER CREATION\n")
    return response

@app.route("/db/api/user/details/", methods = ['GET'])
def userDetails():
    try:
        email = request.args.get("user")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})
    print(email)
    if (not isString([email])):
        return json.dumps({"code": 2, "response": error_messages[2]})

    answer = getUserInfoByEmail(email)
    if answer != None:
        return json.dumps({"code": 0, "response": answer})
    else:
        return json.dumps({"code": 1, "response": error_messages[1]})


@app.route("/db/api/user/follow/", methods = ['POST'])
def follow():
    print("\n================USER FOLLOW========================")
    try:
        follower = request.json["follower"]
        followee = request.json["followee"]
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})
    try:
        idFollower = getUserIdByEmail(follower)
        idFollowee = getUserIdByEmail(followee)
    except:
        return json.dumps({"code": 1, "response": error_messages[1]})

    print("follower : " + str(idFollower))
    print("followee : " + str(idFollowee))
    sql = "INSERT INTO Follower(idFollower, idFollowing) VALUES(%s, %s)"
    cursor.execute(sql, [idFollower, idFollowee])

    emailsFollowers = getFollowerEmails(idFollower)
    emailsFollowing = getFollowingEmails(idFollower)

    userInfo = getUserInfoByID(idFollower)
    userInfo["followers"] = emailsFollowers
    userInfo["following"] = emailsFollowing
    userInfo["subscriptions"] = []
    print("Response : ")
    print(userInfo)
    response = json.dumps({"code": 0, "response": userInfo})
    print("================USER FOLLOW SUCCESS================\n")
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

def getUserInfoByEmail(email):
    sql = "SELECT * FROM User WHERE email = %s"
    cursor.execute(sql, email)

    q_result = cursor.fetchone()

    if (q_result != None):
        data = {}
        data['id'] = q_result[0]
        data['username'] = q_result[1]
        data['email'] = q_result[2]
        data['name'] = q_result[3]
        data['about'] = q_result[4]
        data['isAnonymous'] = q_result[5]
        return data
    else:
        return None

def getUserIdByEmail(email):
    sql = "SELECT idUser FROM User WHERE email = %s"
    cursor.execute(sql, email)
    q_result = cursor.fetchone()[0]
    return q_result

def getUserInfoByID(id):
    sql = "SELECT * FROM User WHERE idUser = %s"
    cursor.execute(sql, id)

    q_result = cursor.fetchone()

    if (q_result != None):
        data = {}
        data['id'] = q_result[0]
        data['username'] = q_result[1]
        data['email'] = q_result[2]
        data['name'] = q_result[3]
        data['about'] = q_result[4]
        data['isAnonymous'] = q_result[5]
        return data
    else:
        return None

def getFollowerEmails(idUser):
    sql = "SELECT U.email FROM Follower F INNER JOIN User U ON F.idFollower = U.idUser WHERE F.idFollowing = %s"
    cursor.execute(sql, idUser)
    emails = getArrayFromDoubleDictionary(cursor.fetchall())
    print("EMAILS FOLLOWERS OF USER (" + str(idUser) + ") : " + str(emails))
    return emails

def getFollowingEmails(idUser):
    sql = "SELECT U.email FROM Follower F INNER JOIN User U ON F.idFollowing = U.idUser WHERE F.idFollower = %s"
    cursor.execute(sql, idUser)
    emails = getArrayFromDoubleDictionary(cursor.fetchall())
    print("EMAILS FOLLOFING OF USER (" + str(idUser) + ") : " + str(emails))
    return emails

def getArrayFromDoubleDictionary(dictionary):
    array = []
    for item in dictionary:
        array.append(item[0])
    return array