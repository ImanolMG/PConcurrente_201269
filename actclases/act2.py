import time
import threading




def gestionar(vartemp):
    print(vartemp, "Finalizado")

def buffer(tipoentrada):
    vartemp = tipoentrada
    gestionar(vartemp)


def escritor():
    for limite in range(3):
        time.sleep(3)
        nescritor = "Escritor"+str(limite)
        buffer(nescritor)

def lector():
    for limite in range(3):
        time.sleep(3)
        nlectura = "Lector"+str(limite)
        buffer(nlectura)
 
if __name__ == "__main__":
   threading.Thread(target=escritor).start()
   threading.Thread(target=lector ).start()