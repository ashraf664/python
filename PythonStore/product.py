class Product:
    """يمثل منتجًا واحدًا في المتجر."""

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        """تحويل المنتج إلى قاموس ليُحفظ بصيغة JSON."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        """إنشاء منتج من بيانات قُرئت من ملف JSON."""
        return cls(
            data["product_id"],
            data["name"],
            data["price"],
            data["quantity"],
        )
