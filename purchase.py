from receipt import * 

class newPurchase:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.receipt = receipt(self.__productlist)
        self.run()

    def run(self):
        while True:
            print('commands:')
            print('<productid> <amount>')
            print('PAY')
            command_selection = input('command: ')
            if command_selection.lower() == 'pay':
                print(self.receipt.printfull())
                return
            else:
                productid, amount = command_selection.split(' ')
                productid = str(productid)
                amount = int(amount)
                for object in self.__productlist:
                    if object.getID() == productid:
                        priceType = object.getType()
                self.receipt.addrows(productid,amount)
                self.receipt.printexcisting()

