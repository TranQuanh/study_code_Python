from collections import Counter
s='28tech python 28tech java java'
a=s.split()
b=set(a)
print(b)

s="28tech?Python.C++!Bahoa"
delim='?!.'
for x in delim:
    s=s.replace(x,' ')
print(s)