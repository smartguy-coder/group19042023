from enum import Enum

# TANK_POWER = 33
#
# ART_POWER = 50
# ART_PRECISION = 30
#
# TANK_PRECISION = 50

# TANK_SETTINGS = {
#     'TANK_POWER': 30,
#     'TANK_PRECISION': 50,
# }
#
# ART_SETTINGS = {
#     'ART_POWER': 50,
#     'ART_PRECISION': 30,
# }


class TankSettings(Enum):
    TANK_POWER: int = 33
    TANK_PRECISION: int = 50


class ArtSettings(Enum):
    ART_POWER: int = 50
    ART_PRECISION: int = 30


class JavelinSettings(Enum):
    JAVELIN_POWER: int = 100
    JAVELIN_PRECISION: int = 90
