s=input()
s=s.split()
s.sort()
print(' '.join(s))
s.sort(key=lambda x:[len(x),x])
print(' '.join(s))