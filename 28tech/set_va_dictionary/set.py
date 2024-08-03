a={1,4,1,2,5,6,2,1}
print(a)
a.add(1)
a.add(2)
print(a)
a.update([100,"abc"])
print(a)
# xoá: remove(lỗi nếu xoá ptu ko trg set),discard
a={1,2,3,4,5}
b={2,3,4,5,6}
print(a|b)
print(a&b)
print(a-b)
print(a^b)
print(a.isdisjoint(b))
c={1,2,3}
print(c.issubset(a))