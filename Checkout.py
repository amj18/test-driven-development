from typing import Dict

class Checkout:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item: str, numberOfItems: int, price: float) -> None:
        discount = self.Discount(numberOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item: str, price: int) -> None:
        self.prices[item] = price

    def addItem(self, item: str) -> None:
        if item not in self.prices:
            raise Exception("Item has no price")

        if item in self.items:
            self.items[item] +=1
        else:
            self.items[item] = 1

    def calculateTotal(self) -> int:
        total = 0
        for item, cnt in self.items.items():
            total += self.canCalculateItemTotal(item, cnt)
        return total

    def canCalculateItemTotal(self, item: str, cnt: int) -> int:
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.canCalculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def canCalculateItemDiscountedTotal(self, item: str, cnt: int, discount: Dict) -> int:
        total = 0
        numberOfDiscounts = cnt / discount.nbrItems
        total += numberOfDiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total