from Client import Connection

if __name__ == "__main__":
    server_ip = "192.168.1.15"
    plane_ip = "192.168.1.7"
    port = 5559

    planeReceiver = PlaneReceiver(server_ip, plane_ip, port)
    planeReceiver.start_threads()
