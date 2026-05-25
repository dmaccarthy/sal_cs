"""Static file server using Python's standard http.server module"""

import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on 'http://localhost:{PORT}'")
    httpd.serve_forever()
