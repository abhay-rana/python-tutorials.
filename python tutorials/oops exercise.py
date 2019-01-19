#make a laptop class in which u have to mention brand_name,model_name,price
#and u have to give the discount on the given amount
#and show the price after the discounted amount

class laptop():
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def apply_discount(self,discount):
        x=self.price*discount/100
        return self.price-x
l1=laptop("acer","x2s",50000)
print("original price is",l1.price)
print(l1.apply_discount(50))
