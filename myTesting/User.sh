curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{}' http://localhost:5000/db/api/clear/
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"username":"User1", "about":"i am user1", "name": "Ivan", "email": "a@mail.ru", "isAnonymous": false}' http://localhost:5000/db/api/user/create/
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"username":"User2","about":"i am user without anonymous param", "name": "Ivan2", "email": "adb@mail.ru"}' http://localhost:5000/db/api/user/create/
curl -X GET http://localhost:5000/db/api/user/details/?user=example3@mail.ru
