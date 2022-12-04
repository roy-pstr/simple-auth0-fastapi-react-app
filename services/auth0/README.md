# Auth0
Auth0 (by Okta) is an Access & User management service. It handles the management of users entities and their access to different APIs using different applications. </br>
In this application we demonstrate the following features of Auth0:
- User management (create and remove). The users database is managed by Auth0 (meaning there is no need to create users table in your own database).
- Authentication service: Authenticate users versus the users database. Once user is verified (using username and password, or social identification) a JWT is granted. Using this JWT a client can make requests to the server which verify the JWT each time (JWT verification is made by the server side using public key from Auth0).
- Authorization service: Authorization is the process of verify the client has the right permissions to access the requested resource. For each request, the server checks the permissions (scopes), that are stored in the JWT, and compare them to the endpoint access permissions.

## Quick Setup of Auth0 Account
At the end of this stage you should have all the environment variables needed to run the application.
1. Sign Up
2. Create tenant
3. Create Application
4. Create API
    - create permission 'test:read'
5. Create test user
    - Add permission: 'test:read'