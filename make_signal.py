import can
import time

bus = can.interface.Bus(bustype='virtual', channel = 'vcan0', bitrate = 50000)

msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)

try:
    while True:
        bus.send(msg)
        print(f"Sent message: {msg}")
        time.sleep(1)  # Adjust the delay as needed
except KeyboardInterrupt:
    pass

bus.shutdown()
