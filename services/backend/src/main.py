from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routes import debug
from src.routes import token
from src.routes import user
from src.core.config import get_settings, Settings

app = FastAPI()
settings: Settings = get_settings()

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

app.include_router(
    debug.router,
    prefix="/debug",
    tags=["Debug"],
)
app.include_router(
    token.router,
    prefix="/token",
    tags=["Token"],
)
app.include_router(
    user.router,
    prefix="/user",
    tags=["Users"],
)

@app.get("/")
async def root():
    html_page=f"""<!DOCTYPE html>
<html lang="en-us">
<body>
<form target="_blank" action="/token" method="POST">
    <input type="username" id="username" name="username">
    <input type="password" id="password" name="password">
    <input type="submit" value="Submit">
    <input onclick="window.location.href = 'https://{settings.AUTH0_DOMAIN}/authorize?response_type=code&scope=openid%20profile%20email&audience={settings.AUTH0_API_DEFAULT_AUDIENCE}&client_id={settings.AUTH0_APPLICATION_CLIENT_ID}&redirect_uri=http://localhost/token/callback&connection=google-oauth2';" type="submit" value="Continue with google">
</form>
</body>
</html>
"""
    return HTMLResponse(content=html_page)

