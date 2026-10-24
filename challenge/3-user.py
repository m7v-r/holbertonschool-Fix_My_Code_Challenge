#!/usr/bin/python3
""" 
User class
"""
import hashlib


class User():
    """ User class representation """

    def __init__(self):
        """ Initialization """
        self.__password = None

    @property
    def password(self):
        """ Getter for password """
        return self.__password

    @password.setter
    def password(self, pwd):
        """ Setter for password with MD5 hashing """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """ Check if password is valid """
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password


if __name__ == '__main__':
    print("Test User")

    user = User()
    user.password = "Test"
    if not user.is_valid_password("Test"):
        print("is_valid_password should return True if it's the right password")

    if user.is_valid_password("Test1"):
        print("is_valid_password should return False if it's not the right password")

    if user.is_valid_password("test"):
        print("is_valid_password should return False if it's not the right password")

    if user.is_valid_password(None):
        print("is_valid_password should return False if it's not the right password")

    if user.is_valid_password(123):
        print("is_valid_password should return False if it's not the right password")
