from math import *
from string import *  
import sys
fi=open("DATA.in","r")
fo=open("output","w")    
sys.stdin=fi
sys.stdout=fo

m,n=map(int,input().split())
print(m+n)
