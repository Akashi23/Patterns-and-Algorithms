from abc import ABC, abstractmethod
from typing import List
from time import sleep
from random import randint

class Observer(ABC):
    @abstractmethod
    def update(temp: float, humidity: float, pressure: float):
        raise NotImplementedError

class Subject(ABC):
    @abstractmethod
    def register_observer(self, o: Observer):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, o: Observer):
        raise NotImplementedError
    
    @abstractmethod
    def notify_observers():
        raise NotImplementedError

class DisplayElement:
    @abstractmethod
    def display(self):
        raise NotImplementedError

class WeatherStation(Subject):
    observers: List[Observer]
    temp: float
    humidity: float
    pressure: float

    def __init__(self) -> None:
        self.observers = []

    def register_observer(self, o: Observer) -> None:
        self.observers.append(o)

    def remove_observer(self, o: Observer) -> None:
        self.observers.remove(o)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure)

    def measurementsChanged(self)  -> None:
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(Observer, DisplayElement):
    temprature: float
    humidity: float
    weatherStation: WeatherStation

    def __init__(self, weatherStation: WeatherStation) -> None:
        self.weatherStation = weatherStation
        weatherStation.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temprature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f'Displayed Temperature: {self.temprature} Celsium, Humidity: {self.humidity}')


weatherStation = WeatherStation()

currentConditionsDisplay = CurrentConditionsDisplay(weatherStation)

for i in range(5):
    weatherStation.set_measurements(randint(12, 35), randint(50, 90), randint(720, 800))
    sleep(1)
    