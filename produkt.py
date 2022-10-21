class Product:
    def __init__(self,id:str,name:str,price:float,type:str):
        self.__name = name
        self.__id = id
        self.__price = price
        self.__priceType = type

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