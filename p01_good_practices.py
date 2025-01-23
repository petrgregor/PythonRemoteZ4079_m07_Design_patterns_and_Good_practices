#import my_package
from my_package.my_super_module import my_perfect_function

# PEP 8 - konvence pojmenování
# proměnná
number = 5


# funkce
def add_numbers(a=0, b=0):
    """ add_numbers method
        :param a (int)
        :param b (int)

        return sum of a and b
    """
    return a + b


def my_function(name):
    """Purpose of the function.

    Description od parameters (optional).

    Return values (optional).

    Preconditions (optional).

    Side effects (optional).

    Additional information (further explanations, bibliography references,
    examples of use) (optional).
    """
    pass


# třída
class MyClass:
    """MyClass
    Demo class for this module.
    """

    def method1(self):
        pass

    def method2(self):
        pass


# konstanta
PI = 3.14159

print(my_function.__doc__)
print(add_numbers.__doc__)

# neporovnáváme booleovské hodnoty s hodnotami True a False.
is_prime = True
if is_prime:  # nepoužíváme if is_prime == True:
    print("Is prime.")
if not is_prime:  # nepoužíváme if is_prime == False:
    print("Is not prime.")

# používáme logický kontext (např. prázdný string je False)
# my_string = ""  # False
my_string = "Ahoj"  # True
if my_string:
    print(f"my_string = {my_string}")
else:
    print("my_string is empty")

x = None
if x is not None:
    print(f"x = '{x}'")

name = "Petr"
# if name[:1] == "P":  # toto nepoužíváme
if name.startswith('P'):
    print(f"name '{name}' starts with 'P'")


def my_method():
    """my method docstring"""
    pass


# use of docstring
print(f"Docstring for print function:\n{print.__doc__}")


