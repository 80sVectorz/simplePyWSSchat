import asyncio
import websockets
import os, time, pickle

import struct

def convert_string_to_bytes(string):
    bytes = b''
    for i in string:
        bytes += struct.pack("B", ord(i))
    return bytes

log = []
name = input("Whats your name: ")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def display():
    for m in log:
        print(f"{m}")

async def chat():
    global log
    cls()
    display()
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        request = "{g}"
        await websocket.send(request)
        recv = await websocket.recv()
        if recv != "{NONE}":
            log = pickle.loads(recv)
    async with websockets.connect(uri) as websocket:
        msg = "["+name+"] "+input("Message: ")
        await websocket.send(msg)

async def main():
    while True:
        await chat()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
