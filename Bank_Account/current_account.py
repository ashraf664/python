from decimal import Decimal

from Bank_Account.bank_account import BankAccount, MoneyInput


class CurrentAccount(BankAccount):
    """A bank account that does not earn interest or allow overdrafts."""

    def __init__(
        self,
        account_number: str,
        owner_name: str,
        initial_balance: MoneyInput = Decimal("0.00"),
    ) -> None:
        super().__init__(account_number, owner_name, initial_balance)

    def calculate_interest(self) -> Decimal:
        return Decimal("0.00")
