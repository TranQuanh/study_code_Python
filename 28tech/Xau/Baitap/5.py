s=input()
t=input()
set1=set(s)
set2=set(t)
giao=set1.intersection(set2)
print("".join(sorted(giao)))
hop=set1.union(set2)
print("".join(sorted(hop)))
        