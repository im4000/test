"""
    - start app from this
"""

class StartUp:

    def __init__(self):
        super(StartUp, self).__init__()

    def __start_sockettcp_services__(self):
        """ this function start all services on this app
            :params:
            :return:
        """
        from modules.services.sockettcp.socket_server import SocketServer

        SocketServer().run()

    def start(self):
        """ this function start app from this lines
            :params:
            :return: 
        """
        self.__start_sockettcp_services__()