#make a laptop class in which u have to mention brand_name,model_name,price
#and u have to give the discount on the given amount
#and show the price after the discounted amount

class laptop:
    def __init__ (self,model,price,brand):
        self.brand=brand
        self.price=price
        self.model=model
    def discount(self,offer):
        print(f"-------\ndiscount offer is---> {offer}%")
        self.discount=(self.price*offer)/100
        self.discountedprice=self.price-self.discount
        print(f"\noriginal price is --->{self.price}")
        save_money=self.price-self.discountedprice
        print(f"\nyou save money is---> {save_money}")
        return print(f"\nthe price after discount is--> {self.discountedprice}\n------")

obj=laptop("mdx121001",60000,"lenovo")
obj.discount(20)

