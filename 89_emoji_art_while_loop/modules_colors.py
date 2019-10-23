from termcolor import colored



# prepare text to print in color
text = colored("HI THERE!", color="red", on_color="on_green")
print(text)
text1 = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text1)


