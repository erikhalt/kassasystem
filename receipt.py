from datetime import datetime

class receipt:
    def __init__(self,productlist):
        self.__date = datetime.now()
        self.__productlist = productlist
        self.__receiptrows = []

    def addrows(self,productid,productamount):
        for rows in self.__receiptrows:
            if productid in rows:
                rows[3] += productamount
        for products in self.__productlist:
            if productid == products.getID():
                newrow = [productid,products.getName(),products.getPrice(),productamount]
                self.__receiptrows.append(newrow)
    def printexcisting(self):
        print(datetime.now())
        for rows in self.__receiptrows:
            print(f'{rows[1]}%t{rows[2]}*{rows[3]}%t= {rows[2]*rows[3]}')

    def printfull(self):
        print(self.__date)
        for rows in self.__receiptrows:
            print(f'{rows[1]}%t{rows[2]}*{rows[3]}%t= {rows[2]*rows[3]}')

