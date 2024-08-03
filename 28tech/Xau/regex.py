import re
text='co cai gi dau Hieu oi'
pattern=r'Thinh'
result=re.sub('Hieu',pattern,text)
print(result)

text='ban oi ban la con cho a ban oi'
matches=re.findall('ban',text)
print(matches)


text="xin chao ban, ban lam cai chi rua"
matches=re.search("ban",text)
print(matches.span())
print(matches.group())
print(matches.string    )