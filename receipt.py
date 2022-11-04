from datetime import datetime
import os

class receipt:
    def __init__(self,productlist):
        self.__productlist = productlist
        self.__receiptrows = []
        self.__receiptrowids = []
        self.__nextreceiptnumber = 0
        self.__receiptdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__dateofpurchase = datetime.now().strftime("%Y-%m-%d")

        with open('nextreceiptnumber.txt') as file:
            rNumber = file.read()
        
        self.__nextreceiptnumber = int(rNumber)

        

        self.__campaignDateToday = int(self.__dateofpurchase.replace('-',''))

    def addrows(self,productid,productamount):
        campaign = False
        self.__campaigns = []
        with open('Campaign.txt','r') as file:
            for lines in file:
                self.__campaigns.append(lines.replace('\n', ''))

        if productid in self.__receiptrowids:
            for rows in self.__receiptrows:
                if productid in rows:
                    rows[3] += productamount
        else:                    
            for products in self.__productlist:
                if productid == products.getID():
                    
                    for campaigns in self.__campaigns:
                        partsCampaign = campaigns.split(':')
                        productCampaignStart = int(partsCampaign[2].replace('-',''))
                        productCampaignEnd = int(partsCampaign[3].replace('-',''))
                        productCampaignPrice = float(partsCampaign[1])
                        productCampaignID = partsCampaign[0]
                        if productCampaignID == productid:
                            if productCampaignStart <= self.__campaignDateToday <= productCampaignEnd:
                                campaign = True
                                newrow = [productid,products.getName(),productCampaignPrice,productamount]
                                self.__receiptrows.append(newrow)
                                self.__receiptrowids.append(productid)
            if not campaign:
                for products in self.__productlist:
                    if productid == products.getID():
                        newrow = [productid,products.getName(),products.getPrice(),productamount]
                        self.__receiptrows.append(newrow)
                        self.__receiptrowids.append(productid)
                
    
    def printexcisting(self):
        totalsum = 0
        print(f'Kvitto:{self.__nextreceiptnumber}\t{self.__receiptdate}')        
        for rows in self.__receiptrows:
            totalsum += (rows[2]*rows[3])
            print(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {round((rows[2]*rows[3]),2)}')

        print(f'Total:{round((totalsum),2)}')

    def printfull(self):
        totalsum = 0
        print(f'Kvitto: {self.__nextreceiptnumber}\t{self.__receiptdate}')        
        for rows in self.__receiptrows:
            totalsum += (rows[2]*rows[3])
            print(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {round((rows[2]*rows[3]),2)}')

        print(f'Total:{round((totalsum),2)}')

        with open('nextreceiptnumber.txt', 'w') as file:
            file.write(str(self.__nextreceiptnumber+1))
    
    def savetofile(self):
        if os.path.isfile(f'Receipts\\RECEIPT_{self.__dateofpurchase}.txt'):
            with open(f'Receipts\\RECEIPT_{self.__dateofpurchase}.txt', 'a') as file:
                totalsum = 0
                file.write(f'Kvitto:{self.__nextreceiptnumber}\t{self.__receiptdate}\n')        
                for rows in self.__receiptrows:
                    totalsum += (rows[2]*rows[3])
                    file.write(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {round((rows[2]*rows[3]),2)}\n')

                file.write(f'Total:{round((totalsum),2)}\n')
        else:
            with open(f'Receipts\\RECEIPT_{self.__dateofpurchase}.txt', 'w+') as file:
                totalsum = 0
                file.write(f'Kvitto:{self.__nextreceiptnumber}\t{self.__receiptdate}\n')        
                for rows in self.__receiptrows:
                    totalsum += (rows[2]*rows[3])
                    file.write(f'{rows[1]} antal {rows[3]} á {rows[2]}\t\t= {round((rows[2]*rows[3]),2)}\n')

                file.write(f'Total:{round((totalsum),2)}\n')
