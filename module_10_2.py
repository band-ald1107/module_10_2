import threading
from threading import Thread
import time

class knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f'{self.name} сражается {self.days} дней..., осталось {self.enemies} воинов.')
        print(f"{self.name} одержал победу спустя {self.days} {'день' if self.days == 1 else 'дня'}!")

knight1 = knight("Рыцарь Артур", 20)
knight2 = knight("Рыцарь Ланселот", 30)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Битвы окончены!")