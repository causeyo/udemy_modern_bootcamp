import re
text_tmp = "Fracking you"


def censor(text):
    pattern = re.compile(r'\bfrack\w*\b', re.I)
    result = pattern.sub("CENSORED", text)
    return result

c = censor(text_tmp)
print(c)
