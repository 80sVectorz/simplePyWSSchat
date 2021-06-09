import threading
import asyncio
import websockets
import os, time, pickle ,sys


log = []
name = input("Whats your name: ")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def display():
    cls()
    i = 1
    for m in log:
        sys.stdout.write("\n")
        sys.stdout.write(f"\r{m}")
        sys.stdout.flush()
        i+=1
    sys.stdout.write("\n Send message: ")
    sys.stdout.flush()

async def recieveLog():
    global log
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        request = "{g}"
        await websocket.send(request)
        recv = await websocket.recv()
        if recv != "{NONE}" and pickle.loads(recv)!= log:
            log = pickle.loads(recv)
            cls()
            display()


async def sendMessage(): 
    uri = "ws://localhost:8765"
    while True :
        msg = "["+name+"] "+input("")
        async with websockets.connect(uri) as websocket:
            await websocket.send(msg)
        display()

async def main():
    threadInputLoop = threading.Thread(target=mainInput, args=())
    threadInputLoop.start()
    while True:
        await recieveLog()


async def ping(w):
    await w.send("{ping}")

def mainPing(websocket):
    while True:
        loop.run_until_complete(ping(websocket))
        loop.close()

    
def mainInput():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(sendMessage())
    loop.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())







