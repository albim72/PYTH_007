class Celsius:
    def __init__(self, temp_c: float):
        self._temp_c = temp_c

    @property
    def fahrenheit(self) -> float:
        return (self._temp_c * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self._temp_c = (value - 32) / 1.8

    @property
    def kelvin(self) -> float:
        return self._temp_c + 273.15

    @kelvin.setter
    def kelvin(self, value: float) -> None:
        self._temp_c = value - 273.15


if __name__ == '__main__':
    t = Celsius(20)
    print(t.fahrenheit)
    t.fahrenheit = 77
    print(t.kelvin)
    t.kelvin = 293.15
    print(t.fahrenheit)
    print(t._temp_c)
