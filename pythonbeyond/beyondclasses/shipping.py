import iso6346
'''
ShippingContainer class 
To demonstrate static methods,class methods,factory constructors,properties
'''


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 2109
    container_format = "<owner_code={0};contents={1}=bic_code:{2};volume={3}>"

    @staticmethod
    def make_bic_code(owner_code, serial):
        """Returns an ISO 6346 shipping container code.
        Args:
        owner_code (str): Three character alphabetic container code.
        serial (str): Six digit numeric serial number.
        """
        return iso6346.create(owner_code, serial=str(serial).zfill(6))

    @classmethod
    def get_next_serial(cls):
        """Gets  next serial number
        Args:
        None

        """
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        """ Creates Shipping Container with empty contents.
        Args:
        owner_code (str): Three character alphabetic container code.
        """
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        """ Creates Shipping Container with list of contents.
        Args:
        owner_code (str): Three character alphabetic container code.
        items:list of items

        """
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __str__(self):
        return ShippingContainer.container_format.format(
            self.owner_code,
            self.contents,
            self.bic_code, self.volume_ft3)

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        self.bic_code = self.make_bic_code(
            owner_code=self.owner_code,
            serial=ShippingContainer.get_next_serial())

    @property
    def volume_ft3(self):
        return (ShippingContainer.HEIGHT_FT *
                ShippingContainer.WIDTH_FT * self.length_ft)


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def make_bic_code(owner_code, serial):
        """Returns an ISO 6346 shipping container code.
        Args:
        owner_code (str): Three character alphabetic container code.
        serial (str): Six digit numeric serial number.
        """
        return iso6346.create(owner_code,
                              serial=str(serial).zfill(6),
                              category="R")

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenhiet):
        return (fahrenhiet - 32) * 5 / 9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature exceed {0}"
                             .format(RefrigeratedShippingContainer))
        self._celsius = value

    @property
    def fahrenhiet(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenhiet.setter
    def fahrenhiet(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return (super().volume_ft3 -
                RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        RefrigeratedShippingContainer.celsius.fset(self, value)
