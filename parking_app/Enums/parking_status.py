from enum import Enum

class ParkingStatus(str, Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    UNAVAILABLE = "unavailable"