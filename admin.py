from genericpath import isfile
import os
from produkt import *

class AdminPage:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.run()
    def run(self):
        while True:
            print('*AdminVerktyg*')
            print('1. Ändra namn/pris på produkt')
            print('2. Sök kvitton')
            print('3. Lägg till Kampanjpris')
            print('4. Backa')
            
            try: 
                selection = int(input(' : '))
            except:
                print('Något gick fel.....')
            
            if selection == 1:
                self.changeProduct()
                with open('goodsfile.txt', 'w') as file:
                    for product in self.__productlist:
                        file.write(f'{product.getID()}:{product.getName()}:{product.getPrice()}:{product.getType()}\n')
            elif selection == 2:
                self.searchReceipt()
            elif selection == 3:
                pass
            elif selection == 4:
                return
    def changeProduct(self):
        print('Vilket ID vill du ändra på?')
        choice = input(' : ')
        for product in self.__productlist:
            if choice == product.getID():
                print(f'{product.getName()} {product.getPrice()}')
                print('Commands:')
                print('<namn/pris> <nytt värde>')
                print('BACKA')
                change = input(' : ')
                if change == 'BACKA':
                    break
                theType, theValue = change.split(' ')
                if theType == 'namn':
                    product.setName(theValue)
                if theType == 'pris':
                    product.setPrice(theValue)

    def searchReceipt(self):
        print('Vilken dag söker du?')
        print('Input = yyyy-mm-dd')
        receiptChoice = input(' : ')
        receiptPath = f'Receipts\\RECEIPT_{receiptChoice}.txt'
        if os.path.isfile(receiptPath):
            with open(receiptPath, 'r') as file:
                for lines in file:
                    parts = lines.split(':')
                    if parts[0] == 'Kvitto':
                        print(f'Kvitto:{parts[1][0]}')
                    if parts[0] == 'Total':
                        print(f'Total:{parts[1]}')
        
        print('Vilket kvittonummer vill du se?')
        print('Ange *BACKA* för att backa')
        printing = False
        choice = input(' : ')
        if choice == 'BACKA':
            pass
        elif os.path.isfile(receiptPath):
            with open(receiptPath, 'r') as file:
                for lines in file:
                    parts = lines.split(':')
                    if parts[0] == 'Kvitto':
                        if parts[1][0] == choice:
                            printing = True
                    if parts[0] == 'Total' and printing == True:
                        print(lines)
                        printing = False
                    if printing:
                        print(lines)

                        
                    

                        
