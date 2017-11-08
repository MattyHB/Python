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

    def __init__(self):
        self.__addresses = {}

    def insert(self, a):
        self.__addresses[a.getName()] = a

    def getCount(self):
        return len(self.__addresses)
    
    def get(self, name: str):
        if name in self.__addresses:
            return self.__addresses[name]
        else:
            return None
    def getNames(self):
        AlphList = []
        for i in sorted(self.__addresses):
            AlphList.append(i)
        return AlphList

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

def test_AddressBook():
    book = AddressBook()
    assert book.getCount() == 0

    book.insert(Address('Frank', 'frank@bju.edu'))
    assert book.getCount() == 1

    book.insert(Address('Helen', 'helen@bju.edu'))
    assert book.getCount() == 2

    book.get('Frank') == Address('Frank', 'frank@bju.edu')
    book.get('GiveMeAnA+OnThisAssignment') == None

    names = book.getNames()
    assert names == ['Frank', 'Helen']

    addr = book.get('Frank')
    assert addr != None
    assert addr.getName() == 'Frank'
    assert addr.getEmail() == 'frank@bju.edu'

    addr = book.get('Helen')
    assert addr.getEmail() == 'helen@bju.edu'

    addr = book.get('Joey')
    assert addr == None