import socket

def create_response():
    content = b"<html><body><h1>Ol\xc3\xa1 Milene</h1></body></html>"
    response = b"HTTP/1.1 200 OK\r\n"
    response += b"Content-Type: text/html; charset=utf-8\r\n"
    response += b"Content-Length: " + str(len(content)).encode() + b"\r\n"
    response += b"\r\n"
    response += content
    return response

def start_server():
    host = 'localhost'
    port = 8002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established from {addr}")

        request = client_socket.recv(1024).decode()
        print(f"Received request:\n{request}")

        response = create_response()

        client_socket.sendall(response)
        client_socket.close()

if __name__ == '__main__':
    start_server()
