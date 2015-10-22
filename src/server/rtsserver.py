# -*- coding: utf-8 -*-
# rtsserver.py
# Main model for the server
# Author : Jean-Sébastien Beaulieu

import Pyro4
from random import randint
from threading import Timer
from servertools import ServerTools
from datetime import datetime


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
        self.create_server()

    def create_server(self):
        """Attempts to create a new server instance."""
        try:
            ip = ServerTools.get_local_ip()
            self.deamon = Pyro4.Daemon(host=ip, port=47089)
            self.uri = self.deamon.register(self, "uri")
            self.deamon.requestLoop()
        except:
            pass

    ############################################################################
    # Interaction between clients and game_data                                #
    ############################################################################
    def get_server_info(self):
        return self.uri

    def get_players(self):
        return self.game_data.players

    def empty_players(self):
        self.game_data.players = {}

    def get_new_chat(self):
        return self.game_data.chat

    def empty_new_chat(self):
        self.game_data.chat = []

    def chat_message(self, name, message):
        time_ms = datetime.now()
        chat_string = str(name) + ": " + str(message) + "\n"
        self.game_data.chat.append([time_ms, chat_string])

    def register(self, name):
        return self.game_data.register(name)

    def game_packets(self, name):
        return self.game_data.game_packets(name)

    def receive_info(self, actions):
        return self.game_data.receive_info(actions)

    def client_quit(self, name):
        del self.game_data.players[name]

    ############################################################################
    # Shutting down the server                                                 #
    ############################################################################
    def shutdown(self):
        self.deamon.shutdown()


if __name__ == '__main__':
    s = Server()
