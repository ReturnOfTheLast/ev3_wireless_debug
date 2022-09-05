# Made by Marcus Kolbe
# Github: https://github.com/ReturnOfTheLast/ev3_wireless_debug

import socket
import argparse
from datetime import datetime
import logging
import sys
from time import sleep

# Setup logging file
logging.basicConfig(filename=f"{datetime.now().strftime('%d%m%y-%H%M%S')}.log", encoding="UTF-8", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

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
logging.debug(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] Listening on ({HOST}, {PORT})")

# Accept connection
conn, addr = sock.accept()
logging.debug(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] {addr} has connected")

# Main loop
while True:
    try:
        # Receive data and print it
        data = conn.recv(1024)
        if not data:
            logging.debug(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] {addr} has disconnected")
            break
        conn.send(bytes("Message Received", "UTF-8"))
        logging.debug(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] {addr}> {data.decode('UTF-8')}")
    except KeyboardInterrupt:
        logging.debug(f"[ {datetime.now().strftime('%d/%m-%y %H:%M:%S:%f')} ] CTRL-C is pressed, closing server")
        break

conn.close()