"""
handling erros
write a function which prints text in color
def colorize(text, color)
if provided color doesn't exist, function should raise error
"""


def colorize(text, color):
    colors = ("red", "blue", "white", "black")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if type(color) is not str:
        raise TypeError("color must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid")
    print("Printed {} in {}".format(text, color))

colorize("hello", "")
colorize("hello", "red")
colorize(34, "blue")