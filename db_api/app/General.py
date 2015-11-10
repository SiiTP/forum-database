from app import app, cursor
from flask import request
import json

@app.route("/db/api/clear/", methods = ['POST'])
def clear():
    cursor.execute("DELETE FROM User;")
    cursor.execute("DELETE FROM Forum;")
    cursor.execute("DELETE FROM Post;")
    cursor.execute("DELETE FROM Thread;")
    cursor.execute("DELETE FROM Forum_User;")
    cursor.execute("DELETE FROM Follower;")
    response = json.dumps({"code": 0, "response": "OK"})
    return response
    
@app.route("/db/api/status/", methods = ['GET'])
def status():
    db_info = { "forum": 0, "user": 0, "thread": 0, "post": 0 }
    db_info["forum"] = cursor.execute("SELECT COUNT(*) FROM Forum")
    db_info["user"] = cursor.execute("SELECT COUNT(*) FROM User")
    db_info["thread"] = cursor.execute("SELECT COUNT(*) FROM Thread")
    db_info["post"] = cursor.execute("SELECT COUNT(*) FROM Post")
    
    response = json.dumps({"code": 0, "response": db_info})
    return response
    

