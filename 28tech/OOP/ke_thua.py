class Nguoi:
    def __init__(self):
        print('ham khoi tao')
    def XinChao(self):
        print("Nguoi xin chao")
class SinhVien(Nguoi):
    def __init__(self):
        print("khoi tao")

p1=SinhVien()
p1.XinChao()
    