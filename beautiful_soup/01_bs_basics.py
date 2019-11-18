from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""


def linebreak(text=""):
    print('\n' + 10 * '*' + ' {} '.format(text) + 10 * '*')


soup = BeautifulSoup(html, "html.parser")
linebreak("soup.body.div")
print(soup.body.div)  # only first match

linebreak("find 'div'")
d1 = soup.find("div")  # only first match
print(d1)

linebreak("find_all 'div'")
d2 = soup.find_all("div")  # all matches
print(d2)

linebreak("find 'id'")
d4 = soup.find(id="first")  # css id should be unique so it should be searched with 'find', not 'findall'
print(d4)

linebreak("find 'class'")
d5 = soup.find_all(class_="special")  # class_ should be use because 'class' is a special word in python
print(d5)

linebreak("find attributes")
d5 = soup.find_all(attrs={"data-example": "yes"})  # class_ should be use because 'class' is a special word in python
print(d5)

"""
navigating with CSS Selectors

select - returns a list of elements matching a CSS selector
 - select by id of foo: #foo
 - select by class of bar: .bar
 - select children: div > p
 - select descendents: div p 

# find an element with an id of foo
soup.find(id="foo")
soup.select("#foo")[0]

# find all elements with a class of bar
# careful! "class" is a reserved word in python
soup.find_all(class_="bar")
soup.select(".bar")

# find all elements with a data
# attribute of "baz"
# using the general attrs kwarg
soup.find_all(attrs={"data-baz":True})
soup.select("[data-baz]")

"""
linebreak('select by css id')
s1 = soup.select("#first")  # select always returns a list
print(s1)

linebreak('select by css class')
s2 = soup.select(".special")
print(s2)

linebreak('select by tag - div')
s3 = soup.select("div")
print(s3)

linebreak('select by attribute -> data-example')
s4 = soup.select("[data-example]")
print(s4)