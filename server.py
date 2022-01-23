import asyncio
import datetime
import random
import websockets

async def show_time(websocket):
    while websocket.open:
        await websocket.send("teplota je 30 C a vlhkost 25%")
        await asyncio.sleep(2)

async def main():
    async with websockets.serve(show_time, "localhost", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())