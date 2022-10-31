import sys
from admin import AdminPage
from globalFunctions import menuChoice
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
                self.__productlist.append(Product(parts[0],parts[1],float(parts[2]),parts[3].replace('\n', '')))
        while True:
            print('**Kassa**')
            print('1. Nytt köp')
            print('2. Adminmenu')
            print('3. Avsluta')
            
            selection = menuChoice(3)

            if selection == 1:
                Purchase = newPurchase(self.__productlist)
                Purchase.run()
            elif selection == 2:
                Adminmenu = AdminPage(self.__productlist)
                Adminmenu.run()

            elif selection == 3:
                self.exit()
    
    def exit(self):
        sys.exit()


if __name__ == '__main__':
    System = system()
    System.run()