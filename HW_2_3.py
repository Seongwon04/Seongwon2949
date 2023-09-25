class Item:
    count = 0
    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1

    def getprice(self):
        return print('%s의 가격은 %d원 입니다.' %(self.title, self.price))
    
class Book(Item):
    def __init__(self, title, price, page, writer):
        super().__init__(title, price)
        self.page = page
        self.writer = writer
    
    def __str__(self):
        return '제목: %s, 가격: %s, 페이지 수: %s, 저자: %s' %(self.title, self.price, self.page, self.writer)

class Magazine(Item):
    def __init__(self, title, price, month):
        super().__init__(title, price)
        self.month = month

    def __str__(self):
        return '제목: %s, 가격: %s, 출간 월: %s' %(self.title, self.price, self.month)



book1 = Book('소나기', 10000, 124, '황순원')
book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
book3 = Book('난쏘공', 12000, 112, '조세희')
magazine1 = Magazine('보그',11000, 9)
magazine2 = Magazine('싱글즈',13000, 8)
print('', book1,'\n', book2, '\n', book3, '\n', magazine1, '\n', magazine2)
print('총',Item.count,'권')
book2.getprice()
magazine1.getprice()
book1.getprice()

