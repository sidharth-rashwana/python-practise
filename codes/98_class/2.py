"""
Define a class named American and its subclass NewYorker.
"""


class American:
    class NewYorker:
        def print_country(self):
            print('NewYork')


a = American
n = a.NewYorker()
n.print_country()
