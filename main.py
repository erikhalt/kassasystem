import sys
from purchase import *
from receipt import *
from produkt import *


class system:
    def __init__(self):
        self.__productlist = []
        
    def run(self):
        with open('goodsfile.txt') as file:
            for line in file:
                parts = line.split(':')
                self.__productlist.append(Product(parts[0],parts[1],int(parts[2]),parts[3].replace('\n', '')))
        while True:
            print('**Kassa**')
            print('1. Nytt köp')
            print('2.Avsluta')
            
            try: 
                sel = int(input(' : '))
            except:
                print('något gick fel....')

            if sel == 1:
                newPurchase(self.__productlist)
            elif sel == 2:
                self.exit()
            elif sel == 3:
                
    
    def exit(self):
        sys.exit()


if __name__ == '__main__':
    System = system()
    System.run()