from decimal import Decimal

from Bank_Account.bank_account import BankAccount, MoneyInput


class SavingsAccount(BankAccount):
    """A bank account that earns interest at an annual percentage rate."""

    def __init__(
        self,
        account_number: str,
        owner_name: str,
        initial_balance: MoneyInput = Decimal("0.00"),
        annual_interest_rate: MoneyInput = Decimal("0.00"),
    ) -> None:
        super().__init__(account_number, owner_name, initial_balance)

        rate = self._to_decimal(annual_interest_rate)
        if rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        self.__annual_interest_rate = rate

    @property
    def annual_interest_rate(self) -> Decimal:
        return self.__annual_interest_rate

    def calculate_interest(self) -> Decimal:
        interest = self.balance * self.__annual_interest_rate / Decimal("100")
        return interest.quantize(Decimal("0.01"))
