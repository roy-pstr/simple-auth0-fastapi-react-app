from src.auth0 import Auth0API

def get_auth0() -> Auth0API:
    """
    Return instance of Auth0API.
    """
    return Auth0API()

