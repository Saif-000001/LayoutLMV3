from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add the CORS header
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    # Create and start the HTTP server
    server = HTTPServer(('localhost', 8080), CORSRequestHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()
