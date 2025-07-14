from abc import ABC, abstractmethod 

# --- Abstract Interfaces ---
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass 

    @abstractmethod
    def remove_observer(self, observer):
        pass 

    @abstractmethod
    def notify_observers(self):
        pass 

class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass 


class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0 

    def register_observer(self, observer):
        self._observers.append(observer) 

    def remove_observer(self, observer):
        self._observers.remove(observer) 

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure) 

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers() 

# --- Concrete Observers ---
class PhoneDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display: Temperature - {temperature}, Humidity - {humidity}") 

class WindowDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Window Display: Pressure - {pressure}") 

class SmartWatchDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"SmartWatch Display: It's {temperature} degrees!") 

# --- Client Code ---
station = WeatherStation() 

phone = PhoneDisplay()
window = WindowDisplay()
watch = SmartWatchDisplay() 

station.register_observer(phone)
station.register_observer(window)
station.register_observer(watch) 

station.set_measurements(82, 70, 29.2) 

print("\n--- Removing Phone Display ---\n")
station.remove_observer(phone) 

station.set_measurements(78, 90, 29.9)