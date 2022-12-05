from auth0.v3 import authentication, management

from src.core.config import get_settings, Settings

def get_auth0_token_client() -> authentication.GetToken:
    """
    Return instance of GetToken.
    """
    settings: Settings = get_settings()
    return authentication.GetToken(settings.AUTH0_DOMAIN)

def get_auth0_users_client() -> authentication.Users:
    """
    Return instance of GetToken.
    """
    settings: Settings = get_settings()
    return authentication.Users(settings.AUTH0_DOMAIN)

def get_auth0_management_client() -> management.Auth0:
    """
    Return instance of Auth0 management API.
    """
    settings: Settings = get_settings()
    auth0_token = get_auth0_token_client()
    response = auth0_token.client_credentials(
        client_id=settings.AUTH0_MANAGEMENT_API_CLIENT_ID,
        client_secret=settings.AUTH0_MANAGEMENT_API_CLIENT_SECRET, 
        audience=settings.AUTH0_MANAGEMENT_API_AUDIENCE
        )
    mgmt_api_token = response['access_token']
    
    auth0 = management.Auth0(settings.AUTH0_DOMAIN, mgmt_api_token)
    
    return auth0




