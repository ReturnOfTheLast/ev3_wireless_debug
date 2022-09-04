# Made by Marcus Kolbe
# Github: https://github.com/ReturnOfTheLast/ev3_wireless_debug

import socket
import argparse
from datetime import datetime

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="", action="store", dest="host", required=False)
parser.add_argument("--port", type=int, default=1337, action="store", dest="port", required=False)
args = parser.parse_args()

# Set host and port from arguments
HOST = args.host # Default: ""
PORT = args.port # Default: 1337

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket and listen
sock.bind((HOST, PORT))
sock.listen(1)
print(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] Listening on ({HOST}, {PORT})")

# Accept connection
conn, addr = sock.accept()
print(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] {addr} has connected")

# Main loop
while True:
    try:
        # Receive data and print it
        data = conn.recv(1024)
        if not data:
            print(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] {addr} has disconnected")
            break
        conn.send(bytes("Message Received", "UTF-8"))
        print(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] {addr}> {data.decode('UTF-8')}")
    except KeyboardInterrupt:
        print(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] CTRL-C is pressed, closing server")
        break

conn.close()