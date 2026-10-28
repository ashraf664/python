from bank import Bank


def show_menu() -> None:
    print("\n=== نظام البنك ===")
    print("1. إنشاء حساب توفير")
    print("2. إنشاء حساب جارٍ")
    print("3. عرض جميع الحسابات")
    print("4. عرض تفاصيل حساب")
    print("5. إيداع")
    print("6. سحب")
    print("7. تحويل بين حسابين")
    print("8. حساب فائدة حساب توفير")
    print("0. خروج")


def main() -> None:
    bank = Bank()

    while True:
        show_menu()
        choice = input("اختر عملية: ").strip()

        try:
            if choice == "1":
                account = bank.create_savings_account(
                    input("رقم الحساب: "),
                    input("اسم صاحب الحساب: "),
                    input("الرصيد الابتدائي: "),
                    input("معدل الفائدة السنوي (%): "),
                )
                print(f"تم إنشاء حساب التوفير رقم {account.account_number}.")
            elif choice == "2":
                account = bank.create_current_account(
                    input("رقم الحساب: "),
                    input("اسم صاحب الحساب: "),
                    input("الرصيد الابتدائي: "),
                )
                print(f"تم إنشاء الحساب الجاري رقم {account.account_number}.")
            elif choice == "3":
                accounts = bank.list_accounts()
                if not accounts:
                    print("لا توجد حسابات حتى الآن.")
                for account in accounts:
                    print(account.get_account_details())
                    print(
                        "الفائدة السنوية المحسوبة: "
                        f"{account.calculate_interest():.2f}\n"
                    )
            elif choice == "4":
                account = bank.get_account(input("رقم الحساب: "))
                print(account.get_account_details())
            elif choice == "5":
                account = bank.get_account(input("رقم الحساب: "))
                balance = account.deposit(input("مبلغ الإيداع: "))
                print(f"تم الإيداع. الرصيد الجديد: {balance:.2f}")
            elif choice == "6":
                account = bank.get_account(input("رقم الحساب: "))
                balance = account.withdraw(input("مبلغ السحب: "))
                print(f"تم السحب. الرصيد الجديد: {balance:.2f}")
            elif choice == "7":
                source_number = input("رقم الحساب المُرسل: ")
                target_number = input("رقم الحساب المُستقبل: ")
                amount = input("مبلغ التحويل: ")
                source_balance, target_balance = bank.transfer(
                    source_number,
                    target_number,
                    amount,
                )
                print("تم التحويل بنجاح.")
                print(f"رصيد الحساب المُرسل: {source_balance:.2f}")
                print(f"رصيد الحساب المُستقبل: {target_balance:.2f}")
            elif choice == "8":
                account = bank.get_account(input("رقم الحساب: "))
                print(f"الفائدة السنوية: {account.calculate_interest():.2f}")
            elif choice == "0":
                print("إلى اللقاء.")
                break
            else:
                print("اختيار غير صحيح. حاول مرة أخرى.")
        except (TypeError, ValueError) as error:
            print(f"تعذر تنفيذ العملية: {error}")


if __name__ == "__main__":
    main()
