import SocketServer
import time
import config


class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()

        print "{} wrote:".format(self.client_address[0])
        print "%s %s" % (int(time.time()), self.data)

        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    server = SocketServer.TCPServer((config.config['host'], config.config['port']), TCPHandler)
    server.serve_forever()
