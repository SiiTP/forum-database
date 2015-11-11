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
    
@app.route("/db/api/thread/close", methods = ['POST'])
def closeThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/details/", methods = ['GET'])
def threadDetails():
    print("\n\n===================THREAD DETAILS BEGIN=====================\n=====================================================\n")

    try:
        thread = request.args.get("thread")
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})
    try:
        related = request.args.getlist("related")
    except:
        print("related is empty")
        related = []
    related = []
    print("\nrelated : ")
    print(related)
    answer = getThreadDetailsByID(thread, related)
    if not answer:
        return json.dumps({"code": 1, "response": error_messages[1]})
    response = json.dumps({ "code": 0, "response": answer})
    print("\nRESPONSE : ")
    print(response)
    print("\n===================THREAD DETAILS END=====================\n=====================================================\n")
    return response
    
@app.route("/db/api/thread/list", methods = ['GET'])
def threadsList():
    response = json.dumps({ "code": 0 })
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
    print("\nforum details : ")
    print(forum_details)
    print(forum_details["short_name"])
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
        print("\nAnswer[forum] : ")
        print(answer["forum"])
    # print("\n\nAnswer : ")
    # print(answer)
    # print("\n")
    return answer
