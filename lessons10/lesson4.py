import http.server
import socketserver

with socketserver.TCPServer(('0.0.0.0', 8000),
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()