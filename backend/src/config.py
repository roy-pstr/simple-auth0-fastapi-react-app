import platform

from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    """
    Settings for the FastAPI server.
    Based on pydantic BaseSettings - powerful tool autoload the .env file in the background.
    """
    DUMMY: str
    # AUTH0_DOMAIN: str = "auth.larium.ai"
    # AUTH0_ALGORITHMS: str = "RS256"
    # AUTH0_ISSUER: str = "https://auth.larium.ai/"

    # # Management API
    # AUTH0_MANAGEMENT_API_CLIENT_ID: str
    # AUTH0_MANAGEMENT_API_CLIENT_SECRET: str
    # AUTH0_MANAGEMENT_API_AUDIENCE: str = "https://larium-dev.us.auth0.com/api/v2/"

    # # Connection:
    # AUTH0_DEFAULT_DB_CONNECTION: str = "Beta-users"

    # # API:
    # AUTH0_API_AUDIENCE: str = "https://api-dev.larium.ai"

    class Config:
        """
        Tell BaseSettings the env file path
        """

        env_file = ".env"


@lru_cache()
def get_settings(**kwargs):
    """
    Get settings. ready for FastAPI's Depends.
    lru_cache - cache the Settings object per arguments given.
    """
    settings = Settings(**kwargs)
    return settings
