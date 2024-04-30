"""
Define a class named American which has a static method called printNationality.
"""


class American:
    @staticmethod
    def printNationality():
        print('America')


# static method do not require instance to be created
American.printNationality()
