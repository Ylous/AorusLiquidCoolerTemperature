import logging

import psutil
import usb.core
import usb.util

from src.utils import convert_temperature_to_bytes_array

product_id = 0x7a46
vendor_id = 0x1044
default_interface = 1


class LiquidCooler:
    def __init__(self):
        device = usb.core.find(idVendor=vendor_id,
                               idProduct=product_id)

        if not device:
            raise Exception("Device not found!")
        else:
            logging.info(f"Found device. Bus: {device.bus} | Address: {device.address}")

        if device.is_kernel_driver_active(default_interface):
            device.detach_kernel_device(default_interface)
            usb.util.claim_interface(device, default_interface)
            logging.info(f"Claimed interface: {default_interface}.")

        self.dev = device

    def send_cpu_temperature(self):
        cpu_temp = int(psutil.sensors_temperatures()['coretemp'][0].current)
        data_fragment = convert_temperature_to_bytes_array(cpu_temp)

        response = self.dev.ctrl_transfer(0x21, 0x09, 0x0300, 1, bytes.fromhex(data_fragment))
        logging.info(f"Data sent. Temperature: {cpu_temp} Hex: {data_fragment} Response: {response}")
