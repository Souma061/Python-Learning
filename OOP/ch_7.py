class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.strength = strength

# class GingerChai(Chai):   #Code duplication
#     def __init__(self,type_,strength,spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# class GingerChai(Chai):  #Explicitly calling the parent class constructor
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


class GingerChai(Chai):  #Using super() to call the parent class constructor
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
