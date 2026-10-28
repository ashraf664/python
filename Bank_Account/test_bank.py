import unittest
from decimal import Decimal

from bank import Bank
from bank_account import BankAccount


class BankSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.savings = self.bank.create_savings_account(
            "S001",
            "Ali",
            "100.00",
            "5",
        )
        self.current = self.bank.create_current_account(
            "C001",
            "Sara",
            "100.00",
        )

    def test_deposit_increases_balance(self) -> None:
        self.savings.deposit("25.00")
        self.assertEqual(self.savings.balance, Decimal("125.00"))

    def test_withdraw_decreases_balance(self) -> None:
        self.current.withdraw("30.00")
        self.assertEqual(self.current.balance, Decimal("70.00"))

    def test_invalid_transactions_do_not_change_balance(self) -> None:
        with self.assertRaises(ValueError):
            self.savings.deposit("0")
        with self.assertRaises(ValueError):
            self.current.withdraw("101.00")

        self.assertEqual(self.savings.balance, Decimal("100.00"))
        self.assertEqual(self.current.balance, Decimal("100.00"))

    def test_transfer_moves_money_between_accounts(self) -> None:
        self.bank.transfer("S001", "C001", "40.00")

        self.assertEqual(self.savings.balance, Decimal("60.00"))
        self.assertEqual(self.current.balance, Decimal("140.00"))

    def test_failed_transfer_does_not_change_balances(self) -> None:
        with self.assertRaises(ValueError):
            self.bank.transfer("S001", "C001", "150.00")

        self.assertEqual(self.savings.balance, Decimal("100.00"))
        self.assertEqual(self.current.balance, Decimal("100.00"))

    def test_transfer_to_same_account_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.bank.transfer("S001", "S001", "10.00")

        self.assertEqual(self.savings.balance, Decimal("100.00"))

    def test_savings_and_current_accounts_calculate_interest_polymorphically(
        self,
    ) -> None:
        accounts = self.bank.list_accounts()
        interest_by_number = {
            account.account_number: account.calculate_interest()
            for account in accounts
        }

        self.assertEqual(interest_by_number["S001"], Decimal("5.00"))
        self.assertEqual(interest_by_number["C001"], Decimal("0.00"))

    def test_duplicate_account_number_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.bank.create_current_account("S001", "Another Owner")

    def test_invalid_initial_balance_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.bank.create_current_account("C002", "Omar", "-1.00")

    def test_unprocessable_initial_balance_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.bank.create_current_account("C002", "Omar", "1E+100")

    def test_abstract_base_class_cannot_be_instantiated(self) -> None:
        with self.assertRaises(TypeError):
            BankAccount("A001", "Mona")


if __name__ == "__main__":
    unittest.main()
