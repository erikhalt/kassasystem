import sys
from purchase import *
from receipt import *

class system:
    def __init__(self):
        self.goods_file = {'300':[10,'bananer'], '301':[8,'Äpple']}

        

    def run(self):
        while True:
            print('**Kassa**')
            print('1. Nytt köp')
            print('2.Avsluta')
            
            try:
                sel = int(input(' : '))
            except:
                print('Något gick fel vänligen gör val 1/2...')

            if sel == 1:
                newPurchase(self.goods_file)
            if sel == 2:
                sys.exit()


if __name__ is '__main__':
    System = system()
    System.run()