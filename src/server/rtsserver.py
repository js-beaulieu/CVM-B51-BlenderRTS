# -*- coding: utf-8 -*-
# rtsserver.py
# Main model for the server
# Author : Jean-Sébastien Beaulieu

import Pyro4
from random import randint
import socket
from serverview import ServerView


class GameData():

    """Used by **RTSTITLE** server to manage user data
       and syncing game data between clients."""

    def __init__(self):
        self.registering = True
        self.players = {}
        self.chat = []
        self.random_seed = randint(0, 30000)

    def register(self, name):
        """Register a new player on the server."""
        if self.registering and name not in self.players.keys():
            self.players[name] = None
            return self.random_seed
        else:
            return None

    def game_packets(self, name):
        """Create packets to distribute to the clients.
           Return (False, Player list, Messages) if in Lobby
           Return (True, Game infos) if in Game"""
        if self.registering:
            return (False, list(self.players.keys()), self.chat)
        else:
            if self.players[name] is not None:
                data_pack = self.players[name]
                del self.players[name]
                return (True, data_pack)
            else:
                return (True, None)

    def receive_info(self, actions):
        """Receiving information from everyone."""
        if self.registering:
            self.registering = False
        for key in self.players:
            self.players[key] = actions


class Server():

    """Dedicated server instance for **RTSTITLE**."""

    def __init__(self):
        self.game_data = GameData()
        self.view = ServerView(self.game_data)
        self.server_ui_loop()
        self.view.mainloop()

    def server_ui_loop(self):
        self.view.new_messages()
        self.view.after(40, self.server_ui_loop)

    def create_server(self):
        """Creates a new server instance."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        local_ip_address = s.getsockname()[0]
        self.deamon = Pyro4.Daemon(host=local_ip_address, port=47098)
        uri = self.deamon.register(self, "uri")
        self.deamon.requestLoop()

    def chat_message(self, name, message):
        self.game_data.append(str(name) + ": " + str(message))

    def event_loop(self):
        pass

    def register(self, name):
        return self.game_data.register(name)

    def game_packets(self, name):
        return self.game_data.game_packets(name)

    def receive_info(self, actions):
        return self.game_data.receive_info(actions)

    def client_quit(self, name):
        pass


if __name__ == '__main__':
    s = Server()
