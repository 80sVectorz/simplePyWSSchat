import asyncio
import websockets
import pickle
import copy

log = ["[john] hello"]



async def chat(websocket, path):
    msg = await websocket.recv()
    if msg == "{g}":
        print("fetching and sending...")
        if len(log) == 0:
            print("log empty...")
            await websocket.send("{NONE}")
        else:
            await websocket.send(pickle.dumps(copy.deepcopy(log)))
            return
    else:
        print(msg)
        log.append(msg)
        await websocket.send(msg)

start_server = websockets.serve(chat, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
