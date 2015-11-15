from app import app, cursor
from functions import *
from User import *
from Forum import *
from Thread import *
from flask import request
import json

@app.route("/db/api/post/create/", methods = ['POST'])
def createPost():
    print("\n================Post CREATION\n")
    print("Request : ")
    print(request.json)
    print(request.json["thread"])
    try:
        thread = request.json["thread"]
        message = request.json["message"]
        date = request.json["date"]
        user = request.json["user"]
        forum = request.json["forum"]
        print("Thread : " + str(thread))
        print("Message : " + message)
        print("Date : " + str(date))
        print("User : " + str(user))
        print("Forum : " + str(forum))

    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    parent        = getOptionalParameterOrDefault(request.json, "parent", None)
    isApproved    = getOptionalParameterOrDefault(request.json, "isApproved", False)
    isHighlighted = getOptionalParameterOrDefault(request.json, "isHighlighted", False)
    isEdited      = getOptionalParameterOrDefault(request.json, "isEdited", False)
    isSpam        = getOptionalParameterOrDefault(request.json, "isSpam", False)
    isDeleted     = getOptionalParameterOrDefault(request.json, "isDeleted", False)

    try:
        id_Forum = getForumDetailsByShortName(forum)["id"]
        id_User = getUserInfoByEmail(user)["id"]
    except:
        return json.dumps({"code": 2, "response": error_messages[2]})

    sql = "INSERT INTO Post(parent, isApproved, isHighlighted, isEdited, isSpam, isDeleted, likes, dislikes, date, message, idForum, idThread, idAuthor) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,    [parent, isApproved, isHighlighted, isEdited, isSpam, isDeleted,     0,        0, date, message, id_Forum,  thread, id_User])

    sql = "SELECT MAX(idPost) FROM Post"
    cursor.execute(sql)
    idP = cursor.fetchone()[0]

    answer = {}
    answer["id"] = idP
    answer["parent"] = parent
    answer["isApproved"] = isApproved
    answer["isHighlighted"] = isHighlighted
    answer["isEdited"] = isEdited
    answer["isSpam"] = isSpam
    answer["isDeleted"] = isDeleted
    answer["likes"] = 0
    answer["dislikes"] = 0
    answer["points"] = answer["likes"] - answer["dislikes"]
    answer["date"] = date
    answer["message"] = message
    answer["forum"] = forum
    answer["thread"] = thread
    answer["user"] = user
    response = json.dumps({"code": 0, "response": answer })
    print('\n' + response)
    print("\n================SUCCESSFUL Post CREATION\n")
    return response
    

@app.route("/db/api/post/details/", methods = ['GET'])
def postDetails():
    print("\n\n===================POST DETAILS BEGIN=====================\n============================================================\n")

    try:
        post = request.args.get("post")
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
    print("post : ")
    print(post)
    answer = getPostDetailsByID(post, related)
    if not answer:
        return json.dumps({"code": 1, "response": error_messages[1]})
    response = json.dumps({ "code": 0, "response": answer})
    print("\nRESPONSE : ")
    print(response)
    print("\n===================POST DETAILS END=====================\n============================================================\n")
    return response
    
@app.route("/db/api/post/list", methods = ['GET'])
def postsList():
    response = json.dumps({ "code": 0, "response": "details" })
    return response

@app.route("/db/api/post/remove", methods = ['POST'])
def removePost():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/post/restore", methods = ['POST'])
def restorePost():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/post/update", methods = ['POST'])
def updatePost():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/post/vote", methods = ['POST'])
def votePost():
    response = json.dumps({ "code": 0 })
    return response

def getPostDetailsByID(postID, related):
    sql = "SELECT * FROM Post WHERE idPost = %s"
    cursor.execute(sql, postID)
    data = cursor.fetchone()
    print(data)
    if (not data):
        print("\nThread not found")
        return None
    answer = {}
    answer["id"] = data[0]
    answer["parent"] = data[1]
    answer["isApproved"] = data[2]
    answer["isHighlighted"] = data[3]
    answer["isEdited"] = data[4]
    answer["isSpam"] = data[5]
    answer["isDeleted"] = data[6]
    answer["likes"] = data[7]
    answer["dislikes"] = data[8]
    answer["date"] = str(data[9])
    answer["message"] = data[10]
    answer["forum"] = getForumDetailsById(data[11])["short_name"]
    answer["thread"] = data[12]
    answer["user"] = getUserInfoByID(data[13])["email"]
    answer["points"] = answer["likes"] - answer["dislikes"]

    if "user" in related:
        data_user = getUserInfoByEmail(answer["user"])
        answer["user"] = data_user
    if "forum" in related:
        answer["forum"] = getForumDetailsByShortName(answer["forum"])
    if "thread" in related:
        answer["thread"] = getThreadDetailsByID(answer["thread"], [])
    print("\n===========Answer getPostByID() : ")
    print(answer)
    print("===================================\n")
    return answer