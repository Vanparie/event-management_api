# Authentication Setup

This project uses Django REST Framework’s Token Authentication to secure API endpoints.

## How to Authenticate
1. **Obtain a Token:**
   - Send a `POST` request to `/api/token/` with valid credentials.
   - Example Request:
     ```bash
     curl -X POST http://127.0.0.1:8000/api/token/ -d "username=admin&password=yourpassword"
     ```
   - Example Response:
     ```json
     {
         "token": "abcd1234efgh5678ijkl9012mnop3456"
     }
     ```

2. **Access Protected Endpoints:**
   - Include the token in the `Authorization` header for all secured endpoints.
   - Example:
     ```bash
     curl -X GET http://127.0.0.1:8000/api/events/ -H "Authorization: Token abcd1234efgh5678ijkl9012mnop3456"
     ```

## Testing
- Use tools like **Postman**, **Thunder Client**, or `curl` to interact with the API.
