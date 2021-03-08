import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def qnt():
    qnt = 'qnt'
    return qnt

@pytest.fixture()
def price():
    price = 'price'
    return price

@pytest.fixture()
def discount():
    discount = 'discount'
    return discount

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_improperInputs(invoice, monkeypatch):
    inputs = iter(['n', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    unit_price = invoice.inputNumber("Input a non-number: ")
    assert unit_price == 3
        
def test_isProductAdded(invoice, qnt, price, discount):
    invoice.addProduct(qnt, price, discount)
    assert qnt == qnt
    assert price == price
    assert discount == discount
