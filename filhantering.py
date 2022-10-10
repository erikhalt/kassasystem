minfil = []
class produkt:
    def __init__(self,id,namn,pris,typ):
        self.id = id
        self.namn = namn
        self.pris = pris
        self.type = typ
# p1 = produkt(300,'bananer',15,'kr/kg')
# p2 = produkt(305,'äpple',12,'kr/kg')

# minfil.append(p1)
# minfil.append(p2)

# with open('goodsfile.txt', 'w') as file:
#     for produkt in minfil:
#         file.write(f'{produkt.id}:{produkt.namn}:{produkt.pris}:{produkt.type}\n')

with open('goodsfile.txt') as file:
    for line in file:
        p = line.split(':')
        minfil.append(produkt(p[0],p[1],int(p[2]),p[3].replace('\n', '')))

print(minfil)