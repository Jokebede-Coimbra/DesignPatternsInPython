from fan import Fan
from temperature_display import TemperatureDisplay
from weather_station import WeatherStation

# Uso do padrão Observer
weather_station = WeatherStation()

temperature_display = TemperatureDisplay()
fan = Fan()

weather_station.add_observer(temperature_display)
weather_station.add_observer(fan)

weather_station.set_temperature(20)
weather_station.set_temperature(30)
