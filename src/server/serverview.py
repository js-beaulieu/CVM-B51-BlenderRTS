# -*- coding: utf-8 -*-
# serverview.py
# View for rtsserver module
# Author : Jean-Sébastien Beaulieu

import tkinter as tk
from tkinter import ttk

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 350


class ServerView(tk.Tk):

    """Main window for **RTSTITLE** standalone dedicated server."""

    def __init__(self, model):
        tk.Tk.__init__(self)
        self.model = model

        self.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.title("**RTSTITLE** - Dedicated Multiplayer Server manager")
        self.main_window()

    def main_window(self):
        """Create the main window elements."""
        # infos and controls
        self.frame_infos = tk.Frame(self, width=WINDOW_WIDTH/4,
                                    height=WINDOW_HEIGHT, padx=15, pady=15)
        self.frame_infos.pack(side=tk.LEFT, fill=tk.BOTH)
        label_infos = tk.Label(self.frame_infos, text="Server Controls")
        label_infos.pack(pady=5, anchor=tk.CENTER)
        button_create = tk.Button(self.frame_infos, text="Start", padx=10)
        button_create.bind("<Button-1>", self.event_button_create)
        button_create.pack(pady=5)
        button_stop = tk.Button(self.frame_infos, text="Stop", padx=10)
        button_stop.bind("<Button-1>", self.event_button_stop)
        button_stop.pack(pady=5)

        # players list
        self.frame_players = tk.Frame(self, width=WINDOW_WIDTH/4,
                                      height=WINDOW_HEIGHT, padx=15, pady=15)
        self.frame_players.pack(side=tk.LEFT, fill=tk.BOTH)
        label_players = tk.Label(self.frame_players, text="Joueurs connectés")
        label_players.pack(pady=5, anchor=tk.CENTER)
        for k in self.model.players:
            player = tk.Label(self.frame_players, text=k)
            player.pack(side=tk.TOP, anchor=tk.W)

        # server chat
        self.frame_chat = tk.Frame(self, height=WINDOW_HEIGHT,
                                   width=WINDOW_WIDTH/2, padx=15, pady=15)
        self.frame_chat.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        label_chat = tk.Label(self.frame_chat, text="Chat")
        label_chat.pack(pady=5, anchor=tk.CENTER)

    # Binds handling
    def event_button_create(self, event):
        pass

    def event_button_stop(self, event):
        pass
