from abc import ABC,abstractmethod

class Bike(ABC):
    @abstractmethod
    def transmission(self):pass
    @abstractmethod
    def start(self):pass

class Pulser(Bike):

    def transmission(self):
        print("Pulser transmission")

    def start(self):
        print("pulser start")   

pulser_instance=Pulser()

pulser_instance.transmission()

pulser_instance.start()