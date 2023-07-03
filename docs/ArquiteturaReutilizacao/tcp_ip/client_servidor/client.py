import socket


HOST = '127.0.0.1'  
PORT = 8000 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((HOST, PORT))
print(f"Conectado ao servidor em {HOST}:{PORT}")

while True:
    
    message = input("Digite uma mensagem para o servidor: ")
    client_socket.send(message.encode())
    
    
    response = client_socket.recv(1024).decode()
    print(f"Resposta do servidor: {response}")
    
    
    if message.lower() == 'exit':
        break


client_socket.close()
