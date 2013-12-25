import socket
import sys
import time
import base64
import json
import config

try:
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((config['host'], config['port']))
        sock.sendall(base64.b64encode(json.dumps(config)))
        # Receive data from the server and shut down
        received = sock.recv(1024)

        print "Received: {}".format(received)

        time.sleep(config['sleep'])
finally:
    sock.close()