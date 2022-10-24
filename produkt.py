class Product:
    def __init__(self,id:str,name:str,price:float,type:str):
        self.__name = name
        self.__id = id
        self.__price = price
        self.__priceType = type
        self.__campaign = 0
        self.__campaignStart = ''
        self.__campaignEnd = ''

    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getID(self):
        return self.__id
    def getType(self):
        return self.__priceType
    def setName(self,name):
        self.__name = name
    def setPrice(self,price):
        self.__price = price

    def getCampaign(self):
        return self.__campaign
    def setCampaign(self,campaign):
        self.__campaign = campaign

    def getCampaignStart(self):
        return self.__campaignStart
    def setCampaignStart(self,date):
        self.__campaignStart = date

    
    def getCampaignEnd(self):
        return self.__campaignEnd
    def setCampaignEnd(self,date):
        self.__campaignEnd = date