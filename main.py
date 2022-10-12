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
                self.__productlist.append(Product(parts[0],parts[1],int(parts[2]),parts[3].replace('\n', '')))
        while True:
            print('**Kassa**')
            print('1. Nytt köp')
            print('2.Avsluta')
            
            sel = int(input(' : '))

            if sel == 1:
                newPurchase(self.__productlist)
            elif sel == 2:
                return
    
    def exit():
        sys.exit()


if __name__ == '__main__':
    System = system()
    System.exit()