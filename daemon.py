from threading import *
import time 
  
def thread_1():                       
  for i in range(8): 
    print('Este es el hilo T') 
    time.sleep(1) 
  
T = Thread(target = thread_1)  
  
T.setDaemon(True)                    
  
T.start()                            
time.sleep(5) 
print('Este es el hilo principal')  