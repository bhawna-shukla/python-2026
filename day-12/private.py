#private (like) attributes & methods
#conceptual  implement & methods  are meant to be used  only which the class and are not accesible from outside  the class 



class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

s1 = account(12536,"abcde")
print(s1.acc_no)
print(s1.__acc_pass)    #thos is private using double underscore
