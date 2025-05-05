from socket import *
import socket
import threading
import logging
from datetime import datetime

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        try:
            while True:
                data = b''
                while not data.endswith(b'\r\n'):
                    part = self.connection.recv(1)
                    if not part:
                        break
                    data += part

                if not data:
                    break

                text = data.decode('utf-8').strip()
                logging.warning(f"Received from {self.address}: {text}")

                if text == 'TIME':
                    now = datetime.now()
                    time_string = now.strftime("%H:%M:%S")
                    response = f"JAM {time_string}\r\n"
                    self.connection.sendall(response.encode('utf-8'))
                elif text == 'QUIT':
                    logging.warning(f"Connection closed by client: {self.address}")
                    break
                else:
                    self.connection.sendall(b"Invalid command\r\n")
        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 45000))
        self.my_socket.listen(1)
        logging.warning(f"Server is listening on port 45000")
        while True:
            connection, client_address = self.my_socket.accept()
            logging.warning(f"Connection from {client_address}")

            clt = ProcessTheClient(connection, client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format='%(message)s')
    main()
