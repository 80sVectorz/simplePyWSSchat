import asyncio
import websockets
import pickle
import copy

log = []



async def chat(websocket, path):
    global log
    async for msg in websocket:
        if msg == "{g}":
            if len(log) == 0:
                print("log empty...")
                await websocket.send("{NONE}")
            else:
                await websocket.send(pickle.dumps(copy.deepcopy(log)))
                return
        elif msg != "{g}":
            print(msg)
            log.append(msg)
            await websocket.send(msg)

start_server = websockets.serve(chat, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
