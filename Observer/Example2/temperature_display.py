# ConcreteObserver (Observador Concreto)
from weather_observer import WeatherObserver


class TemperatureDisplay(WeatherObserver):
    def update(self, temperature):
        print(f"Nova temperatura: {temperature}°C")

class Fan(WeatherObserver):
    def update(self, temperature):
        if temperature > 25:
            print("Ligando o ventilador.")
        else:
            print("Desligando o ventilador.")

