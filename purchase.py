

class newPurchase:
    def __init__(self, goods:dict):
        self.goods = goods
        self.goods_id = self.goods.keys()
        self.goods_price = self.goods_id[0]
        self.goods_name = self.goods_id[1]
        
        self.run()

    def run(self):

