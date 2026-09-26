import unittest

from account.account import Account

class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account = Account("Abdulkadir")
        self.assertEqual("abdulkadir", account.name)
        self.assertEqual(account.balance, 0)

    def test_that_account_can_receive_deposit(self):
        account = Account("Abdulkadir")
        account.deposit(1000)
        self.assertEqual(account.balance, 1000)

    def test_that_account_can_not_receive_negative_amount(self):
        account = Account("Abdulkadir")
        self.assertRaises(ValueError, account.deposit, -1000)

    def test_that_account_can_withdraw(self):
        account = Account("Abdulkadir")
        account.set_pin(1234)
        account.deposit(5000)
        account.withdraw(1000, 1234)
        self.assertEqual(account.balance, 4000)
    def test_that_I_cant_withdraw_from_empty_balance(self):
        account = Account("Abdulkadir")
        account.set_pin(1234)
        account.withdraw(5000, 1234)
        self.assertEqual(account.balance, 0)

    def test_that_account_cannot_withdraw_with_negative_amount(self):
        account = Account("Abdulkadir")
        account.set_pin(1234)
        self.assertRaises(ValueError, account.withdraw, -1000, 1234)

    def test_that_i_cant_withdraw_more_than_balance(self):
        account = Account("Abdulkadir")
        account.deposit(5000)
        account.set_pin(1234)
        account.withdraw(6000, 1234)
        self.assertEqual(account.balance, 5000)

if __name__ == '__main__':
    unittest.main()