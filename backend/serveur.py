import http.server
import time

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

PORT = 8080
server_address = ("", PORT)

httpd = server(server_address, handler)


httpd.serve_forever()
