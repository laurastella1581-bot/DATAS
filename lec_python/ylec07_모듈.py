# 함수 정의
def add(a,b)  :
    res = a + b
    print(res)
    return res

# 함수 호출
son = add(4, 5)
print("받았음", son)



class PhoneBook :
    def __init__(self):
        print("init함수 호출....")

    def addc(self,a,b) :
        res = a + b
        return res

    def loginc(name):
        print(f"{name}님 로그인")

    def logins33(self , name):
        return name