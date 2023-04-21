# tuple(튜플)형
# 튜플은 element의 값을
# 수정할 수 없다.
# mutable(=변하는) / immutable(=불변하는)
# mutable 수정 가능한
# list, dict
# immutable 수정 불가능
# int, float, str, tuple
my_list = [1, 2, 3]
my_list[0] = 5
# print(my_list)

# my_tuple = (1, 2, 3)
# my_tuple[0] = 5 # Error 튜플형은 수정 불가능
# print(my_tuple)
tuple_1 = ("Hello", "world", "python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3
t5 = (1, 2, (3, 4, 5))

t6 = tuple_1 + t2
t7 = t3 * 3

t3 = (1, 2, "Hello")
print(t3[2])
print(t3[0:2])
print(len(t3))

# t5 = (1, 2, (3, 4, 5))
# print(t5[2][1])

# t8 = (5, 3, 1, 4, 2)
# for i in t8:
#     print(i)
















