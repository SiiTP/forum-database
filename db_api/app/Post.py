from app import app, mysql

@app.route("/db/api/post/create", methods = ['POST'])
def createPost():
    response = json.dumps({ "code": 0 })
    return response
    

@app.route("/db/api/post/details", methods = ['GET'])
def postDetails():
    response = json.dumps({ "code": 0, "response": "details" })
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
