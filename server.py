#import SimpleHTTPServer
#import SocketServer
import http.server
import socketserver
import os

PORT = 8000

import consul
import socket
import uuid

CONSULHOST = os.environ.get('CONSUL_HOST')

# Get the real public ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((CONSULHOST, 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]

c = consul.Consul(host=CONSULHOST)

c.agent.service.register(name='TestWebserver', service_id=str(uuid.uuid4().hex), port=8000, address=local_ip_address)


Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
