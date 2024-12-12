import threading
from queue import Queue
import time
import random

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

    def is_free(self):
        return self.guest is None



class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)



class Cafe:
    def __init__(self, *tables):
        self.queve = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.is_free():
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queve.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queve.empty() or any(not table.is_free() for table in self.tables):
            for table in self.tables:
                if not table.is_free() and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')

                    if not self.queve.empty():
                        next_guest = self.queve.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number} ')



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

