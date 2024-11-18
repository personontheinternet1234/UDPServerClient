from Client import ClientConnection

if __name__ == "__main__":
    server_addr = "192.168.1.15"
    client_addr = "192.168.1.7"
    port = 5559

    connection = ClientConnection(server_addr, client_addr, port)
    connection.start_threads()
