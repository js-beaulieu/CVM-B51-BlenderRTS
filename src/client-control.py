# -*- coding: utf-8 -*-
# client-control.py
# Main client controller
# Author : Jean-Sébastien Beaulieu

from server import servertools as st
import Pyro4


class Client():

    """Main client class, to initialize connection with the server
       and share informations with other players."""

    def __init__(self):
        self.ip = st.ServerTools.get_local_ip()
        self.name = "Johnny"
        self.connect_server()

    def connect_server(self):
        """Attempts to open a new server connection."""
        uri = "PYRO:uri@" + str(self.ip) + ":47089"
        print(uri)
        self.server = Pyro4.Proxy(uri)


if __name__ == '__main__':
    client = Client()
