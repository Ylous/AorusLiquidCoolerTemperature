from aorus_liquid_cooler.enums import CoolingMode, CoolingType


def create_temperature_set_payload(temperature: int) -> bytes:
    """
    Creates payload for temperature set packet
    Args:
        temperature: Temperature for packet

    Returns: Bytes of payload

    """
    assert 256 > temperature > 0

    return bytes([0xE0, 0x00, temperature, 0x14, 0x02, 0x05, 0x0A, 0x00])


def create_cooling_mode_payload(cooling_type: CoolingType,
                                cooling_mode: CoolingMode) -> bytes:
    """
    Creates payload for fan mode packet
    Args:
        cooling_mode: Cooling mode
        cooling_type: Fans or pump

    Returns: Bytes for payload

    """
    assert cooling_type in CoolingType
    assert cooling_mode in CoolingMode

    return bytes([0xE5, cooling_type, cooling_mode, 0x00, 0x00, 0x00, 0x00, 0x00])
