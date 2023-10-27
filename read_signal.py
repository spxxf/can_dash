import can

bus = can.interface.Bus(bustype='virtual', channel='vcan0', bitrate=500000)

try:
    while True:
        print('he')


        msg = bus.recv()
        print(f"Received message: {msg}")
except KeyboardInterrupt:
    pass

bus.shutdown()

