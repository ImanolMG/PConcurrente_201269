import signal
import os
import time
 
def receive_signal(signal,stack):
    print('receive ',stack)
 
#signal.signal(signal.SIGALRM, receive_signal)
sigs = set(signal.Signals)
for sig in sigs:
    try:
        signal.signal(sig, receive_signal)
        print(sig)
    except:
        print('error: ',sig)
 
 
#signal.signal(signal.SIGUSR2, receive_signal)
x=0
while x<2:
    time.sleep(4)
    x+=1

#https://rico-schmidt.name/pymotw-3/signal/index.htmls