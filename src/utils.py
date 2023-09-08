def convert_temperature_to_bytes_array(temperature: int) -> str:
    hex_bytes = bytes.fromhex("E0 00 00 14 02 05 0A 00")
    byte_array = bytearray(hex_bytes)
    byte_array[2] = temperature
    new_hex_bytes = bytes(byte_array)

    return new_hex_bytes.hex()
