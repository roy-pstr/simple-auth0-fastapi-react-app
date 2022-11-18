from fastapi import FastAPI
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
# from src.utils.auth0 import Auth0API
# from src.apis.dependencies import get_auth0
# from src.apis.dependencies import get_auth0_management
# from src.utils.auth0 import CreateUser
# from src.utils.auth0 import Auth0ManagementAPI

app = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def root():
    return {"message": "Hello World"}
            
# @app.post("/token")
# async def login_for_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(), auth0_api: Auth0API = Depends(get_auth0)
# ):
#     """
#     Get access token from auth0 /oauth/token endpoint.
#     """
#     response = auth0_api.login(username=form_data.username, password=form_data.password, client_id=form_data.client_id)
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail=response.text)

#     response_json = response.json()

#     return {"access_token": response_json["access_token"], "token_type": "bearer"}

# @app.post("/user")
# async def create_new_user(
#     create_user: CreateUser,
#     auth0_api: Auth0ManagementAPI = Depends(get_auth0_management)
# ):
#     """
#     Create user in auth0.
#     if verify_email=True -> send verification mail
#     """
#     # Create user in auth0
#     response = auth0_api.create_user(body=create_user.dict(exclude_none=True))  # raise for status -> HTTPException
    
#     return {
#         "auth0": response
#     }