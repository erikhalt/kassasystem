import os
from produkt import *
from globalFunctions import *

class AdminPage:
    def __init__(self,productlist):
        self.__productlist = productlist
        
    def run(self):
        while True:
            print('*AdminVerktyg*')
            print('1. Ändra namn/pris på produkt')
            print('2. Sök kvitton')
            print('3. Kampanjer')
            print('4. Backa')
            selection = menuChoice(4)
            if selection == 1:
                self.changeProduct()
                with open('goodsfile.txt', 'w') as file:
                    for product in self.__productlist:
                        file.write(f'{product.getID()}:{product.getName()}:{product.getPrice()}:{product.getType()}\n')
            elif selection == 2:
                self.searchReceipt()
            elif selection == 3:
                print('1. Ändra kampanj')
                print('2. Lägg till ny kampanj')
                choice = menuChoice(2)
                if choice == 2:
                    self.NewcampaignPrice()
                if choice == 1:
                    self.changeCampaign()
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
                    return
                theType, theValue = change.split(' ')
                if theType == 'namn':
                    product.setName(theValue)
                if theType == 'pris':
                    product.setPrice(theValue)


    def searchReceipt(self):
        print('Vilken dag söker du?')
        print('Input = yyyy-mm-dd')
        receiptChoice = input(' : ')
        if not checkvalidDate(receiptChoice):
            print('Felaktigt inmatning i datum ange yyyy-mm-dd')
            return
        receiptPath = f'Receipts\\RECEIPT_{receiptChoice}.txt'
        if os.path.isfile(receiptPath):
            with open(receiptPath, 'r') as file:
                for lines in file:
                    parts = lines.split(':')
                    if parts[0] == 'Kvitto':
                        receiptNumber = parts[1].split('\t')
                        receiptNumber = receiptNumber[0]
                        print(f'Kvitto:{receiptNumber}')
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
                        receiptNumber = parts[1].split('\t')
                        receiptNumber = receiptNumber[0]
                        if receiptNumber == choice:
                            printing = True
                    if parts[0] == 'Total' and printing == True:
                        print(lines)
                        printing = False
                    if printing:
                        print(lines)


    def NewcampaignPrice(self):
        campaignList = []
        with open('Campaign.txt', 'r') as file:
            for line in file:
                campaignList.append(line.replace('\n',''))

        choiceID = input('Vilket ID vill du lägga till/ändra kampanj på?')
        for products in self.__productlist:
            if products.getID() == choiceID:
                print('Vilket pris ska kampanjen ha?')
                newCampaign = newfloatPrice()
                while True:
                    campaignStart = input('Vilket datum ska det börja (yyyy-mm-dd)')
                    if not checkvalidDate(campaignStart):
                        print('Felaktig inmatning av Startdatum')
                    else:
                        break
                while True:
                    campaignEnd = input('Vilket datum ska det sluta (yyyy-mm-dd)')
                    if not checkvalidDate(campaignEnd):
                        print('Felaktig inmatning av Slutdatum')

                    if checkValidDateSpan(campaignStart,campaignEnd):
                        break
                print('Vill du spara kampanjen? (Ja/Nej)')
                choiceSave = input(' : ')
                if choiceSave.lower() == 'ja':
                        campaignList.append(f'{choiceID}:{newCampaign}:{campaignStart}:{campaignEnd}\n')

        with open('Campaign.txt','w') as file:
            for campaigns in campaignList:
                file.write(f'{campaigns}\n')



    def changeCampaign(self):
        campaignList = []
        with open('Campaign.txt', 'r') as file:
            for line in file:
                campaignList.append(line.replace('\n',''))

        for campaign_index, campaigns in enumerate(campaignList):
            if campaigns != '':
                print(f'{campaign_index+1}. {campaigns}')
        print(f'Vilken kampanj vill du ändra på?(1-{len(campaignList)})')
        choiceCampaign = menuChoice(len(campaignList))

        print('Vill du ändra eller ta bort kampanj?')
        print('1. Ändra')
        print('2. Ta bort')
        choiceChange = menuChoice(2)

        if choiceChange == 2:
            del campaignList[choiceCampaign-1]

        if choiceChange == 1:
            newPrice = input('Nytt Pris: ')
            newStart = input('Ny Start (yyyy-mm-dd): ')
            if not checkvalidDate(newStart):
                print('Felaktig inmatning av Startdatum')
                return
            newEnd  = input('Nytt Slut (yyyy-mm-dd)')
            if not checkvalidDate(newEnd):
                print('Felaktig inmatning av Slutdatum')
                return
            parts = campaignList[choiceCampaign-1].split(':')
            del campaignList[choiceCampaign-1]
            changedCampaign = f'{parts[0]}:{newPrice}:{newStart}:{newEnd}'
            campaignList.append(changedCampaign)

        with open('Campaign.txt','w') as file:
            for campaigns in campaignList:
                file.write(f'{campaigns}\n')
