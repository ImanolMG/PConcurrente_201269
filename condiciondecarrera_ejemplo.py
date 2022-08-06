import threading
import time
class Condicion_carrera():
    def __init__(self) :
        self.locked = threading.Lock()
    def ejecutar_proceso(self, y):
          self.locked.acquire()
          try:
             print("Ejecutando proceso en hilo")
             time.sleep(y)
          finally:
              print("Hilo finalizado")
              self.locked.release()

            

def procesos(x, y):
    x.ejecutar_proceso(y)

if __name__ == "__main__":
    condicion_carrera = Condicion_carrera()
    for y in range(5):
        tsart = threading.Thread(target=procesos, args=(condicion_carrera , 5))
        tsart.start()
        tsart.join()

        
