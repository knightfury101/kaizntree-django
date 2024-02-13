# Kaizntree Django Backend

Documentation for the API backend can be found at Swagger. (http://3.86.93.165:8000/docs/)

## Installation

- To run the server locally, make ```.env.dev``` and keep it empty.
- Run ```docker-compose up --build```
- Access it on ```localhost:8000/docs```

Swagger Steps:
- Register a user.
- Authenticate the user and you'll get an access token.
- On top of the API table, you'll have the authorize option.
- Type ```Bearer <Access Token>``` and authorize it.
- Create tags, create categories, and then create products. Now you should be able to use all the APIs. 
