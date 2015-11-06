# -*- coding: utf-8 -*-
# rtsserver-control.py
# Main controller for the server
# Author : Jean-Sébastien Beaulieu

from serverview import ServerView
from subprocess import Popen
import Pyro4
from servertools import ServerTools
import time


class ServerController():

    """Controller class for the RTS server."""

    def __init__(self):
        self.ip = str(ServerTools.get_local_ip())
        Popen(["python", "rtsserver.py"])
        try:
            self.connect_server()
        except:
            ServerTools.erbox("Erreur de connexion",
                              "Le serveur n'a pas pu être rejoint.\n" +
                              "Le gestionnaire de serveur va maintenant fermer.")
        else:
            self.gui = ServerView(self.server, ns)
            self.gui_update()
            self.gui.mainloop()

    def gui_update(self):
        self.gui.new_messages()
        self.gui.new_user()
        self.gui.after(50, self.gui_update)

    def connect_server(self):
        """Attempts to open a new server connection."""
        uri = "PYRO:uri@" + self.ip + ":47089"
        self.server = Pyro4.Proxy(uri)
        # self.server.register_user("ADMIN", uri)


if __name__ == '__main__':
    server = ServerController()
