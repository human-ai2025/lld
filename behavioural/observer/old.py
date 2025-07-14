class PhoneDisplay:
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display: Temperature - {temperature}, Humidity - {humidity}") 

class WindowDisplay:
    def update(self, temperature, humidity, pressure):
        print(f"Window Display: Pressure - {pressure}") 

class WeatherStation:
 def __init__(self):
    self._temperature = 0
    self._humidity = 0
    self._pressure = 0
    self._phone_display = PhoneDisplay()
    self._window_display = WindowDisplay() 

 def set_measurements(self, temperature, humidity, pressure):
    self._temperature = temperature
    self._humidity = humidity
    self._pressure = pressure
    self.measurements_changed() 

 def measurements_changed(self):
    self._phone_display.update(self._temperature, self._humidity, self._pressure)
    self._window_display.update(self._temperature, self._humidity, self._pressure) 

# Client Code
station = WeatherStation()
station.set_measurements(80, 65, 30.4)

# The WeatherStation has direct references to each display object and call their methods explicitly. 
