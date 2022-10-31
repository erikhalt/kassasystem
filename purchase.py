from receipt import * 

class newPurchase:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.receipt = receipt(self.__productlist)
        

    def run(self):
        while True:
            print('commands:')
            print('<productid> <amount>')
            print('PAY')
            command_selection = input('command: ')
            if command_selection.lower() == 'pay':
                self.receipt.savetofile()
                print(self.receipt.printfull())
                
                return
            else:
                try:
                    productid, amount = command_selection.split(' ')
                    productid = str(productid)
                    amount = float(amount)
                    for products in self.__productlist:
                        if products.getID() == productid and products.getType() == 'kr/st':
                            try:
                                int_amount = int(amount)
                                if int_amount != amount:
                                    raise ValueError
                                self.receipt.addrows(productid,amount)
                                self.receipt.printexcisting()
                            except ValueError:
                                print('produkt av denna typ kan bara vara heltal i amount.')
                        elif products.getID() == productid:
                            self.receipt.addrows(productid,amount)
                            self.receipt.printexcisting()
                except:
                    print('felinmatning...')
