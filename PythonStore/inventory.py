from product import Product


class Inventory:
    """يدير منتجات المتجر وعمليات البيع والتعديل عليها."""

    def __init__(self, products=None):
        self.products = products if products is not None else []

    def add_product(self, name, price, quantity):
        if not name.strip():
            raise ValueError("اسم المنتج لا يمكن أن يكون فارغًا.")
        if price <= 0:
            raise ValueError("يجب أن يكون السعر أكبر من صفر.")
        if quantity < 0:
            raise ValueError("لا يمكن أن تكون الكمية سالبة.")

        next_id = max(
            (product.product_id for product in self.products),
            default=0,
        ) + 1
        product = Product(next_id, name.strip(), price, quantity)
        self.products.append(product)
        return product

    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        raise ValueError("لم يُعثر على منتج بهذا الرقم.")

    def search_products(self, search_text):
        search_text = search_text.strip().casefold()
        return [
            product
            for product in self.products
            if search_text in product.name.casefold()
        ]

    def update_product(self, product_id, price=None, quantity=None):
        product = self.get_product(product_id)
        if price is not None:
            if price <= 0:
                raise ValueError("يجب أن يكون السعر أكبر من صفر.")
            product.price = price
        if quantity is not None:
            if quantity < 0:
                raise ValueError("لا يمكن أن تكون الكمية سالبة.")
            product.quantity = quantity
        return product

    def sell_product(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("يجب أن تكون كمية البيع أكبر من صفر.")

        product = self.get_product(product_id)
        if quantity > product.quantity:
            raise ValueError("الكمية المطلوبة غير متوفرة في المخزون.")

        product.quantity -= quantity
        return product.price * quantity
