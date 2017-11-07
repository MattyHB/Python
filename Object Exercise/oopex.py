# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: oopex.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program is designed to create an Address Book 
#       that matches names with emails.
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
class Address:
    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email

    def getEmail(self):
        return self.__email

    def getName(self):
        return self.__name

    def setEmail(self, newEmail: str):
        self.__email = newEmail

    def setName(self, newName: str):
        self.__name = newName
    
    def isValidEmail(self) -> bool:
        for ch in self.getEmail():
            if not ch.isalnum() and ch not in '@_.':
                return False     
        return True


    def __repr__(self):
        return 'Name: {0} , Email: {1}'.format(self.__name, self.__email)


class AddressBook:

    def __init__(self, addresses: dict):
        self.__addresses = {addresses}

    def insert(self, Address):
        self.__addresses = self.__addresses + (Address)

    def getCount(self):
        num = 0
        for i in self.__addresses:
            num += 1
        return num







# ------ Test ------

def test_Address():
    addr = Address('Frank', 'frank@somewhere.com')
    assert addr.getName() == 'Frank'
    assert addr.getEmail() == 'frank@somewhere.com'
    assert addr.isValidEmail() == True

    addr.setName('Joe')
    assert addr.getName() == 'Joe'
    addr.setEmail('joe_123@elsewhere.net')
    assert addr.getEmail() == 'joe_123@elsewhere.net'
    assert addr.isValidEmail() == True

    addr = Address('Lydia', 'lydiagmail!@.com')
    assert addr.getName() == "Lydia"
    assert addr.getEmail() == 'lydiagmail!@.com'
    assert addr.isValidEmail() == False
    
# Finish the header