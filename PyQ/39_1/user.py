class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def role(self):
        if self.email.endswith('@my-company.com'):
            return 'staff'
        else:
            return 'viewer'
