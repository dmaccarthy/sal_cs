"""Static file server using Python's standard http.server module"""

from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
print(f"Serving on 'http://localhost:{PORT}'")
httpd.serve_forever()

