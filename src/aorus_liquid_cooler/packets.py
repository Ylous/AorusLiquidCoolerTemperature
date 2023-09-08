def create_temperature_set_payload(temperature: int) -> bytes:
    assert temperature > 0
    assert temperature < 256

    return bytes([0xE0, 0x00, temperature, 0x14, 0x02, 0x05, 0x0A, 0x00])
