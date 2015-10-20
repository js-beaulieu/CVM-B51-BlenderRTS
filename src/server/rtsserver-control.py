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
        try:
            self.connect_server()
        except:
            ServerView.erbox("Erreur de connexion",
                             "Le serveur n'a pas pu être rejoint.\n" +
                             "Le gestionnaire de serveur va maintenant fermer.")
        else:
            self.gui = ServerView(self.server)
            self.gui.server_event("Serveur démarré. Informations de connexion:")
            self.gui.server_event(self.get_local_ip() + "/" + str(47089))
            self.gui_update()
            self.gui.mainloop()

    def gui_update(self):
        self.gui.new_messages()
        self.gui.after(250, self.gui_update)

    def connect_server(self):
        """Attempts to open a new server connection."""
        ip = self.get_local_ip()
        uri = "PYRO:uri@" + ip + ":47089"
        self.server = Pyro4.Proxy(uri)

    def get_local_ip(self):
        """Returns the local IP address"""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
        strs = str(s.getsockname()[0])
        return strs


if __name__ == '__main__':
    server = ServerController()
