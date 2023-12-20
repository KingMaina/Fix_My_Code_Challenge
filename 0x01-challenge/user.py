#!/usr/bin/python3
"""
User class
"""


class User():
    """ Represents a user """

    def __init__(self):
        """ Initialize a user object """
        self.__email = None

    @property
    def email(self):
        """ Gets the value of the email property """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets the value of the email property """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
