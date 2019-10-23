import pyfiglet


def print_f(text_to_print, color="BLUE"):
    pyfiglet.print_figlet(text=text_to_print, colors=color)


user_text = input("what message do you want to print? ")
user_color = input("what color? ")

if user_color.upper() not in pyfiglet.COLOR_CODES.keys():
    user_color = "magenta"

print_f(text_to_print=user_text, color=user_color.upper())