import asyncio
import datetime
import random
import websockets
import psutil





async def show_time(websocket):
    while websocket.open:
        temp = psutil.sensors_temperatures()
        temp2 = temp.get("cpu_thermal")
        tempstr = str(temp2[0])
        str_pos = tempstr.find("current")
        temp_pos = str_pos+len("current=")
        tempCPU=(tempstr[temp_pos]+tempstr[temp_pos+1]+","+tempstr[temp_pos+3]+tempstr[temp_pos+4])
        print(tempCPU)
        
        await websocket.send(tempCPU)
        await asyncio.sleep(2)

async def main():
    async with websockets.serve(show_time, "localhost", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())