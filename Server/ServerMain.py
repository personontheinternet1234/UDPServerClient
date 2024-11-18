from Server import ThreadedServer

if __name__ == "__main__":
    server_addr = "192.168.1.15"
    port = 5559

    groundControlServer = ThreadedServer(server_addr, port)
