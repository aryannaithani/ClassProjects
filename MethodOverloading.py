class NewStr(str):

    def __init__(self, inp):
        self.input = str(inp)

    def isEmail(self):
        valid_emails = ['@gmail.com', '@gla.ac.in']
        result = 'Invalid Email'
        for email in valid_emails:
            if self.input.endswith(email):
                result = 'Valid Email'
        return result

    def upper(self):
        return 'Upper of NewStr'


obj1 = NewStr('aryannaithani1085@g.com')
obj2 = NewStr('aryannaitani@gla.ac.in')
print(obj1.isEmail())
print(obj2.isEmail())
