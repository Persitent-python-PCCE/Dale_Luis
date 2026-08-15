class Product:

    def __init__(
        self,
        product_id=None,
        product_name=None,
        p_description=None,
        price=0.0,
        stock=0,
        category_id=None,
        supplier_id=None,
        is_active=True
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.p_description = p_description
        self.price = price
        self.stock = stock
        self.category_id = category_id
        self.supplier_id = supplier_id
        self.is_active = is_active

    def __str__(self):
        return (
            f"{self.product_id} | "
            f"{self.product_name} | "
            f"₹{self.price} | "
            f"Stock: {self.stock}"
        )