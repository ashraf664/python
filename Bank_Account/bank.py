from decimal import Decimal
from typing import Dict, List, Tuple

from Bank_Account.bank_account import BankAccount, MoneyInput
from Bank_Account.current_account import CurrentAccount
from Bank_Account.savings_account import SavingsAccount


class Bank:
    """Stores accounts and coordinates banking operations."""

    def __init__(self) -> None:
        self.__accounts: Dict[str, BankAccount] = {}

    def add_account(self, account: BankAccount) -> None:
        if not isinstance(account, BankAccount):
            raise TypeError("Only bank account objects can be added.")
        if account.account_number in self.__accounts:
            raise ValueError("An account with this number already exists.")
        self.__accounts[account.account_number] = account

    def create_savings_account(
        self,
        account_number: str,
        owner_name: str,
        initial_balance: MoneyInput = Decimal("0.00"),
        annual_interest_rate: MoneyInput = Decimal("0.00"),
    ) -> SavingsAccount:
        account = SavingsAccount(
            account_number,
            owner_name,
            initial_balance,
            annual_interest_rate,
        )
        self.add_account(account)
        return account

    def create_current_account(
        self,
        account_number: str,
        owner_name: str,
        initial_balance: MoneyInput = Decimal("0.00"),
    ) -> CurrentAccount:
        account = CurrentAccount(account_number, owner_name, initial_balance)
        self.add_account(account)
        return account

    def get_account(self, account_number: str) -> BankAccount:
        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Account number must not be empty.")
        try:
            return self.__accounts[account_number.strip()]
        except KeyError:
            raise ValueError("Account not found.") from None

    def list_accounts(self) -> List[BankAccount]:
        return list(self.__accounts.values())

    def transfer(
        self,
        source_account_number: str,
        target_account_number: str,
        amount: MoneyInput,
    ) -> Tuple[Decimal, Decimal]:
        source = self.get_account(source_account_number)
        target = self.get_account(target_account_number)
        if source is target:
            raise ValueError("Source and target accounts must be different.")

        source_balance = source.withdraw(amount)
        target_balance = target.deposit(amount)
        return source_balance, target_balance
