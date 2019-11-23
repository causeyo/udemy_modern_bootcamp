import re


def parse_date(input):
    date_regex = re.compile(r'\b(?P<d>\d{2})[./,]?(?P<m>\d{2})[./,]?(?P<y>\d{4})\b')
    match = date_regex.search(input)
    if match:
        month = match.group('m')
        day = match.group('d')
        if int(month) > 12:
            return None
        year = match.group('y')
        return {
                "d": day,
                "m": month,
                "y": year
                }


a = parse_date("22/01/1999")
print(a)
b = parse_date("01.22,1999")
print(b)
c = parse_date("01/22/1999")
print(c)
