
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)

from datetime import datetime

from utils.config_manager import ConfigManager
from commons.constants.colors import Color

from .client_handler import ClientHandler


class SocketServer:
    """
        This class creates socket stream on TCP protocol
    """

    def __init__(self):
        super(SocketServer, self).__init__()

        self.config_manager = ConfigManager()

        self.sock_connection = socket(AF_INET, SOCK_STREAM)
        self.sock_connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.__start__()

    def __start__(self):
        """ This method creates socket connection
            :params:
            :return:
        """

        self.sock_connection.bind((
            self.config_manager.get().socket_server.IP, # TODO: change get() => property
            self.config_manager.get().socket_server.PORT 
        ))

        self.sock_connection.listen(
            self.config_manager.get().socket_server.LISTEN_CLIENT
        )

        print(str(datetime.now()).split('.')[0] + " => [+] Server is ready to listening")

    def run(self):
        """ start server for listening clients
            :params:
            :return:
        """

        client, client_address = self.sock_connection.accept()

        # we create new thread per client that connect to server
        ClientHandler(
            client,
            client_address
        ).start()

        self.run()