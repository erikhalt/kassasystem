from datetime import datetime
import os

class receipt:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.__receiptrows = []
        self.__receiptrowids = []
        self.__nextreceiptnumber = 0
        self.__totalsum = 0
        self.__receiptdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__dateofpurchase = datetime.now().strftime("%Y-%m-%d")

        with open('nextreceiptnumber.txt') as file:
            rNumber = file.read()
        
        self.__nextreceiptnumber = int(rNumber)

        self.__campaigns = []
        with open('Campaign.txt','r') as file:
            self.__campaigns.append(file.readline())

    def addrows(self,productid,productamount):

        if productid in self.__receiptrowids:
            for rows in self.__receiptrows:
                if productid in rows:
                    rows[3] += productamount
        else:                    
            for products in self.__productlist:
                if len(self.__campaigns) > 0:
                    for campaigns in self.__campaigns:
                        partsCampaign = campaigns.split(':')
                        productCampaignStart = int(partsCampaign[2].replace('-',''))
                        productCampaignEnd = int(partsCampaign[3].replace('-',''))
                        dateOfPurchase = int(self.__dateofpurchase.replace('-',''))
                        if products.getID() == partsCampaign[0]:
                            if productCampaignStart <= dateOfPurchase <= productCampaignEnd:
                                if productid == products.getID():
                                    newrow = [productid,products.getName(),float(partsCampaign[1]),productamount]
                                    self.__receiptrows.append(newrow)
                            else:
                                if productid == products.getID():
                                    newrow = [productid,products.getName(),products.getPrice(),productamount]
                                    self.__receiptrows.append(newrow)

                else:
                        if productid == products.getID():
                            newrow = [productid,products.getName(),products.getPrice(),productamount]
                            self.__receiptrows.append(newrow)
        self.__receiptrowids.append(productid)
    
    def printexcisting(self):
        print(f'Kvitto:{self.__nextreceiptnumber}\t{self.__receiptdate}')        
        for rows in self.__receiptrows:
            self.__totalsum += (rows[2]*rows[3])
            print(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {rows[2]*rows[3]}')

        print(f'Total:{self.__totalsum}')

    def printfull(self):
        print(f'Kvitto: {self.__nextreceiptnumber}\t{self.__receiptdate}')        
        for rows in self.__receiptrows:
            self.__totalsum += (rows[2]*rows[3])
            print(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {rows[2]*rows[3]}')

        print(f'Total:{self.__totalsum}')

        with open('nextreceiptnumber.txt', 'w') as file:
            file.write(str(self.__nextreceiptnumber+1))
    
    def savetofile(self):
        if os.path.isfile(f'Receipts\\RECEIPT_{self.__dateofpurchase}.txt'):
            with open(f'Receipts\\RECEIPT_{self.__dateofpurchase}.txt', 'a') as file:
                
                file.write(f'Kvitto:{self.__nextreceiptnumber}\t{self.__receiptdate}\n')        
                for rows in self.__receiptrows:
                    self.__totalsum += (rows[2]*rows[3])
                    file.write(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {rows[2]*rows[3]}\n')

                file.write(f'Total:{self.__totalsum}\n')
        else:
            with open(f'Receipts\\RECEIPT_{self.__dateofpurchase}.txt', 'w+') as file:
                
                file.write(f'Kvitto:{self.__nextreceiptnumber}\t{self.__receiptdate}\n')        
                for rows in self.__receiptrows:
                    self.__totalsum += (rows[2]*rows[3])
                    file.write(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {rows[2]*rows[3]}\n')

                file.write(f'Total:{self.__totalsum}\n')
