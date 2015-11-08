curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"name":"forum1","short_name":"f1", "user": "a@mail.ru"}' http://localhost:5000/db/api/forum/create/
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"name":"forum2","short_name":"f2", "user": "not_exist@mail.ru"}' http://localhost:5000/db/api/forum/create/
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"name":"forum3","short_name":"f3",  user": "bad_json@mail.ru"}' http://localhost:5000/db/api/forum/create/
