import threading
import time
import random


class Contador():
    def __init__(self, conta= 0) :
        self.locked = threading.Lock()
        print("se bloquen todos los hilos")
        self.conta_send = conta
    
    def incrementar(self):
        self.locked.acquire()

        try:
            print("messirve")
            self.conta_send += 1
            print(self.conta_send)
        finally:
            self.locked.release()
            print("messirvio")

def fun_conta(x):
    for y in range(5):
        time_f = random.random()
        time.sleep(time_f)
        x.incrementar()

if __name__ == "__main__":
    contador = Contador()
    for y in range(5):
        tsart = threading.Thread(target=fun_conta, args=(contador ,))
        tsart.start()