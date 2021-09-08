class my_solution():
    
    def __init__(self):
        self._str = ""

    def get_String(self):
        self._str = input('Entrez une chaîne de caractères : ')

    def print_String(self):
        print(self._str.upper())

my = my_solution()
my.print_String()
my.get_String()
my.print_String()
