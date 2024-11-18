#!/usr/bin/env python

# Author: Isaac Verbrugge - isaacverbrugge@gmail.com
# Since: November 11, 2024
# Project: UDPServerClient
# Purpose: Client

import socket
import threading
import json
import os
import sys
from time import sleep


class ClientConnection:

    def __init__(self, server_addr, client_addr, port):
        self.server_addr = server_addr
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind(('', self.port))
        self.client_addr = client_addr

        self.server_response = False
        self.connected_to_server = False

        self.rate = 2

        self.connect()

    def start_threads(self):
        threading.Thread(target=self.listen).start()
        threading.Thread(target=self.server_check).start()

    def server_check(self):
        while True:
            sleep(0.001)

            self.client_socket.sendto(("{\"server_check\": \"challenge\"}").encode("UTF-8"),
                                      (self.server_addr, self.port))
            self.server_response = False
            sleep(10)
            if self.server_response == False:
                print("[Client] No response from server - disconnected")
                self.connected_to_server = False
                self.connect()

    def connect(self):
        try:
            self.client_socket.sendto(("{\"connected\": \"" + self.client_addr + "\"}").encode("UTF-8"),
                                      (self.server_addr, self.port))
            print("[Client] Binded To Socket")
        except (ConnectionRefusedError, OSError) as e:
            print("[Client] Not Connected")
            return False
        return True

    def listen(self):
        while True:
            sleep(0.001)

            try:
                data, _ = self.client_socket.recvfrom(4096)

                # if "check" not in str(data):
                print("[Client] received: " + str(data))

                packet = json.loads(data)

                if (packet.get("client_check")):
                    self.client_socket.sendto(("{\"client_check\": \"received\"}").encode("UTF-8"),
                                              (self.server_addr, self.port))
                if (packet.get("server_check")):
                    self.server_response = True

                if (packet.get("test")):
                  print("test received")

            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    server_addr = "192.168.1.15"
    client_addr = "192.168.1.7"
    Client = Client(server_addr, client_addr, 5559)
    Client.start_threads()
