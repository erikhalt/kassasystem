import sys
from purchase import *
from receipt import *
from produkt import *
class system:
    def __init__(self):
        self.__productlist = []
        self.run()
    def run(self):
        with open('goodsfile.txt') as file:
            for line in file:
                parts = line.split(':')
                self.productlist.append(Product(parts[0],parts[1],int(parts[2]),parts[3].replace('\n', '')))
        while True:
            print('**Kassa**')
            print('1. Nytt köp')
            print('2.Avsluta')
            
            try:
                sel = int(input(' : '))
            except:
                print('Något gick fel vänligen gör val 1/2...')

            if sel == 1:
                newPurchase(self.productlist)
            if sel == 2:
                return
    
    def exit():
        sys.exit()


if __name__ is '__main__':
    System = system()
    System.exit()