# Frontend application
This is a simple React application to provide user interface to the underlying backend server.


## Setup
Use the package manager [npm](https://docs.npmjs.com/cli/v6/commands/npm-install) to install client dependencies.

```bash
npm install
```

### Environment variables
```bash
cd frontend
touch .env
```
Set the following variables in the `.env` file (use corresponding values from backend .env file):
```bash
REACT_APP_BACKEND_URL="http://localhost"
REACT_APP_AUTH0_DOMAIN=
REACT_APP_AUTH0_API_DEFAULT_AUDIENCE=
REACT_APP_AUTH0_APPLICATION_CLIENT_ID=
```

## Testing
TBA

## Usage
```bash
npm start
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
