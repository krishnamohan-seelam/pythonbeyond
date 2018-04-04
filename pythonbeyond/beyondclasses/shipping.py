import iso6346
'''
ShippingContainer class 
To demonstrate static methods,class methods,factory constructors

'''
class ShippingContainer:

    next_serial =2109

    @staticmethod 
    def make_bic_code(owner_code,serial):
        """Returns an ISO 6346 shipping container code.
        Args:
        owner_code (str): Three character alphabetic container code.
        serial (str): Six digit numeric serial number.
        """
        return iso6346.create(owner_code,serial=str(serial).zfill(6))
   
        
    @classmethod
    def get_next_serial(cls):
        """Gets  next serial number
        Args:
        None

        """
        result  = cls.next_serial
        cls.next_serial  += 1
        return result

    @classmethod
    def create_empty(cls,owner_code):
        """ Creates Shipping Container with empty contents.
        Args:
        owner_code (str): Three character alphabetic container code.
        """
        return cls(owner_code,contents =None)

    @classmethod
    def create_with_items(cls,owner_code,items):
        """ Creates Shipping Container with list of contents.
        Args:
        owner_code (str): Three character alphabetic container code.
        items:list of items
        
        """
        return cls(owner_code,contents =list(items))

    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic_code =ShippingContainer.make_bic_code(
            owner_code =self.owner_code,
            serial=ShippingContainer.get_next_serial())

    
