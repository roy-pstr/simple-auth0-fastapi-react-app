# Fullstack react fastapi auth0

This is a simple frontend and backend service that uses Auth0 as 3rd party authentication service. Backend is in FastAPI, integrated with auth0-python client. Frontend is vanilla react application contains simple login and signup forms, includes support in google account login (through Auth0).

## Application Features
### Client-side
- Login (username and password)
- Signup (username and password)
- Google account login

### Server-side
#### Endpoints
- POST /token : exchange username and password with access token (JWT) from Auth0 service
- GET /me : exchange access token with user info
- POST /user : create user in Auth0 database connection
- DELETE /user/{user_id} : remove user from Auth0 database connection
* When using google account login for the first time a user entity will be created in Auth0 with corresponding user id. This user can be deleted (from Auth0) using the user_id and the DELETE /user endpoint. the social login occurs directly between the client side and the Auth0 service w/o going through the backend.

#### Authentication & Authorizations
- JWT verification
- Private endpoint example (must have access token to get access)
- Scoped-private endpoint example (must have access token and permissions to get access)

## Installation

Use the package manager [poetry](https://python-poetry.org/docs/) to install python dependencies and [npm](https://docs.npmjs.com/cli/v6/commands/npm-install) to install client dependencies.

```bash
cd backend
poetry install
cd ../frontend
npm install
```

### Set environment
```bash
cd backend
touch .env
```
Set the following variables in the `.env` file:
```bash
AUTH0_DOMAIN= 
AUTH0_ALGORITHMS= 
AUTH0_ISSUER= 
AUTH0_DEFAULT_DB_CONNECTION = 
AUTH0_API_DEFAULT_AUDIENCE= 
AUTH0_APPLICATION_CLIENT_ID= 
AUTH0_TEST_USERNAME=
AUTH0_TEST_PASSWORD=
AUTH0_MANAGEMENT_API_CLIENT_ID=
AUTH0_MANAGEMENT_API_CLIENT_SECRET=
AUTH0_MANAGEMENT_API_AUDIENCE=
```
Those values are from Auth0. You should have a tenant with domain, an API and an Application 

## Testing
### Backend
```bash
./backend/scripts/test
```

### Frontend
TBA
```bash
./frontend/scripts/test
```

## Usage

### Backend
```bash
./backend/scripts/run
```

### Frontend
```bash
./frontend/scripts/run
```

## Open Tasks
- A script for auto create Auth0 environment given Auth0 Management credentials only. 
- Upgrade frontend user interface a bit,
- Add .env file to frontend side.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)