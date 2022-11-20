from fastapi import FastAPI
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Security

from src.auth0 import Auth0API
from src.dependencies import get_auth0
from src.security.oauth import oauth2_scheme
from src.security.funcs import verify_token
from src.security.funcs import verify_token_scoped
# from src.apis.dependencies import get_auth0_management
# from src.utils.auth0 import CreateUser
# from src.utils.auth0 import Auth0ManagementAPI
from src.config import get_settings, Settings

app = FastAPI()
settings: Settings = get_settings()

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
    return {"message": "Hello from fullstack-react-fastapi-auth0 backend server. try /docs."}

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/private", dependencies=[Depends(verify_token)])
def private():
    """A valid access token is required to access this route"""
    response = "Hello from a private endpoint! If you see this, you're authenticated."
    return response

@app.get(
    "/private-scoped",
    dependencies=[Security(verify_token_scoped, scopes=["test:read"])],
)
def private_scoped():
    """A valid access token with scope of test:read is required to access this route"""
    response = "Hello from a private endpoint! if you see this, you're authenticated and have the scope of test:read."
    return response

@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    auth0_api: Auth0API = Depends(get_auth0)
):
    """
    Get access token from auth0 /oauth/token endpoint.
    """
    response_json = auth0_api.login(username=form_data.username, password=form_data.password, client_id=form_data.client_id or settings.AUTH0_APPLICATION_CLIENT_ID)

    return {"access_token": response_json["access_token"], "token_type": "bearer"}

@app.get("/me")
async def read_user_me(
    user_access_token: str = Depends(oauth2_scheme), 
    auth0_api: Auth0API = Depends(get_auth0)
) -> dict:
    user = auth0_api.get_user(user_access_token=user_access_token)   
    return user

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