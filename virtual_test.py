import time
import can
import asyncio

bus1 = can.interface.Bus('vcan0', interface='virtual')
bus2 = can.interface.Bus('vcan0', interface='virtual')
async def send_msg():
    msg = can.Message(arbitration_id=0x123, data = [0, 1, 2, 3, 4, 5, 6, 7], is_extended_id = False)

    try:
        while True:
            bus1.send(msg)
            print(f'sent {msg}')
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        pass

    bus1.shutdown()


async def read_msg():
    print('hi')
    try:
        while True:
            msg = bus2.recv()
            print(f'recieved {msg}')
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        pass

    bus2.shutdown()


async def main():
    await asyncio.gather(send_msg(), read_msg())
asyncio.run(main())