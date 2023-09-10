def create_temperature_set_payload(temperature: int) -> bytes:
    """
    Creates payload for temperature set packet
    Args:
        temperature: Temperature for packet

    Returns: Bytes of payload

    """
    assert temperature > 0
    assert temperature < 256

    return bytes([0xE0, 0x00, temperature, 0x14, 0x02, 0x05, 0x0A, 0x00])


def create_cooling_mode_payload(cooling_type: int = 1, cooling_mode: str = "max") -> bytes:
    """
    Creates payload for fan mode packet
    Args:
        cooling_type: Available types: 1 - Fans, 2 - Pump
        cooling_mode: Available modes: Zero, Balance, Performance, Quiet, Max, Default, Custom

    Returns: Bytes for payload

    """
    assert cooling_mode
    assert cooling_type in [1, 2]

    modes = {
        "zero": 7,
        "balance": 0,
        "performance": 5,
        "quiet": 6,
        "max": 4,
        "default": 2,
        "custom": 1
    }

    return bytes([0xE5, cooling_type, modes[cooling_mode.lower()], 0x00, 0x00, 0x00, 0x00, 0x00])
