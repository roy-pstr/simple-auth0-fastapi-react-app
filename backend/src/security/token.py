from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel


class AccessToken(BaseModel):
    """
        Access token schema based on auth0 token (should match any jwt standard)

        Example:
        {
          "iss": "https://****.us.auth0.com/",
          "sub": "auth0|61e0451a690cd100686*****",
          "aud": [
            "https://****.us.auth0.com/userinfo"
          ],
          "iat": 1642932778,
          "exp": 1643019178,
          "azp": "dM01vq4BFSKRCLhQqRmRDoujMBoo5aTJ",
          "scope": "openid profile email",
          "gty": "password",
          "permissions": [
            "test:read",
            "test:write"
          ]
        }
    """

    iss: str
    sub: str
    aud: Union[str, List[str]] = []
    iat: str
    exp: str
    azp: str
    scope: str
    gty: Optional[str]
    permissions: List[str] = []
