from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
from typing import Union


MoneyInput = Union[Decimal, int, float, str]


class BankAccount(ABC):
    """Base class shared by the bank's account types."""

    def __init__(
        self,
        account_number: str,
        owner_name: str,
        initial_balance: MoneyInput = Decimal("0.00"),
    ) -> None:
        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Account number must not be empty.")
        if not isinstance(owner_name, str) or not owner_name.strip():
            raise ValueError("Owner name must not be empty.")

        balance = self._to_decimal(initial_balance)
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.__account_number = account_number.strip()
        self.__owner_name = owner_name.strip()
        self.__balance = balance

    @staticmethod
    def _to_decimal(amount: MoneyInput) -> Decimal:
        if isinstance(amount, bool):
            raise ValueError("Amount must be a valid money value.")
        try:
            value = Decimal(str(amount))
        except (InvalidOperation, TypeError, ValueError):
            raise ValueError("Amount must be a valid money value.") from None

        if not value.is_finite():
            raise ValueError("Amount must be a finite number.")
        try:
            rounded_value = value.quantize(Decimal("0.01"))
        except InvalidOperation:
            raise ValueError("Amount is too large to process.") from None
        if value != rounded_value:
            raise ValueError("Amount cannot have more than two decimal places.")
        return value

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def owner_name(self) -> str:
        return self.__owner_name

    @property
    def balance(self) -> Decimal:
        return self.__balance

    def deposit(self, amount: MoneyInput) -> Decimal:
        amount_value = self._to_decimal(amount)
        if amount_value <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount_value
        return self.__balance

    def withdraw(self, amount: MoneyInput) -> Decimal:
        amount_value = self._to_decimal(amount)
        if amount_value <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount_value > self.__balance:
            raise ValueError("Insufficient funds.")

        self.__balance -= amount_value
        return self.__balance

    def get_account_details(self) -> str:
        return (
            f"Account type: {type(self).__name__}\n"
            f"Account number: {self.__account_number}\n"
            f"Owner: {self.__owner_name}\n"
            f"Balance: {self.__balance:.2f}"
        )

    @abstractmethod
    def calculate_interest(self) -> Decimal:
        """Return the interest for this account type."""
        raise NotImplementedError
