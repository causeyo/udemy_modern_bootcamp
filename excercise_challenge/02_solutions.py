def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


def find_factors(num):
    factors = []
    i = 1
    while (i <= num):
        if (num % i == 0):
            factors.append(i)
        i += 1
    return factors


def includes(item, val, start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]


def repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr


def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string

    return string[:n - 3] + "..."
