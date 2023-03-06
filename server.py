import socket
import threading

def handle_client(client_socket, client_addr, clients):
    print(f"[NEW CONNECTION] {client_addr} conectat.")

    while True:
        try:
            # Așteptăm primirea unui mesaj de la client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{client_addr}] {message}")
                # Iterăm prin toți clienții conectați și le trimitem mesajul
                for client in clients:
                    if client != client_socket:
                        client.sendall(message.encode('utf-8'))
            else:
                # Dacă nu am primit niciun mesaj de la client, înseamnă că s-a întrerupt conexiunea
                print(f"[DISCONNECT] {client_addr} sa deconectat.")
                client_socket.close()
                clients.remove(client_socket)
                break

        except ConnectionResetError:
            print(f"[DISCONNECT] {client_addr} sa deconenctat.")
            client_socket.close()
            clients.remove(client_socket)
            break

def start_server():
    # Creăm un socket de tip TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ne asigurăm că putem refolosi adresa și portul serverului în cazul în care îl oprim și apoi îl pornim din nou
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Setăm adresa și portul pe care va fi disponibil serverul
    server_address = ('localhost', 1234)
    server_socket.bind(server_address)

    # Ascultăm conexiuni
    server_socket.listen()

    print(f"[LISTENING] Serverul asculta pe portul {server_address}")

    # Lista în care vom ține toți clienții conectați
    clients = []

    while True:
        # Acceptăm conexiunea unui client
        client_socket, client_address = server_socket.accept()

        # Adăugăm clientul la lista de clienți conectați
        clients.append(client_socket)

        # Începem un fir de execuție separat pentru a gestiona comunicarea cu acest client
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
        thread.start()

start_server()
