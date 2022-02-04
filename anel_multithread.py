import threading
import time

class thread (threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
        self.on = False
        self.input = ''
        self.next = -1
        self.finished = False
    
    def turnOn(self, text):
        self.text = text
        self.on = True
    
    def setNext(self, next):
        self.next = next

    def run(self):
        print(f'T${self.num} - rodando')

        while not self.finished:
            if self.on:
                min = False
                for i in range(0, len(self.text)):
                    if self.text[i].islower():
                        min = True
                        self.text = self.text[:i] + self.text[i].upper() + self.text[i + 1:] 
                        break
                
                if min:
                    print(f'T${self.num} - ${self.text}')
                    self.on = False
                    time.sleep(1)
                    self.next.turnOn(self.text)
                else:
                    self.finished = True
            else:
                time.sleep(0.3)
    
        self.next.finished = True
        print(f'T${self.num} - encerrando')

    
class Ciclo:
    def __init__(self, n):
        self.threads = [thread(i) for i in range(0, n)]
        for i in range(0, n-1):
            self.threads[i].setNext(self.threads[i+1])
        
        self.threads[n-1].setNext(self.threads[0])

    def start(self, text):
        for i in self.threads:
            i.start()
        self.threads[0].turnOn(text)
  

def main():
    anel = Ciclo(30)
    text = input('Digite o input: ')

    anel.start(text)
    print('Finalizando Main')

main()