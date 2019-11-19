"""
navigating via TAGS:
- parent/parents
- contents
- next_sibling / next_siblings
- previous_sibling / next_sibling

navigating via SEARCHING:
- find_parent / find_parents
- find_next_sibling / find_next_siblings
- find_previous_sibling / find_previous_siblings
"""

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
    <li class="special super-special">This list item is special.</li>
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
data = soup.body.contents
print(data) # list with new_lines between elements

linebreak("first element will be '\\n'")
data1 = soup.body.contents[0]
print(data1)

linebreak("second element will be 'div'")
data2 = soup.body.contents[1]
print(data2)

linebreak("with usage of 'next_sibling' we can move forward to next element on the same level which will be '\\n'")
data3 = soup.body.contents[1].next_sibling
print(data3)

linebreak("with usage of 'next_sibling' we can move forward to next element on the same level which will be 'ol'")
data4 = soup.body.contents[1].next_sibling.next_sibling
print(data4)

linebreak("find class super-special")
data5 = soup.find(class_="super-special")
print(data5)

linebreak("find parent of class super-special -> 'ol'")
data6 = soup.find(class_="super-special").parent
print(data6)

linebreak("find parent of parent of class super-special -> 'body'")
data6 = soup.find(class_="super-special").parent.parent
print(data6)

linebreak("find id='first'")
data7 = soup.find(id="first")
print(data7)

linebreak("find_next_sibling to id='first' -> omit '\\n' element")
data8 = soup.find(id="first").find_next_sibling()
print(data8)

linebreak("chain of find_next_sibling to id='first' -> omit '\\n' element")
data9 = soup.find(id="first").find_next_sibling().find_next_sibling()
print(data9)

linebreak("select attribute data-example")
data10 = soup.select("[data-example]")
print(data10)

linebreak("select first attribute data-example")
data11 = soup.select("[data-example]")[1]
print(data11)

linebreak("find_previous_sibling to select first attribute data-example")
data12 = soup.select("[data-example]")[1].find_previous_sibling()
print(data12)

linebreak("find class super-special")
data13 = soup.find(class_="super-special")
print(data13)

linebreak("find_next_sibling to class super-special which contains 'class_=special'")
data14 = soup.find(class_="super-special").find_next_sibling(class_="special")
print(data14)

linebreak("find 'h3' element")
data15 = soup.find("h3")
print(data15)

linebreak("find parent of 'h3' element")
data16 = soup.find("h3").find_parent()
print(data16)

linebreak("find parent of 'h3' element with passed argument 'html'- it is silly because there is always one 'html'")
data17 = soup.find("h3").find_parent("html")
print(data17)