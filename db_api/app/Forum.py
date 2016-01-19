# -*- coding: utf-8 -*-
from app import app, cursor, conn
from functions import *
from flask import request
import json

@app.route("/db/api/forum/create/", methods = ['POST'])
def createForum():
    try:
        name       = request.json["name"].encode("UTF-8")
        short_name = request.json["short_name"]
        user       = request.json["user"]
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    cursor.execute("SELECT idUser FROM User WHERE User.email = %s", [user])
    id_User = cursor.fetchone()
    if (not id_User):
        return json.dumps({"code": 1, "response": error_messages[1]})
    id_User = id_User[0]

    sql = "SELECT * FROM Forum WHERE name = %s"
    cursor.execute(sql, [name])
    fetchone = cursor.fetchone()
    if (fetchone):
        print(fetchone)
        return json.dumps({"code": 0, "response": getForumDetailsById(fetchone[0])})

    sql = "SELECT * FROM Forum WHERE short_name = %s"
    cursor.execute(sql, [short_name])
    fetchone = cursor.fetchone()
    if (fetchone):
        print("n unique shName")
        print(fetchone)
        return json.dumps({"code": 0, "response": getForumDetailsById(fetchone[0])})


    sql = "INSERT INTO Forum (name, short_name, idFounder) VALUES (%s, %s, %s)"
    cursor.execute(sql, [name, short_name, id_User])
    conn.commit()

    sql = "SELECT max(idForum) FROM Forum"
    cursor.execute(sql)
    idF = cursor.fetchone()[0]

    answer = {"code": 0, "response": {"id": idF, "name": name, "short_name": short_name, "user": user}}
    response = json.dumps(answer)
    return response
    
@app.route("/db/api/forum/details/", methods = ['GET'])
def forumDetails():
    from User import getUserInfoByID

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
    
@app.route("/db/api/forum/listPosts/", methods = ['GET'])
def forumListPosts():
    logging.info("FORUM LIST POSTS===========================")
    from Post import getListPostsOfForum
    from Thread import getThreadDetailsByID
    from User import getUserEmailByID

    forum  = None
    try:
        forum = request.args.get("forum")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    limit   = getOptionalGetParameterOrDefault(request.args, "limit", None)
    order   = getOptionalGetParameterOrDefault(request.args, "order", "desc")
    since   = getOptionalGetParameterOrDefault(request.args, "since", None)

    try:
        related = request.args.getlist("related")
    except:
        logging.info("  related is empty")
        related = []

    logging.info("  forum   = " + str(forum))
    logging.info("  related = " + str(related))

    answer = []
    answer = getListPostsOfForum(forum, since, order, limit, related)

    # if not answer:
    #     print("empty 3")
    #     return json.dumps({"code": 1, "response": error_messages[2]})

    response = json.dumps({"code": 0, "response": answer})
    logging.info("  Response : ")
    logging.info(response)
    logging.info("FORUM LIST POSTS SUCCESSFUL================")
    return response
    
@app.route("/db/api/forum/listUsers/", methods = ['GET'])
def forumListUsers():
    from User import getListUsersOfForum

    logging.info("FORUM LIST USERS===========================")

    try:
        forum = request.args.get("forum")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    limit   = getOptionalGetParameterOrDefault(request.args, "limit", None)
    order   = getOptionalGetParameterOrDefault(request.args, "order", "desc")
    since   = getOptionalGetParameterOrDefault(request.args, "since", None)

    answer = getListUsersOfForum(forum, since, order, limit)

    # if not answer:
    #     print("empty 4")
    #     return json.dumps({"code": 1, "response": error_messages[2]})

    response = json.dumps({"code": 0, "response": answer})
    logging.info("  Response : ")
    logging.info(response)
    return response
    
@app.route("/db/api/forum/listThreads/", methods = ['GET'])
def forumListThreads():
    logging.info("FORUM LIST THREADS===========================")
    from Thread import getListThreadsOfForum

    forum  = None
    try:
        forum = request.args.get("forum")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    limit   = getOptionalGetParameterOrDefault(request.args, "limit", None)
    order   = getOptionalGetParameterOrDefault(request.args, "order", "desc")
    since   = getOptionalGetParameterOrDefault(request.args, "since", None)

    try:
        related = request.args.getlist("related")
    except:
        logging.info("  related is empty")
        related = []

    logging.info("  forum   = " + str(forum))
    logging.info("  related = " + str(related))

    answer = getListThreadsOfForum(forum, since, order, limit, related)

    # if not answer:
    #     print("empty 5")
    #     return json.dumps({"code": 1, "response": error_messages[2]})

    response = json.dumps({"code": 0, "response": answer})
    logging.info("  Response : ")
    logging.info(response)
    return response

def getForumDetailsByShortName(short_name):
    from User import getUserEmailByID
    sql = "SELECT * FROM Forum WHERE short_name = %s"
    cursor.execute(sql, [short_name])
    data = cursor.fetchone()
    if (not data):
        return None
    answer = {}
    answer["id"] = data[0]
    answer["name"] = data[1]
    answer["short_name"] = data[2]
    answer["idFounder"] = data[3]
    answer["user"] = getUserEmailByID(answer["idFounder"])
    return answer

def getForumIdByShortName(short_name):
    sql = "SELECT idForum FROM Forum WHERE short_name = %s"
    # print("SHORT_NAME : " + short_name)
    cursor.execute(sql, [short_name])
    data = cursor.fetchone()
    if (not data):
        return None
    answer = data[0]
    return answer

def getForumDetailsById(id):
    sql = "SELECT * FROM Forum WHERE idForum = %s"
    cursor.execute(sql, [id])
    data = cursor.fetchone()
    if (not data):
        return None
    answer = {}
    answer["id"] = data[0]
    answer["name"] = data[1]
    answer["short_name"] = data[2]
    answer["idFounder"] = data[3]
    return answer

def getForumShortNameById(id):
    sql = "SELECT short_name FROM Forum WHERE idForum = %s"
    cursor.execute(sql, [id])
    data = cursor.fetchone()
    if (not data):
        return None
    answer = data[0]
    return answer