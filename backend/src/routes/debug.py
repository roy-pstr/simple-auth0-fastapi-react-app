from fastapi import APIRouter
from fastapi import Depends
from fastapi import Security

from src.security.funcs import verify_token
from src.security.funcs import verify_token_scoped

router = APIRouter()

@router.get("/ping")
async def ping():
    return "pong"

@router.get("/private", dependencies=[Depends(verify_token)])
def private():
    """A valid access token is required to access this route"""
    response = "Hello from a private endpoint! If you see this, you're authenticated."
    return response

@router.get(
    "/private-scoped",
    dependencies=[Security(verify_token_scoped, scopes=["test:read"])],
)
def private_scoped():
    """A valid access token with scope of test:read is required to access this route"""
    response = "Hello from a private endpoint! if you see this, you're authenticated and have the scope of test:read."
    return response
