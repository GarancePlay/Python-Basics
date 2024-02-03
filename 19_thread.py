
#19 Thread

import time
from threading import Thread
from threading import RLock # 

def process_one():
    i = 0
    while i < 3 :
        print("XXXXX")
        time.sleep(0.3)
        i += 1

def process_two():
    i = 0
    while i < 3 :
        print("OOOOO")
        time.sleep(0.3)
        i += 1

thread1 = Thread(target=process_one)
thread2 = Thread(target=process_two)

thread1.start()
thread2.start()

thread1.join() # On attend la fin de l'execution des thread
thread2.join() # pour poursuivre le traitement sequentiel

print("End of process!")


