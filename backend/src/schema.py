import typing
from pydantic import BaseModel

from src.config import get_settings, Settings
settings: Settings = get_settings()

class CreateUser(BaseModel):
    connection: str = settings.AUTH0_DEFAULT_DB_CONNECTION
    email: str
    password: str
    name: str
    verify_email: bool = False  # Whether the user will receive a verification email after creation (true) or no email (false). Overrides behavior of email_verified parameter.
    email_verified: typing.Optional[
        bool
    ] = False  # Whether this email address is verified (true) or unverified (false). User will receive a verification email after creation if email_verified is false or not specified
    given_name: typing.Optional[str] = None
    family_name: typing.Optional[str] = None
    nickname: typing.Optional[str] = None
    picture: typing.Optional[str] = None