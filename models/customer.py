class Customer():
    """Cocaine Bear is a funny movie
    """
    # Class initializer. It has 2 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
new_customer = Customer(3, "Erin Stephens")
