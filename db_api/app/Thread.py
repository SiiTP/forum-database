from app import app, mysql

@app.route("/db/api/thread/create", methods = ['POST'])
def createThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/close", methods = ['POST'])
def closeThread():
    response = json.dumps({ "code": 0 })
    return response
    
@app.route("/db/api/thread/details", methods = ['GET'])
def threadDetails():
    response = json.dumps({ "code": 0 })
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
