from datetime import datetime

class receipt:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.__receiptrows = []
        self.__receiptrowids = []
        self.__nextreceiptnumber = 0

        with open('nextreceiptnumber.txt') as file:
            rNumber = file.read()
        
        self.__nextreceiptnumber = int(rNumber)

    def addrows(self,productid,productamount):
        if productid in self.__receiptrowids:
            for rows in self.__receiptrows:
                if productid in rows:
                    rows[3] += productamount
        else:                    
            for products in self.__productlist:
                if productid == products.getID():
                    newrow = [productid,products.getName(),products.getPrice(),productamount]
                    self.__receiptrows.append(newrow)
        self.__receiptrowids.append(productid)
    
    def printexcisting(self):
        
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Kvittonummer: {self.__nextreceiptnumber}')
        for rows in self.__receiptrows:
            print(f'{rows[1]}%t{rows[2]}*{rows[3]}%t= {rows[2]*rows[3]}')

    def printfull(self):
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Kvittonummer: {self.__nextreceiptnumber}')
        for rows in self.__receiptrows:
            print(f'{rows[1]}%t{rows[2]}*{rows[3]}%t= {rows[2]*rows[3]}')
        with open('nextreceiptnumber.txt', 'w') as file:
            file.write(str(self.__nextreceiptnumber+1))

