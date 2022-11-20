# Fullstack react fastapi auth0

This app is meant to quickstart any user authentication and authorization service using FastAPI as python backend, React for client-side, and auth0 as the authentication and authorization service. 
Currently supports:
- Login
- Signup
- Signup/Login with a google account


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
AUTH0_DOMAIN = 
AUTH0_ALGORITHMS = 
AUTH0_ISSUER = 
AUTH0_DEFAULT_DB_CONNECTION  = 
AUTH0_API_DEFAULT_AUDIENCE = 
AUTH0_APPLICATION_CLIENT_ID = 
AUTH0_TEST_USERNAME=
AUTH0_TEST_PASSWORD=
```


## Testing
### Backend
```bash
./backend/scripts/test.sh
```

### Frontend
```bash
./frontend/scripts/test.sh
```

## Usage

### Backend
```bash
./backend/scripts/run.sh
```

### Frontend
```bash
./frontend/scripts/run.sh
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)