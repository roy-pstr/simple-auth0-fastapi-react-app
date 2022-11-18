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

## Usage
### Backend
```bash
poetry run uvicorn src.main:app --host 0.0.0.0 --port 80
```

### Frontend
```bash
npm start
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)