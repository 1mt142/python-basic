string = "Imtiaz"
itgr = 10
flt = 12.99
cmplex = complex(flt)
print(cmplex)

# list
listArry = [1, 22, 22, 33, 4, 5, 6]
# tuple
tpl = (1, 2, 3, 4, 5, 6, 9, 9)
print(tpl)
# range
rng = range(10)
print(rng)
# dictionary
dic = {"name": string, "price": flt}
print(dic)
# set // unique value
st = {1, 2, 3, 4, 5, 5, 6}
print(st)
bol = True
print(type(bol))
# frozenset // unique
frzValue = ({1, 1, 1, 2, 2})
print(frzValue)

# bytes
bty = x = b"Hello"
print(bty)

# byte array
bArr = bytearray(5)

# display x:
print(type(bArr))

x = memoryview(bytes(5))

# display x:
print(x)

# display the data type of x:
print(type(x))

x = None
print(x)
