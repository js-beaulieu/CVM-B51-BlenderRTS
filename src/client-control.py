# -*- coding: utf-8 -*-
# client-control.py
# Main client controller
# Author : Jean-Sébastien Beaulieu

from server import servertools as st


class Client():

    """Main client class, to initialize connection with the server
       and share informations with other players."""

    def __init__(self):
        self.ip = st.ServerTools.get_local_ip()

if __name__ == '__main__':
    client = Client()
