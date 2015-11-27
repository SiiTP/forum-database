curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"follower": "aadb@mail.ru", "followee": "a@mail.ru"}' http://localhost:5000/db/api/user/follow/
curl -X GET http://localhost:5000/db/api/user/listFollowers/?user=a@mail.ru
