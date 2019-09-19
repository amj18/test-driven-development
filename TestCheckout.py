import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("Milk", 1)
    checkout.addItemPrice("Eggs", 2)
    return checkout

def test_canCalculateTotal(checkout):
    checkout.addItem("Milk")
    assert checkout.calculateTotal() == 1

def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("Milk")
    checkout.addItem("Eggs")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount("Milk", 3, 2)

#@pytest.mark.skip()
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("Milk", 3, 2)
    checkout.addItem("Milk")
    checkout.addItem("Milk")
    checkout.addItem("Milk")
    assert checkout.calculateTotal() == 2

def test_exceptionWithItemButNoPrice(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")