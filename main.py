import time
import logging

from src.main import LiquidCooler

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m.%d.%Y %H:%M:%S',
        level=logging.INFO,
    )

    liquid_cooler = LiquidCooler()

    while True:
        liquid_cooler.send_cpu_temperature()
        time.sleep(2)
