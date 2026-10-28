import json

from inventory import Inventory
from storage import ProductStorage
from terminal_display import configure_terminal, input_terminal, print_terminal


def display_products(products):
    if not products:
        print_terminal("لا توجد منتجات لعرضها.")
        return

    print_terminal("\nرقم | اسم المنتج | السعر | الكمية")
    print_terminal("-" * 45)
    for product in products:
        print_terminal(
            f"{product.product_id} | {product.name} | "
            f"{product.price:.2f} | {product.quantity}"
        )


def read_positive_number(prompt):
    value = float(input_terminal(prompt))
    if value <= 0:
        raise ValueError("أدخل رقمًا أكبر من صفر.")
    return value


def read_non_negative_integer(prompt):
    value = int(input_terminal(prompt))
    if value < 0:
        raise ValueError("أدخل صفرًا أو رقمًا صحيحًا موجبًا.")
    return value


def read_positive_integer(prompt):
    value = int(input_terminal(prompt))
    if value <= 0:
        raise ValueError("أدخل عددًا صحيحًا أكبر من صفر.")
    return value


def run():
    configure_terminal()
    storage = ProductStorage()
    try:
        inventory = Inventory(storage.load_products())
    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
        print_terminal(f"تعذر تحميل المنتجات من الملف: {error}")
        return

    while True:
        print_terminal(
            "\n=== إدارة المتجر ===\n"
            "1. إضافة منتج\n"
            "2. عرض المنتجات\n"
            "3. البحث عن منتج\n"
            "4. تعديل سعر أو كمية\n"
            "5. بيع منتج\n"
            "0. خروج"
        )
        choice = input_terminal("اختر العملية: ").strip()

        try:
            if choice == "1":
                name = input_terminal("اسم المنتج: ")
                price = read_positive_number("السعر: ")
                quantity = read_non_negative_integer("الكمية: ")
                product = inventory.add_product(name, price, quantity)
                storage.save_products(inventory.products)
                print_terminal(f"تمت إضافة {product.name} برقم {product.product_id}.")

            elif choice == "2":
                display_products(inventory.products)

            elif choice == "3":
                search_text = input_terminal("اكتب اسم المنتج أو جزءًا منه: ")
                display_products(inventory.search_products(search_text))

            elif choice == "4":
                product_id = int(input_terminal("رقم المنتج: "))
                product = inventory.get_product(product_id)
                print_terminal("اترك الحقل فارغًا إذا لم ترد تغييره.")
                price_text = input_terminal(
                    f"السعر الجديد (الحالي {product.price:.2f}): "
                )
                quantity_text = input_terminal(
                    f"الكمية الجديدة (الحالية {product.quantity}): "
                )
                price = float(price_text) if price_text.strip() else None
                quantity = int(quantity_text) if quantity_text.strip() else None
                inventory.update_product(product_id, price, quantity)
                storage.save_products(inventory.products)
                print_terminal("تم تحديث المنتج.")

            elif choice == "5":
                product_id = int(input_terminal("رقم المنتج: "))
                quantity = read_positive_integer("كمية البيع: ")
                total = inventory.sell_product(product_id, quantity)
                storage.save_products(inventory.products)
                print_terminal(f"تم البيع. الإجمالي: {total:.2f}")

            elif choice == "0":
                print_terminal("إلى اللقاء.")
                break

            else:
                print_terminal("اختيار غير صحيح. حاول مرة أخرى.")

        except (ValueError, OSError) as error:
            print_terminal(f"تعذر تنفيذ العملية: {error}")


if __name__ == "__main__":
    run()
