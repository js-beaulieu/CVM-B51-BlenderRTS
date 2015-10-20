# -*- coding: utf-8 -*-
# rtsserver-control.py
# Main controller for the server
# Author : Jean-Sébastien Beaulieu

from serverview import ServerView
from subprocess import Popen
import Pyro4
import socket


class ServerController():

    """Controller class for the RTS server."""

    def __init__(self):
        Popen(["python", "rtsserver.py"])
        self.connect_server()
        self.gui = ServerView(self.server)
        self.gui_update()
        if self.server.is_initialized():
            self.gui.server_event("Connexion au serveur réussie!")
            self.gui.server_event(self.get_local_ip() + "/" + str(47089))
        else:
            self.gui.server_event("Erreur de connexion. Relancer le serveur.")
        self.gui.mainloop()

    def gui_update(self):
        self.gui.new_messages()
        self.gui.after(250, self.gui_update)

    def connect_server(self):
        """Attempts to open a new server connection."""
        try:
            ip = self.get_local_ip()
            uri = "PYRO:uri@" + ip + ":47089"
            self.server = Pyro4.Proxy(uri)
        except:
            pass

    def get_local_ip(self):
        """Returns the local IP address"""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
        strs = str(s.getsockname()[0])
        return strs


if __name__ == '__main__':
    server = ServerController()
