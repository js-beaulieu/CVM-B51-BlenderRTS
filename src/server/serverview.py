# -*- coding: utf-8 -*-
# serverview.py
# View for rtsserver module
# Author : Jean-Sébastien Beaulieu

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class ServerView(tk.Tk):

    """Main window for **RTSTITLE** standalone dedicated server."""

    def __init__(self, server, ns):
        tk.Tk.__init__(self)
        self.server = server
        self.ns = ns
        self.main_window()
        self.resizable(width=False, height=False)
        self.title("**RTSTITLE** - Dedicated Multiplayer Server manager")
        self.protocol("WM_DELETE_WINDOW", self.shutdown)

        self.chat_history = []  # to keep in memory messages already shown
        self.connected_players = []
        self.server_event("SERVEUR DÉMARRÉ")
        self.server_event("Informations de connexion :")
        self.server_event(str(self.server.get_server_info()))
        # self.server_event(str(self.server.ping()))

    ############################################################################
    # Main window                                                              #
    ############################################################################
    def main_window(self):
        """Create the main window elements."""
        # players list + chat
        self.frame_players = tk.Frame(self, width=350, padx=15, pady=15)
        self.frame_players.pack(side=tk.LEFT, fill=tk.Y)
        self.chatbox = self.pop_chatbox()
        self.chatbox.pack(fill=tk.BOTH, expand=1)
        self.pop_chat_controls = self.pop_chat_controls()
        self.pop_chat_controls.pack(fill=tk.X, expand=1)
        self.playerlist_frame = self.pop_playerlist_frame()
        self.playerlist_frame.pack_propagate(False)
        self.playerlist_frame.pack(fill=tk.BOTH)
        self.pop_player_list()

        # server log
        self.frame_log = tk.Frame(self, padx=15, pady=15, width=400)
        self.frame_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        log = self.pop_server_events()
        log.pack(fill=tk.BOTH)

    def pop_playerlist_frame(self):
        """Returns a tkinter frame containing the playerlist."""
        frame = tk.Frame(self.frame_players, height=100)
        return frame

    def pop_player_list(self):
        for widget in self.playerlist_frame.winfo_children():
            widget.destroy()
        tk.Label(self.playerlist_frame, text="Joueurs connectés").pack(
                                                        pady=5, anchor=tk.CENTER)
        try:
            for name in self.connected_players:
                tk.Label(self.playerlist_frame, text=name).pack(pady=5,
                                                                anchor=tk.LEFT)
        except:
            pass

    def pop_chatbox(self):
        """Returns a tkinter frame containing the chat box."""
        frame = tk.Frame(self.frame_players)
        label_chat = tk.Label(frame, text="Messages - ADMIN")
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
    def connection_error(self):
        messagebox.showerror("Erreur de connexion!",
                             "Malheureusement, le serveur n'a pas pu démarrer." +
                             "Le gestionnaire va maintenant fermer.")
        self.quit()

    def shutdown(self):
        if messagebox.askyesno("Arrêter le serveur?",
                               "Voulez-vous fermer le serveur?\n" +
                               " Ceci éjecte les joueurs connectés."):
            self.server.shutdown()
            self.quit()

    def event_button_chat(self, event):
        if self.chat_entry.get():
            self.server.chat_message("ADMIN", self.chat_entry.get())
            self.chat_entry.delete(0, tk.END)

    ############################################################################
    # Update UI                                                                #
    ############################################################################
    def new_messages(self):
        """Updates the chatbox with the messages since the last query."""
        if self.server.get_new_chat() is not None:
            for i in self.server.get_new_chat():
                if i not in self.chat_history:
                    self.chat_history.append(i)
                    self.chatbg.config(state=tk.NORMAL)
                    self.chatbg.insert(tk.END, i[1])
                    self.chatbg.config(state=tk.DISABLED)
                    self.chatbg.see(tk.END)

    def new_user(self):
        for name in self.server.get_players():
            if name not in self.connected_players:
                self.connected_players.append(name)
<<<<<<< Updated upstream
                tk.Label(self.playerlist_frame, text=name).pack(anchor=tk.W)
                self.server_event(name + " s'est connecté.")
=======
        for name in self.connected_players:
            if name not in self.server.get_players():
                self.connected_players.remove(name)
        self.pop_player_list()
>>>>>>> Stashed changes

    def server_event(self, event):
        """Creates a new entry in the server log."""
        self.log.config(state=tk.NORMAL)
        time = str(datetime.now().time())
        self.log.insert(tk.END, time.split(".")[0] + " - " + event + "\n")
        self.log.config(state=tk.DISABLED)
        self.log.see(tk.END)
