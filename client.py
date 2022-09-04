# Made by Marcus Kolbe
# Github: https://github.com/ReturnOfTheLast/ev3_wireless_debug

import socket

# Set host and port
HOST = "127.0.0.1"
PORT = 1337

# Set maximum reconnect attempts
max_reconnect_attempts = 3

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
sock.connect((HOST, PORT))

# Keep track of connection status
connected = True
print(f"Connected to ({HOST}, {PORT})")

# Send message function
def send_debug_message(m: str) -> None:
    global sock
    message_sent = False
    reconnect_attempts = 0
    while not message_sent and reconnect_attempts < max_reconnect_attempts:
        try:
            sock.send(bytes(m, "UTF-8"))
            print(f"{m}")
            confirmation = sock.recv(1024)
            if not confirmation:
                raise socket.error
            print(f"{confirmation.decode('UTF-8')}")
            message_sent = True
        except socket.error:
            connected = False
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"Lost connection... reconnecting")
            while not connected and reconnect_attempts < max_reconnect_attempts:
                try:
                    sock.connect((HOST, PORT))
                    connected = True
                    print(f"Reconnected to ({HOST}, {PORT})")
                except socket.error:
                    reconnect_attempts += 1

# <your code goes here>

sock.close()