# -*- coding: utf-8 -*-
# serverview.py
# View for rtsserver module
# Author : Jean-Sébastien Beaulieu

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ServerView(tk.Tk):

    """Main window for **RTSTITLE** standalone dedicated server."""

    def __init__(self, server):
        tk.Tk.__init__(self)
        self.server = server
        self.main_window()
        self.resizable(width=False, height=False)
        self.title("**RTSTITLE** - Dedicated Multiplayer Server manager")
        self.protocol("WM_DELETE_WINDOW", self.button_stop.invoke())

    ############################################################################
    # Main window                                                              #
    ############################################################################
    def main_window(self):
        """Create the main window elements."""
        # infos and controls
        self.frame_infos = tk.Frame(self, width=150, padx=15, pady=15)
        self.frame_infos.pack(side=tk.LEFT, fill=tk.Y)
        label_infos = tk.Label(self.frame_infos, text="Contrôle serveur")
        label_infos.pack(pady=5, anchor=tk.CENTER)
        button_create = tk.Button(self.frame_infos, text="Start", padx=10)
        button_create.bind("<Button-1>", self.event_button_create)
        button_create.pack(pady=5)
        self.button_stop = tk.Button(self.frame_infos, text="Stop", padx=10)
        self.button_stop.bind("<Button-1>", self.event_button_stop)
        self.button_stop.pack(pady=5)
        ttk.Separator(self.frame_infos).pack(fill=tk.X, pady=20)

        # players list + chat
        self.frame_players = tk.Frame(self, width=400, padx=15, pady=15)
        self.frame_players.pack(side=tk.LEFT, fill=tk.Y)
        self.playerlist_frame = self.pop_playerlist_frame()
        self.playerlist_frame.pack(fill=tk.BOTH)
        self.chatbox = self.pop_chatbox()
        self.chatbox.pack(fill=tk.BOTH, expand=1)
        self.pop_chat_controls = self.pop_chat_controls()
        self.pop_chat_controls.pack(fill=tk.X, expand=1)

        # server log
        self.frame_log = tk.Frame(self, padx=15, pady=15, width=400)
        self.frame_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        log = self.pop_server_events()
        log.pack(fill=tk.BOTH)
        self.log.insert(tk.END, str(datetime.now().time()) + "SERVER STARTED")

    def pop_playerlist_frame(self):
        """Returns a tkinter frame containing the playerlist."""
        frame = tk.Frame(self.frame_players, height=100)
        label_players = tk.Label(self.frame_players, text="Joueurs connectés")
        label_players.pack(pady=5, anchor=tk.CENTER)
        for k in self.server.game_data.players:
            player = tk.Label(frame, text=k)
            player.pack(anchor=tk.W)
        return frame

    def pop_chatbox(self):
        """Returns a tkinter frame containing the chat box."""
        frame = tk.Frame(self.frame_players)
        label_chat = tk.Label(frame, text="Chat")
        label_chat.pack(pady=5, anchor=tk.CENTER)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chatbg = tk.Text(frame, yscrollcommand=scrollbar.set,
                              padx=5, pady=5, height=20, width=40,
                              state=tk.DISABLED, font=("Consolas", 10))
        self.chatbg.pack()
        return frame

    def pop_chat_controls(self):
        """Returns a tkinter frame containing the chat controls."""
        frame = tk.Frame(self.frame_players)
        self.chat_entry = tk.Entry(frame, width=42)
        self.chat_entry.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W)
        self.chat_entry.bind("<Return>", self.event_button_chat)
        button = tk.Button(frame, text="Envoyer")
        button.bind("<Button-1>", self.event_button_chat)
        button.pack(side=tk.LEFT)
        return frame

    def pop_server_events(self):
        """Returns a tkinter frame containing the server event log."""
        frame = tk.Frame(self.frame_log)
        label_chat = tk.Label(frame, text="Évènements")
        label_chat.pack(pady=5, anchor=tk.CENTER)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log = tk.Text(frame, yscrollcommand=scrollbar.set,
                           state=tk.DISABLED, padx=5, pady=5, height=30,
                           width=50, font=("Consolas", 10))
        self.log.pack(fill=tk.BOTH)
        return frame

    ############################################################################
    # Buttons and binds                                                        #
    ############################################################################
    def event_button_create(self, event):
        self.server.create_server()

    def event_button_stop(self, event):
        if messagebox.askyesno("Arrêter le serveur?", "Ceci éjecte les joueurs connectés."):
            self.server.shutdown()

    def event_button_chat(self, event):
        if self.chat_entry.get():
            self.server.game_data.chat.append("ADMIN: " + self.chat_entry.get() + "\n")
            self.chat_entry.delete(0, tk.END)

    ############################################################################
    # Update UI                                                                #
    ############################################################################
    def new_messages(self):
        """Updates the chatbox with the messages since the last query."""
        for i in self.server.game_data.chat:
            self.chatbg.config(state=tk.NORMAL)
            self.chatbg.insert(tk.END, i)
            self.chatbg.config(state=tk.DISABLED)
            self.chatbg.see(tk.END)
        self.server.game_data.chat = []

    def server_event(self, event):
        """Creates a new entry in the server log."""
        self.log.config(state=tk.NORMAL)
        time = str(datetime.now().time())
        self.log.insert(tk.END, time.split(".")[0] + " - " + event + "\n")
        self.log.config(state=tk.DISABLED)
        self.log.see(tk.END)
