class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9

print(TemperatureConverter.celsius_to_fahrenheit(20))
print(TemperatureConverter.fahrenheit_to_celsius(99))
