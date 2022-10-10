strings = "Python"
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# multiple var
name, nid = "Imtiaz", "1324342344"
print(name, nid)

# Global Variable
var = "awesome"


def myfunc():
    global xsl
    xsl = "fantastic"


myfunc()

print("Python is " + xsl)
