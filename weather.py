import math

class Weather:
    def relative_humidity(self, temperature, dewpoint):
        total = 17.27 * ((dewpoint / (dewpoint + 237.3) - temperature) / (temperature + 237.3))
        return math.exp(total)
