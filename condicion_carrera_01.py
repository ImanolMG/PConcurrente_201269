import threading
import time
import random

class Boletos():
    def __init__(self) :
        self.boletos = 1000
        self.locked = threading.Lock()
        print("se bloquen todos los hilos")

    def comprar(self, y):
          self.locked.acquire()
          try:
             if (self.boletos) < 1:
                print("Ya no hay boletos disponibles")
             else:
                print("Turno " , y)
                print("Cuantos boletos desea comprar")
                can_boletos = input()
                self.boletos = self.boletos - int(can_boletos)
            
          finally:
            self.locked.release()
            print("Boletos Restantes: ", self.boletos)
            

def ventaboletos(x, y):
    x.comprar(y)

if __name__ == "__main__":
    boletos = Boletos()
    for y in range(5):
        tsart = threading.Thread(target=ventaboletos, args=(boletos , y))
        tsart.start()

        
