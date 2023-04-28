# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서
# 특정 작업(처리)을 수행하고
# output(출력)을 반환한다.

# 내장 함수(built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

# abs(값)
# absolute의 약자
# 입력한 숫자형 데이터의 절댓값을 반환한다.
# print(abs(100)) # 100
# print(abs(-100)) # 100
# print(abs(3.15)) # 3.15
# print(abs(-3.15)) # 3.15

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다.
# print(sum([1, 2, 3, 4, 5])) # 15

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 4, 5])) # 5

# min(리스트)
# 리스트 안에서 최솟값을 찾아 반환한다.
# print(min([1, 2, 3, 4, 5])) # 1

# chr(정수)
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다.
# print(chr(65)) # A

# ord(문자)
# 문자 1개를 입력받고 해당하는 정수를 반환한다.
# print(ord('A')) # 65

# round(값)
# round(값, 소수 자릿수)
# 반올림 함수
# print(round(1.234)) # 1
# print(round(1.234, 2)) # 1.23
# print(round(1.369, 1)) # 1.4

# 함수 정의(define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결괏값 return value
"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결괏값
"""
# def 함수를 정의하는 명령어
# 함수이름도 변수 이름처럼 규칙을 지켜서 지어야 한다.
# 영어, 숫자, _만 사용
# 숫자로 시작x, 띄어쓰기x, 키워드 사용x
# 기존에 이미 정의된 함수 이름도 피하는 것이 좋음
# def print_names():
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")

# print_names()

# def get_name():
#     return "최태욱"

# def print_my_name():
#     print(get_name())

# print_my_name()
# a = print_names() # 리턴이 없음
# b = get_name() # 리턴이 있음
# # print(a)
# print(b)

# parameter
# 함수에 입력하는 값
# 매개변수, argument 혼용
# def add(a, b):
#     return a + b

# def print_add(a, b):
#     print(a + b)

# result = add(1, 2)
# print(result)

# print_add(1, 2)
# result = print_add(1, 2)
# print(result)

# print_add("안녕", 1) # 숫자형, 문자형 연산은 Error
# print_add(1, 2) # 3
# print_add("안녕", "하세요") # 안녕하세요
# print_add("하세요", "안녕") # 하세요안녕
# print_add(b="하세요", a="안녕") # 안녕하세요

# def swap_number(a, b): # a, b는 지역 변수   # 이름이 같더라도 서로 다른 변수
#     temp = a
#     a = b
#     b = temp
#     print(a, b)
#     return a, b
# a = 1 # a, b는 전역 변수
# b = 2
# print("함수 호출 전", a, b)
# a, b = swap_number(a, b)
# print("함수 호출 후", a, b)

# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱
# def mul(a, b):
#     print(a * b)

# mul(7, 8) # 56

# def mul(a, b):
#     return a * b

# print(mul(7,8)) # 56

# result = mul(7,8)
# print(result) #56

# 기본 값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용
# def mul(n1, n2=1):
#     return n1 * n2

# print(mul(1, 2)) # 2
# print(mul(1)) # 1

# 기본 값을 사용할 때 list는 사용 x 중복되기 때문
# def test_func(x, test=5):
#     test = test
#     print(x, test)

# test_func(1) # 1 5
# test_func(2) # 2 5

# def test_func2(x, test=None):
#     if test == None:
#         test = []
#     test.append(x)
#     print(x, test)

# test_func2(1) # 1 [1]

# 기본값이 있는 매개변수는 기본값이 없는 매개변수 뒤에 위치해야 함
# def sub(n1, n2=0, n3): # Error
# def sub(n1, n3, n2=0):
#     print(n1 - n2 - n3)

# 1 ~ 10까지 더한다
# *를 사용한 매개변수
# 입력값이 몇개가 될지 모를 때(안 정해졌을 때)
# add_many(1, 2) --> 3
# add_many(1, 2, 3, 4, 5) --> 15
# add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) --> 55
# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱, 슬라이싱
#     result = 0
#     for i in args:
#         result += i
#     return result

# result1 = add_many(1, 2, 3, 4, 5)
# print(result1) # 15
# result2 = add_many(3, 2, 5, 9, 1)
# print(result2) # 20
# result3 = add_many(1, 2)
# print(result3) # 3

# def calc_many(n1, *args):
#     result = n1
#     for i in args:
#         result += i
#     return n1

# 키워드 매개변수
# **kwargs
# keyword arguments
# 딕셔너리로 사용
def print_kwargs(**kwargs):
    print(kwargs)

# print_kwargs(a=1, b=2)
# print_kwargs(name='이름', age=10)

# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다.
def test_func5():
    print(1)
    print(2)
    return None
    print(3)
    print(4)
    print(5)
# 함수의 반환값은 무조건 1개이다.
# def test_func6(a, b):
#     # return (a + b, a * b)
#     return a + b, a * b
# result = test_func6(1, 2)
# res_add, res_mul = test_func6(1,2)
# # res_add, res_mul = (a+b, a*b)
# print(result)
# print(res_add,res_mul)

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True
#          짝수면 False
# def is_odd_number(n):
#    if n % 2 == 1:
#        return True
#    else :
#        return False
# print(is_odd_number(9)) # True

# def is_odd_number(n):
#    if n % 2 == 1:
#        return True
#    return False
# print(is_odd_number(8)) # False

# def is_odd_number(n):
#     return n % 2 == 1
# print(is_odd_number(7)) # True

# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해
# 테두리와 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None
# print 예시
# *****
# hello
# *****
# def ger_bordered_str(message):
#     message = str(message)
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
# ger_bordered_str("hello")
# ger_bordered_str(12345)

# 속도를 변환하는 함수
# m/s단위의 속도가 입력되면
# km/h단위의 속도로 변환한다.
# 함수이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도
# def convert_velocity(velocity):
    # 1m/s * 3600
    # 3600m/h
    # 3.6k/h
    # 1m/s ==> 3.6km/h
    # 초속 * 3600 / 1000 ==> 시속
    # 초속 * 3.6 ==> 시속
#     result = velocity * 3.6
#     return result
# print(convert_velocity(10)) # 36.0

# 별 찍기 함수
# 정수를 함수에 입력하여
# 호출하면 해당 정수 줄의
# 별을 화면에 출력한다.
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None
"""
출력 결과 n -> 4
*
**
***
****
"""
# def print_stars(n):
#     for i in range(n): # 0 ~ n-1
#         for j in range(i+1): # 0 ~ i
#             print("*", end="")
#         print()

# # def print_stars(n):
# #     i = 0
# #     while i < n:
# #         j = 0
# #         while j < i+1:
# #             print("*", end="")
# #         print()
# #         i += 1

# print_stars(4)






































