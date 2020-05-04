## Hello flask

### setup
clone this repository

```
$ cd hello_flask
$ pipenv install
```

### run

```
$ pipenv run python hello_flask.py
```

### api

```
$ curl http://localhost:5000/api/test
$ curl -X POST http://localhost:5000/api/test/1234
```

json
```
$ curl http://localhost:5000/api
$ curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' http://localhost:5000/api -d '{"data":"hoge"}'
```