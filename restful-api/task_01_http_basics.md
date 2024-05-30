# HTTP/HTTPS Basics

## HTTP vs HTTPS

- **HTTP (Hypertext Transfer Protocol)**: The foundation of data communication on the web. It transfers data in plain text.
- **HTTPS (HTTP Secure)**: An extension of HTTP. It uses SSL/TLS to encrypt data for secure communication.

## HTTP Methods

1. **GET**: Retrieve data.
2. **POST**: Submit data to be processed.
3. **PUT**: Update existing data.
4. **DELETE**: Remove data.

## HTTP Status Codes

1. **200 OK**: The request was successful.
2. **201 Created**: The request was successful, and a resource was created.
3. **400 Bad Request**: The server could not understand the request due to invalid syntax.
4. **404 Not Found**: The server cannot find the requested resource.
5. **500 Internal Server Error**: The server encountered an unexpected condition.

## HTTP Structure

- **Request**: Includes method, URL, headers, and body (optional).
- **Response**: Includes status code, headers, and body.

Example:
```http
GET /index.html HTTP/1.1
Host: www.example.com
