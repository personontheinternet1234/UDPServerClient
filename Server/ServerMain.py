from Server import ThreadedServer

if __name__ == "__main__":
    host_addr = "192.168.1.15"
    client_addr = "192.168.1.7"

    groundControlServer = ThreadedServer(host_addr, 5559)
