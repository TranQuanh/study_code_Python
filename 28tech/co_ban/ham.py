# def xinchao(name1,name2,name3):
#     print("xin chao ",name1,name2,name3)
# #key word argument
# xinchao(name2="Teo",name3="Ti",name1="cho")    
# default arguement
def info(name,job="xe om"):
    print(name,job)
info("Quang Anh")
# Hàm gửi vào có kiểu dữ liệu j
#Hàm ra có kiểu dữ liệu j
#ucln
def ucln(a,b):
    while b:
        a,b=b,a%b
    return a
print(ucln(4,6)) 
#bisect_left: hoat dong nhu binary search
# from bisect import bisect_left