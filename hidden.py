class userProperties:
    __password="password123!" #hiding variable
    def __init__(self, username, firstName, surname, email):
        self.username=username
        self.firstName=firstName
        self.surname=surname
        self.email=email

    #special function 'getters' to access hidden variables
    def getPassword(self):
        return self.__password
    
    def newPassword(self):
        conformation=input("Please confirm your old password: ")
        if conformation==self.__password:
           newPasswordEntry=input("Please enter your new password: ")
           self.__password=newPasswordEntry
        else:
            print("Your password is incorrect.")

user1=userProperties("erina.ameen", "Erina", "Ameen", "erina.ameen@gmail.com")
#print(user1.__password)  hidden password not accessible
print(user1.getPassword())
user1.newPassword()