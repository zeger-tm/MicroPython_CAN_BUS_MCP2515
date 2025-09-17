
from machine import Pin, SPI as MICROPYTHON_SPI

from .spi import SPI


SPI_SCK_PIN = "PB13"
SPI_MOSI_PIN = "PB12"
SPI_MISO_PIN = "PB13"
SPI_CS_PIN = "PB15"

class SPIPICO(SPI):
    def init(self, baudrate: int) -> Any :
        return MICROPYTHON_SPI(
            4,
            sck=Pin(SPI_SCK_PIN),
            mosi=Pin(SPI_MOSI_PIN),
            miso=Pin(SPI_MISO_PIN),
            baudrate=baudrate
        )