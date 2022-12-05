from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.core.dependencies import get_auth0_token_client, authentication
from src.core.config import get_settings, Settings

router = APIRouter()

settings: Settings = get_settings()

@router.post("/")
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

@router.get("/callback")
async def login_callback(
    code: str, 
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