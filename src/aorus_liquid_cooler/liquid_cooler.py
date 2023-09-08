import logging

import psutil
import usb.core
import usb.util

from packets import create_temperature_set_payload


class LiquidCooler:
    def __init__(self, product_id: int = 0x7A46, vendor_id: int = 0x1044, default_interface: int = 1):
        device = usb.core.find(idVendor=vendor_id,
                               idProduct=product_id)

        if not device:
            raise OSError("HID device not found")
        else:
            logging.debug(f"found device. Bus: {device.bus} | Address: {device.address}")

        if device.is_kernel_driver_active(default_interface):
            device.detach_kernel_device(default_interface)
            usb.util.claim_interface(device, default_interface)
            logging.debug(f"claimed interface: {default_interface}.")

        self.dev = device

    def send_cpu_temperature(self, temperature: int = None):
        cpu_temp = temperature or int(psutil.sensors_temperatures()['coretemp'][0].current)
        payload = create_temperature_set_payload(cpu_temp)

        response = self.dev.ctrl_transfer(0x21, 0x09, 0x0300, 1, payload)
        logging.debug(f"Temperature: {cpu_temp} Response: {response}")
