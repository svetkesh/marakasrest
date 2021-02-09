# marakasrest

Choose DB to use
in config.py
```
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url  # or postgresql_url
```

Run server with
```
$ python api/server.py
```

Browse Api examples at
Marakas Demo Home Page
http://localhost:5000/

Or find Swagger at
http://localhost:5000/api/ui/

Re-build DB with
```
python api/build_database.py
```
