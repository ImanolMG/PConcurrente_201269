import threading

class Boletos():
    def __init__(self) :
        self.boletos = 1000
        self.locked = threading.Lock()
        print("Se forma la fila")
        print("Boletos Disponibles: ", self.boletos)
    def comprar(self, y):
          self.locked.acquire()
          
          try:
             if (self.boletos) < 1:
                print("Turno " , y)
                print("Ya no hay boletos disponibles")
             else:
                print("Turno " , y)
                can_boletos = input("Cuantos boletos desea comprar?: ")
                if int(can_boletos) > self.boletos:
                   print("Solo quedan", self.boletos, "Boletos" )
                   can_boletos = input("Cuantos boletos desea comprar?: ")
                   self.boletos = self.boletos - int(can_boletos)
                else:
                   self.boletos = self.boletos - int(can_boletos)
            
          finally:
            self.locked.release()
            print("Boletos Disponibles: ", self.boletos)
            

def ventaboletos(x, y):
    x.comprar(y)

if __name__ == "__main__":
    boletos = Boletos()
    for y in range(5):
        tsart = threading.Thread(target=ventaboletos, args=(boletos , y))
        tsart.start()

        
