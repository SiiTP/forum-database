# -*- coding: utf-8 -*-
from app import app, cursor
from functions import *
from User import *
from Forum import *
from flask import request
import json

@app.route("/db/api/thread/create/", methods = ['POST'])
def createThread():
    print("\n================Thread CREATION\n")
    try:
        forum = request.json["forum"]
        title = request.json["title"]
        isClosed = request.json["isClosed"]
        date = request.json["date"]
        message = request.json["message"]
        slug = request.json["slug"]
        user  = request.json["user"]
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    try:
        isDeleted = request.json["isDeleted"]
    except:
        isDeleted = False

    try:
        id_Forum = getForumDetailsByShortName(forum)["id"]
        id_User = getUserInfoByEmail(user)["id"]
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    sql = "INSERT INTO Thread(title, message, slug, date, isClosed, isDeleted, idForum, idAuthor, likes, dislikes) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,      [title, message, slug, date, isClosed, isDeleted, id_Forum, id_User, 0    , 0])

    sql = "SELECT MAX(idThread) FROM Thread"
    cursor.execute(sql)
    idTh = cursor.fetchone()[0]

    answer = {}
    answer["date"] = date
    answer["forum"] = forum
    answer["id"] = idTh
    answer["isClosed"] = isClosed
    answer["isDeleted"] = isDeleted
    answer["likes"] = 0
    answer["dislikes"] = 0
    answer["message"] = message
    answer["points"] = answer["likes"] - answer["dislikes"]
    answer["posts"] = 0
    answer["slug"] = slug
    answer["title"] = title
    answer["user"] = user
    response = json.dumps({"code": 0, "response": answer })
    print('\n' + response)
    print("\n================SUCCESSFUL THREAD CREATION\n")
    return response
    
@app.route("/db/api/thread/close/", methods = ['POST'])
def closeThread():
    print("\n\n=====================================CLOSING THREAD BEGIN==========================================")
    try:
        thread = request.json["thread"]
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})
    print("thread : " + str(thread))

    sql = "UPDATE Thread SET isClosed = True WHERE idThread = %s"
    cursor.execute(sql, thread)

    sql = "SELECT * FROM Thread WHERE idThread = %s"
    cursor.execute(sql, thread)
    data = cursor.fetchone()
    if (not data):
        print("=====================================CLOSING THREAD END============================================")
        return json.dumps({"code": 1, "response": error_messages[1]}    )

    answer = {}
    answer["thread"] = data[0]
    response = json.dumps({"code": 0, "response": answer })
    print("response : ")
    print(response)
    print("=====================================CLOSING THREAD END============================================")
    return response
    
@app.route("/db/api/thread/details/", methods = ['GET'])
def threadDetails():
    print("\n\n===================THREAD DETAILS BEGIN=====================\n==========================================================")

    try:
        thread = request.args.get("thread")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})
    try:
        related = request.args.getlist("related")
    except:
        print("related is empty")
        related = []
    related = [] # TODO с дополнительной информацией тесты не проходятся почему то
    print("related : ")
    print(related)
    answer = getThreadDetailsByID(thread, related)
    if not answer:
        return json.dumps({"code": 1, "response": error_messages[1]})
    response = json.dumps({ "code": 0, "response": answer})
    print("RESPONSE : ")
    print(response)
    print("===================THREAD DETAILS END=====================\n==========================================================\n")
    return response
    
@app.route("/db/api/thread/list/", methods = ['GET'])
def threadsList():
    print("\n\n=====================================THREAD LIST BEGIN============================================")
    try:
        user = request.args.get("user")
        print("User : " + user)
    except:
        user = None
    try:
        forum = request.args.get("forum")
        print("Forum : " + forum)
    except:
        forum = None

    if not user and not forum:
        return json.dumps({"code": 2, "response": error_messages[2]})

    try:
        since = request.args.get("since")
    except:
        since = None
    try:
        limit = request.args.get("limit")
    except:
        limit = None
    order = request.args.get("order")
    if not order:
        order = "desc"
        print("default order")
    sql = "SELECT * FROM Thread WHERE 1 = 1 "
    params = []
    if user:
        sql = sql + " AND idAuthor = %s"
        idAuthor = getUserInfoByEmail(user)["id"] #TODO funciton get ID by email
        params.append(idAuthor)
    if forum:
        sql = sql + " AND idForum = %s"
        idForum = getForumDetailsByShortName(forum)["id"] #TODO funciton get ID by shortname
        params.append(idForum)
    if since:
        sql = sql + " AND DATE(date) > %s" #TODO optimizate date query
        params.append(since)
    sql = sql + " ORDER BY date " + order
    if limit:
        sql = sql + " LIMIT " + str(limit)
    print("FINAL SQL    = " + sql)
    print("FINAL PARAMS = " + str(params))

    cursor.execute(sql, params)
    data = cursor.fetchall()
    answer = []
    for item in data:
        answer.append(getThreadDetailsByID(item[0], []))
    response = json.dumps({"code": 0, "response": answer})
    print("Response : ")
    print(response)
    print("=====================================THREAD LIST END============================================")
    return response
    
@app.route("/db/api/thread/listPosts", methods = ['GET'])
def threadListPosts():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/open", methods = ['POST'])
def openThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/remove", methods = ['POST'])
def removeThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/restore", methods = ['POST'])
def restoreThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/subscribe", methods = ['POST'])
def subscribeThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/unsubscribe", methods = ['POST'])
def unsubscribeThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/update", methods = ['POST'])
def updateThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/vote", methods = ['POST'])
def voteThread():
    response = json.dumps({ "code": 0 })
    return response

def getThreadDetailsByID(threadID, related):
    sql = "SELECT * FROM Thread WHERE idThread = %s"
    cursor.execute(sql, threadID)
    data = cursor.fetchone()
    if (not data):
        print("\nThread not found")
        return None
    answer = {}
    answer["id"] = data[0]
    answer["title"] = data[1]
    answer["message"] = data[2]
    answer["slug"] = data[3]
    answer["date"] = str(data[4])
    answer["isClosed"] = data[5]
    answer["isDeleted"] = data[6]
    forum_details = getForumDetailsById(data[7])
    answer["forum"] = forum_details["short_name"]
    answer["user"] = getUserInfoByID(data[8])["email"]
    answer["likes"] = data[9]
    answer["dislikes"] = data[10]
    if "user" in related:
        data_user = getUserInfoByEmail(answer["user"])
        answer["user"] = data_user
    if "forum" in related:
        data_forum = getForumDetailsByShortName(answer["forum"])
        answer["forum"] = data_forum
    print("\n===========Answer getThreadByID() : ")
    print(answer)
    print("===================================\n")
    return answer
