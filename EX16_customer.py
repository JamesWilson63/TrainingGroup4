from person import Person

class Customer(Person):
    def __init__(self, name, gender,acnum):
        super().__init__(name, gender)
        self.acnum = acnum

    def __str__(self):
        return super().__str__() + " Acc#: " + self.acnum
