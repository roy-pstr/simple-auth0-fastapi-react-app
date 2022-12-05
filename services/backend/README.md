# Backend Server
This is a FastAPI backend for a simple user management and authentication service based on Auth0.

## Endpoints
- POST /token : exchange username and password with access token (JWT) from Auth0 service
- GET /token/callback : callback from social login flow.
- GET /user/me : exchange access token with user info
- POST /user : create user in Auth0 database connection
- DELETE /user/{user_id} : remove user from Auth0 database connection
* When using google account login for the first time a user entity will be created in Auth0 with corresponding user id. This user can be deleted (from Auth0) using the user_id and the DELETE /user endpoint. the social login occurs directly between the client side and the Auth0 service w/o going through the backend.

## Dependencies
- auth0-python
- FastAPI

## Setup
### Python environment  
Use the package manager [poetry](https://python-poetry.org/docs/) to install python dependencies.
```bash
./scripts/install
```

### Environment variables
```bash
touch .env
```
Set the following variables in the `.env` file:
```bash
AUTH0_DOMAIN= 
AUTH0_API_DEFAULT_AUDIENCE= 
AUTH0_APPLICATION_CLIENT_ID= 
AUTH0_APPLICATION_CLIENT_SECRET= 
AUTH0_TEST_USERNAME=
AUTH0_TEST_PASSWORD=
AUTH0_MANAGEMENT_API_CLIENT_ID=
AUTH0_MANAGEMENT_API_CLIENT_SECRET=
AUTH0_MANAGEMENT_API_AUDIENCE=
```
Those values are from Auth0. See README.md in auth0 dir.

## Testing
```bash
./scripts/test
```

## Usage
This will start a local server on your local machine. Go to `http://localhost` to simple HTML user interface or `http://localhost/docs` to see the OpenAPI docs (interactive).
```bash
./scripts/run
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
