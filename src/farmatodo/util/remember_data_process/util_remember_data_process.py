class UtilRememberDataProcess:
    __name_product = None
    __price_product = None

    @classmethod
    def set_name_product(cls, name_product):
        cls.__name_product = name_product
    @classmethod
    def get_name_product(cls):
        return cls.__name_product
    @classmethod
    def set_price_product(cls, price_product):
        cls.__price_product = price_product
    @classmethod
    def get_price_product(cls):
        return cls.__price_product
