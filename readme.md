# Aorus Liquid Cooler Temperature

This software is for people like me who have a AORUS Liquid Cooler series water coolant system on Linux hardware. The program
is very simple, it just sends the CPU temperature to the water block by USB interface.

### Getting started

```python
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
    
    liquid_cooler.set_cooling_mode(CoolingType.FANS, CoolingMode.MAX)

    while True:
        liquid_cooler.send_cpu_temperature()
        time.sleep(2)

```

### Systemctl
For your convenience, I have provided a configuration file for creating the service.
```ini
[Unit]
Description=aorus
After=network.target

[Service]
Type=simple
User=root

WorkingDirectory=/home/ylous/AorusLiquidCoolerTemperature
ExecStart=sudo python3 main.py
Restart=always
RestartSec=5

[Install]
WantedBy=network.target 
```


### TODO
- [X] Temperature synchronization.
- [X] Setting the pump or fans.
- [ ] Processor name and other stuff synchronization.

> #### Notes:
> Tested on Aorus Liquid Cooler 240. \
> This snippet works only on Linux!
