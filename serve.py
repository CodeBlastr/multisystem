from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/api/'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"message": "Hello from Backend API"}')
        else:
            super().do_GET()

PORT = 80
with HTTPServer(('0.0.0.0', PORT), CustomHandler) as server:
    print(f"Serving on port {PORT}")
    server.serve_forever()
