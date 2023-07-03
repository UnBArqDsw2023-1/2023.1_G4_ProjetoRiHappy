import socket
import threading


HOST = '127.0.0.1'  
PORT = 8000  


def handle_client(client_socket, client_address):
    while True:
    
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print(f"Mensagem recebida do cliente {client_address[0]}:{client_address[1]}: {data}")

    
        response = "Resposta do servidor"
        client_socket.send(response.encode())

    
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((HOST, PORT))


server_socket.listen()

print(f"Servidor TCP/IP escutando em {HOST}:{PORT}")

while True:
    
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address[0]}:{client_address[1]}")

    
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
