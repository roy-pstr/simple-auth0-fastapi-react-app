import json
from typing import Dict

import requests
from pydantic import EmailStr
from fastapi import HTTPException

from src.config import get_settings


settings = get_settings()


class Auth0API:
    """
    This Auth0API client supports the following methods:
    1. password flow login - given username and password will return the access token and id token if credentials are valid and exist in the AUTH0_DOMAIN.
    2. change password flow - given email and connection will send an email to the user with a link to change the password.
    3. get user info - given access token will return the user info.
    
    """
    def __init__(self, 
            auth0_domain: str = settings.AUTH0_DOMAIN
        ) -> None:
        self.url = f"https://{auth0_domain}"

    def login(self, username: str, password: str, client_id: str) -> requests.Response:
        """
        Login using password flow.
        (username, password) are the credentials of the user. if the user exist in the AUTH0_DOMAIN, then the access token and id token will be returned.

        Args:
            username (str): _description_
            password (str): _description_
            client_id (str): _description_

        Returns:
            requests.Response: _description_
        """
        response = requests.post(
            f"https://{settings.AUTH0_DOMAIN}/oauth/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "password",
                "username": username,
                "password": password,
                "audience": settings.AUTH0_API_DEFAULT_AUDIENCE,
                "scope": "openid profile email",
                "client_id": client_id,
            },
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
        return response.json()

    def get_user(self, user_access_token: str) -> Dict:
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {user_access_token}",
        }
        response = requests.get(url=f"{self.url}/userinfo", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return json.loads(response.text)

    def change_password(self, email: str, connection: str) -> None:
        headers = {
            "accept": "application/json",
        }
        response = requests.post(
            url=f"{self.url}/dbconnections/change_password",
            headers=headers,
            json={"email": email, "connection": connection},
        )
        if response.status_code > 201:
            raise HTTPException(status_code=response.status_code, detail=response.text)
