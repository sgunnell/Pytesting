#test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet(20)

@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet(50)

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 70),
    (20, 2, 68),
])

def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

def test_default_initial_amount(empty_wallet):
  #wallet = Wallet() replaced with fixture
  assert empty_wallet.balance ==0

def test_setting_initial_amount(wallet):
    #wallet = Wallet(100)#replaced with fixture
    assert wallet.balance ==20

def test_wallet_add_cash(wallet):
    #wallet = Wallet(10) replaced with fixture
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    #wallet = Wallet(20) replaced with fixture
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    #wallet = Wallet() replaced with fixture
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
