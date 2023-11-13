class ProductModel:
    def __init__(self, product_id, name, code, category, category_code, price) -> None:
        self.product_id = product_id
        self.name = name
        self.code = code
        self.category = category
        self.category_code = category_code
        self.price = price