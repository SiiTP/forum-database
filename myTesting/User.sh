curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{}' http://localhost:5000/db/api/clear/
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"username":"User1", "about":"i am user1", "name": "Ivan", "email": "a@mail.ru", "isAnonymous": false}' http://localhost:5000/db/api/user/create/
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"username":"User2","about":"i am user without anonymous param", "name": "Ivan2", "email": "adb@mail.ru"}' http://localhost:5000/db/api/user/create/
curl -X GET http://localhost:5000/db/api/user/details/?user=adb@mail.ru

info: Requesting http://127.0.0.1:5000/db/api/forum/listUsers/ with {'order': 'desc', 'forum': 'forum1'} (GET)

info: Request time was: 0.0105 sec

info: Validating by requesting list of objects

error: Attribute <username> from API response (value=u'user4') dont match test object (value='user2')

error: Attribute <username> from API response (value=u'user2') dont match test object (value='user1')

error: Attribute <username> from API response (value=u'user1') dont match test object (value='user4')


