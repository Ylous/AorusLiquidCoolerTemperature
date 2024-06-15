import time
import logging

from aorus_liquid_cooler import LiquidCooler, CoolingType, CoolingMode

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m.%d.%Y %H:%M:%S',
        level=logging.DEBUG,
    )

    liquid_cooler = LiquidCooler()
    
    liquid_cooler.set_cooling_mode(CoolingType.FANS, CoolingMode.CUSTOM)

    while True:
        liquid_cooler.send_cpu_temperature()
        time.sleep(2)
