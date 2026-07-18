1class Solution:
2    def convertTemperature(self, celsius: float) -> List[float]:
3        Kelvin = celsius + 273.15
4        Fahrenheit = celsius * 1.80 + 32.00
5        return [Kelvin,Fahrenheit]
6        