#in this there are some laptops in which there are
# different different discounts are applied on laptops so

class laptop():
    discount_on=10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def apply_discount(self):
        x=self.price*self.discount_on/100
        return self.price-x

l1=laptop("acer","cs2",100000)
print(l1.apply_discount())
l2=laptop("dell","sc2",50000)
l2.discount_on=50
print(l2.apply_discount())
l3=laptop("lenovo","asa",40000)
print(l3.apply_discount())
l4=laptop("apple","mac",200000)
l4.discount_on=100
print(l4.apply_discount())

## in this u can see the discount percent is change for only the one laptop
#that we wanted that we have to choose on
# how much discount we want on a particular laptop


# class laptop():
# #    discount_on=10
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def apply_discount(self,discount):
#         x=self.price*discount/100
#         return self.price-x
#
# l1=laptop("acer","cs2",100000)
# print(l1.apply_discount(10))
# l2=laptop("dell","sc2",50000)
# print(l2.apply_discount(50))
# l3=laptop("lenovo","asa",40000)
# print(l3.apply_discount(10))
# l4=laptop("apple","mac",200000)
# print(l4.apply_discount(100))
