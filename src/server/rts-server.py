# -*- coding: utf-8 -*-
# rts-server.py
# Modèle principal pour le serveur
# Auteur : Jean-Sébastien Beaulieu

import Pyro4
from random import randint
import socket


class GameData():

    def __init__(self):
        self.registering = True
        self.players = {}
        self.random_seed = randint(0, 30000)

    def register(self, name):
        """Ajouter un nouveau joueur à la partie."""
        if self.registering and name not in self.players.keys():
            self.players.update(name=None)
            return self.random_seed
        else:
            return None

    def game_packets(self, name):
        """Crée les paquets à distribuer aux clients.
           Return (True, Player list) si Lobby
           Return (False, Informations) si partie"""
        if self.registering:
            return (False, list(self.players.keys()))
        else:
            if self.players[name] is not None:
                data_pack = self.players[name]
                del self.players[name]
                return (True, data_pack)
            else:
                return (True, None)

    def receive_info(self, actions):
        """Receiving information from everyone and """
        if self.registering:
            self.registering = False
        for key in self.players:
            self.players(key=actions)


class Server():

    def __init__(self):
        self.game_data = GameData()

    def create_server(self):
        """Creates a new server instance."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        local_ip_address = s.getsockname()[0]
        self.deamon = Pyro4.Daemon(host=local_ip_address, port=47098)
        uri = self.deamon.register(self, "uri")
        self.deamon.requestLoop()

    def 


if __name__ == '__main__':
    s = Server()
