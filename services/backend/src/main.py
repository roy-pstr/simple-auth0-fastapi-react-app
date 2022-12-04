import json 

import requests
from fastapi import FastAPI, Request
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from src.dependencies import get_auth0_token_client, get_auth0_users_client, authentication, management, get_auth0_management_client
from src.security.oauth import oauth2_scheme
from src.routes.debug import router as debug_router
from src.config import get_settings, Settings

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    html_page=f"""<!DOCTYPE html>
<html lang="en-us">
<body>
<form target="_blank" action="/token" method="POST">
    <input type="username" id="username" name="username">
    <input type="password" id="password" name="password">
    <input onclick="window.location.href = '/post-login';" type="submit" value="Submit">
    <input onclick="window.location.href = 'https://{settings.AUTH0_DOMAIN}/authorize?response_type=code&scope=openid%20profile%20email&audience={settings.AUTH0_API_DEFAULT_AUDIENCE}&client_id={settings.AUTH0_APPLICATION_CLIENT_ID}&redirect_uri=http://localhost/login/callback&connection=google-oauth2';" type="submit" value="Continue with google">
</form>
</body>
</html>
"""
    return HTMLResponse(content=html_page)

@app.get("/login/callback")
async def login_callback(
    code: str, 
    request: Request,
    auth0_token: authentication.GetToken = Depends(get_auth0_token_client),
):
    response = auth0_token.authorization_code(
        grant_type="authorization_code",
        client_id=settings.AUTH0_APPLICATION_CLIENT_ID, 
        client_secret=settings.AUTH0_APPLICATION_CLIENT_SECRET,
        code=code, 
        redirect_uri="http://localhost/login/callback"
    )
    access_token = response.get("access_token")
    return response


@app.get("/login/success")
async def root(request: Request):
    return "Login success"

# debug route
app.include_router(
    debug_router,
    prefix="/debug",
    tags=["Debug"],
)
settings: Settings = get_settings()

@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    auth0_token: authentication.GetToken = Depends(get_auth0_token_client),
    # settings: Settings = Depends(get_settings) this raise 422 for some reason...
):
    """
    Get access token from auth0 /oauth/token endpoint.
    """
    response = auth0_token.login(
        client_id=form_data.client_id or settings.AUTH0_APPLICATION_CLIENT_ID,
        client_secret=None, 
        username=form_data.username, 
        password=form_data.password, 
        audience=settings.AUTH0_API_DEFAULT_AUDIENCE,
        scope="openid profile email",
        realm=None,
        grant_type="password"
    )

    return {
        "access_token": response["access_token"], 
        "token_type": "bearer"
    }

@app.get("/me")
async def read_user_me(
    access_token: str = Depends(oauth2_scheme), 
    auth0_users: authentication.Users = Depends(get_auth0_users_client)
) -> dict:
    userinfo = auth0_users.userinfo(access_token=access_token)   
    return userinfo

from src.schema import CreateUser
@app.post("/user")
async def create_new_user(
    create_user: CreateUser,
    auth0_mgmt_client: management.Auth0 = Depends(get_auth0_management_client)
):
    """
    Create user in auth0.
    if verify_email=True -> send verification mail
    """
    # Create user in auth0 db
    response = auth0_mgmt_client.users.create(
        body=create_user.dict(exclude_none=True)
        )
    return  response

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: str,
    access_token: str = Depends(oauth2_scheme), 
    auth0_mgmt_client: management.Auth0 = Depends(get_auth0_management_client)
):
    """
    Create user in auth0.
    if verify_email=True -> send verification mail
    """
    # Create user in auth0 db
    response = auth0_mgmt_client.users.delete(
        id=user_id
        )
    
    return {
        "auth0": response
    }