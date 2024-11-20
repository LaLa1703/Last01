import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    self.lock.release()
            finally:
                if self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for j in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")
            self.lock.acquire()
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    if not self.lock.locked():
                        self.lock.acquire()
            finally:
                if self.lock.locked():
                    self.lock.release()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
