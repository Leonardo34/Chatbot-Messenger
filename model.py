class Guest:
    def __init__(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email): 
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_optin(self, optin):
        self.optin = optin

    def set_childrens(self, childrens):
        self.childrens = childrens

    def set_adults(self, adults):
        self.adults = adults        

    def __eq__(self, object):
        return self.id == object.id    

	