## Social Network

# Features

- SignUp/Login
- View/Create/Edit/Delete Posts
- Like/Dislike posts of other people

# Run

Clone repository
``` sh
git clone https://github.com/IvMaslov/SocialNewtork
```

then create and activate virtualenv
``` sh
virtualenv venv
source venv/bin/activate
```

Install requirements
``` sh
pip install -r requirements.txt
```

Start database into docker
``` sh
docker-compose up -d
```

Final step: run application
``` sh
uvicorn main:app --reload
```

# Docs

- [Swagger](http://localhost:8000/docs)

- [Redoc](http://localhost:8000/redoc)