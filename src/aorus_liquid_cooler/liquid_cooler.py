import logging

import psutil
import usb.core
import usb.util

from .enums import CoolingType, CoolingMode
from .packets import create_temperature_set_payload, create_cooling_mode_payload


class LiquidCooler:
    def __init__(self, vendor_id: int = 0x1044, product_id: int = 0x7A46, default_interface: int = 1):
        """
        Creates a liquid cooler device instance by given PID, VID
        Args:
            vendor_id: USB HID VID
            product_id: USB HID PID
            default_interface: Interface for kernel device API
        """
        device = usb.core.find(idVendor=vendor_id,
                               idProduct=product_id)

        if not device:
            raise OSError("HID device not found")
        else:
            logging.debug(f"found device. Bus: {device.bus} | Address: {device.address}")

        if device.is_kernel_driver_active(default_interface):
            device.detach_kernel_driver(default_interface)
            usb.util.claim_interface(device, default_interface)
            logging.debug(f"claimed interface: {default_interface}")

        self.dev = device

    def send_cpu_temperature(self, temperature: int = None) -> None:
        """
        Send temperature to device
        Args:
            temperature: Temperature to send, by default 1st CPU temperature sensor (Optional)

        Returns: None

        """
        cpu_temp = temperature or int(psutil.sensors_temperatures()['coretemp'][0].current)
        payload = create_temperature_set_payload(cpu_temp)

        response = self.dev.ctrl_transfer(0x21, 0x09, 0x0300, 1, payload)
        logging.debug(f"Temperature: {cpu_temp} Response: {response}")

    def set_cooling_mode(self, cooling_type: CoolingType = CoolingType.FANS, cooling_mode: CoolingMode = CoolingMode.MAX) -> None:
        """
        Set cooling mode for pump or fans
        Args:
            cooling_type: Available types: Fans, Pump (Optional)
            cooling_mode: Available modes: Zero, Balance, Performance, Quiet, Max, Default, Custom (Optional)

        Returns: None

        """
        payload = create_cooling_mode_payload(cooling_type, cooling_mode)

        response = self.dev.ctrl_transfer(0x21, 0x09, 0x0300, 1, payload)
        logging.debug(f"Type: {cooling_type} Mode: {cooling_mode} Response: {response}")
