import time

from src.main import LiquidCooler

if __name__ == "__main__":
    liquid_cooler = LiquidCooler()

    while True:
        liquid_cooler.send_cpu_temperature()
        time.sleep(2)
