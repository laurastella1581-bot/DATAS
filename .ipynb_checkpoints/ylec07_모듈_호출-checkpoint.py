from lec_python.ylec07_모듈 import add

son = add(4, 5)
print("받았음", son)

from lec_python.ylec07_모듈 import add
son = add(4, 5)
print("받았음", son)

from lec_python.ylec07_모듈 import add
son = add(4, 5)
print("받았음", son)

from lec_python import ylec07_모듈, ylec07_모듈 as aa

son = ylec07_모듈.add(4, 5)
print("받았음", son)

son = aa.add(4,5)
print("받았음", son)

from lec_python.ylec07_모듈 import PhoneBook
PhoneBook.loginc("홍길동")

#-------------------------------------------------
pb =PhoneBook()
print(pb)

a = pb.addc(5, 3)
print(a)

PhoneBook.loginc("홍길동")


pb.loginc22("홍길동")

a = pb.logins33('홍길동')
print(f"{a}님 로그인")