# -*- coding: utf-8 -*-
# servertools.py
# General tools that might be needed by the different server components
# Author : Jean-Sébastien Beaulieu

from tkinter import messagebox
import socket


class ServerTools():

    @staticmethod
    def erbox(title, text):
        """Static method that creates a messagebox."""
        messagebox.showerror(title, text)

    @staticmethod
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        return s.getsockname()[0]
