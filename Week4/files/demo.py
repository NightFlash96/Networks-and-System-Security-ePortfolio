# mock_sample.py
# This file is intentionally insecure for scanner testing purposes only

import os
import base64
import socket

def unsafe_eval(user_input):
    # Suspicious: eval
    eval(user_input)

def unsafe_exec(code):
    # Suspicious: exec
    exec(code)

def decode_payload(data):
    # Suspicious: base64 decode
    return base64.b64decode(data)

def connect_remote():
    # Suspicious: socket.connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 4444))

if __name__ == "__main__":
    unsafe_eval("2 + 2")
