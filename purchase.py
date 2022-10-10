class newPurchase:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.run()

    def run(self):
        while True:
            print('commands:')
            print('<productid> <amount>')
            print('PAY')
            command_selection = input('command: ')
            if command_selection.lower() == 'pay':
                return
            else:
                productid, amount = command_selection.split(' ')
                print(productid)
                print(amount)




list = [1,23]
newPurchase(list)