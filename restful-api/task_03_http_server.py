#!/usr/bin/python3
"""Simple API using http.server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


HOST = "127.0.0.1"
PORT = 8000


class APIHandler(BaseHTTPRequestHandler):
    """Handles HTTP GET requests"""

    def do_GET(self):
        """Handle GET requests to different endpoints"""
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")  # Correct JSON content type
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(bytes(json.dumps(data), "utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API! Use /data or /status", "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", "utf-8"))


def run(server_class=HTTPServer, handler_class=APIHandler, host=HOST, port=PORT):
    """Start and Run server on port 8000"""
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on {host}:{port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
