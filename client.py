import socket

def start_client():
    # Creăm un socket de tip TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Setăm adresa și portul serverului la care ne vom conecta
    server_address = ('localhost', 1234)

    # Ne conectăm la server
    client_socket.connect(server_address)

    while True:
        # Cerem utilizatorului să introducă un mesaj
        message = input("Scrie un mesaj: ")

        # Trimitem mesajul la server
        client_socket.sendall(message.encode('utf-8'))

        # Așteptăm să primim un răspuns de la server și afișăm mesajul primit
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

start_client()
