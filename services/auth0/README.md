# Auth0
Auth0 (by Okta) is an Access & User management service. It handles the management of users entities and their access to APIs by applications. </br>
In this application we use the following features of Auth0:
- User management (create and remove). The users database is managed by Auth0 (meaning there is no need to create users table in your own database).
- Authentication service: Authenticate users versus the users database. Once the user is verified (by username and password, or social identification) a JWT is granted. Using this JWT the client can make requests to the server which verifies the JWT each time.
- Authorization service: Authorization is the process of verify the client has the right permissions to access the requested resource. For each request, the server checks the permissions (scopes), that are stored in the JWT, and compare them to the endpoint access permissions.

## Quick Setup of Auth0 Account
At the end of this stage you should have all the environment variables needed to run the application.
1. Sign Up
2. Create a tenant
    - Go to "Settings" -> "Custom Domain" -> and here you should get your tenant domain name (e.g. For tenant name "simple-app-demo" and us region the domain is: "simple-app-demo.us.auth0.com") 
    - AUTH0_DOMAIN="simple-app-demo.us.auth0.com"
    - Go to "Settings" -> "API Authorization Settings" -> set "Default Directory" to "Username-Password-Authentication", and "Save".
3. Create an API
    - "Applications" -> "APIs" -> "+ Create API" (Name: Simple App Backend, Identifier: https://simple-app-backend)
    - AUTH0_API_DEFAULT_AUDIENCE="https://simple-app-backend-fastapi"
    - Goto your API -> "Permissions" -> Add permission of "test:read"
    - Goto your API -> Scroll down to "RBAC Settings" -> "Enable RBAC" -> "Save"
4. Create an Application
    - "Applications" -> "Applications" -> "+ Create Application" -> "Single Page Web Applications", Name: "Backend Test App"
    - Goto "Backend Test App" and use the Client ID and Client Secret for AUTH0_APPLICATION_CLIENT_ID, AUTH0_APPLICATION_CLIENT_SECRET.
    - Add "http://localhost/token/callback" to "Allowed Callback URLs" (this is for the server side social login).
    - Add "http://localhost:3000/login/callback" to "Allowed Callback URLs" (this is for the client side social login).
5. Create test user
    - "User Management" -> "+ Create User" -> Enter any email and password, "Create".
    - Use those credentials for AUTH0_TEST_USERNAME and AUTH0_TEST_PASSWORD
    - Goto the user you created -> "Permissions" -> "Assign Permissions" -> Select "Simple App Backend" -> Select "test:read" -> "Add"
6. Auth0 Management 
    - "Applications" -> "Applications" -> "Auth0 Management API (Test Application)" -> "APIs" -> Expand "Auth0 Management API" and add "delete:users" and "create:users" permissions.
    - Use Client ID and Secret of "Auth0 Management API (Test Application)" for AUTH0_MANAGEMENT_API_CLIENT_ID and AUTH0_MANAGEMENT_API_CLIENT_Secret
    - "Applications" -> "APIs" -> "Auth0 Management API" -> Use "Identifier" for AUTH0_MANAGEMENT_API_AUDIENCE

