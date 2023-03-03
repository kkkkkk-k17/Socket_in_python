import socket

# Crearea unui obiect de tip socket pentru server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Atribuirea unui port la server
server_port = 12345

# Legarea server-ului la adresa IP și portul ales
server_socket.bind(('127.0.0.1', server_port))

# Ascultarea conexiunilor de la clienți
server_socket.listen()

print(f"Serverul asculta la portul {server_port}")

# Crearea unei liste de clienți conectați
client_list = []

while True:
    # Acceptarea conexiunii de la un client
    client_socket, client_address = server_socket.accept()

    # Adăugarea clientului la lista de clienți
    client_list.append(client_socket)

    print(f"Clientul {client_address} s-a conectat.")

    while True:
        # Primirea mesajului de la client
        message = client_socket.recv(1024).decode()

        # Verificarea dacă mesajul este gol (clientul a închis conexiunea)
        if not message:
            # Eliminarea clientului din lista de clienți
            client_list.remove(client_socket)
            print(f"Clientul {client_address} s-a deconectat.")
            break

        print(f"Mesaj primit de la {client_address}: {message}")

        # Retransmiterea mesajului la toți clienții conectați
        for client in client_list:
            client.send(message.encode())
