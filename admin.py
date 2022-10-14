

class AdminPage:
    def __init__(self):
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
                pass
            elif selection == 2:
                self.searchReceipt()
            elif selection == 3:
                pass
            elif selection == 4:
                return

    def searchReceipt(self):
        print('Vilken dag söker du?')
        print('Input = yyyy-mm-dd')
        receiptChoice = input(' : ')
