
from socket import(
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)


class SocketClientTCP:

    def __init__(self):
        super(SocketClientTCP, self).__init__()

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    
    def __connect__(self):
        