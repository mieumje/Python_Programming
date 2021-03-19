a = "We are the Future"
print(a)

b = []
for i in a:
    x = chr(ord(i)-1)
    """ print(chr(ord(i)-1)) """
    print(x, end="")
    b.append(x)
print("")


for i in b:
    print(chr(ord(i)+1), end="")
