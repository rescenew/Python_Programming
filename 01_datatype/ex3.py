# 불리언 타입(bool)

# a = True
# b = False
# print(a, type(a))
# print(b, type(b))

# print(2 < 3)
# print(2 > 3)
# print(2 == 3)
# print(2 != 3)

# print("apple" > "banana")
# print("apple" > "apble")
# print("apple" > "Apple")

# bool() 함수
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([10]))
print(bool([]))

# None 자료형
a = None
print(a, type(a))
print(bool(a))

if a is None:
    print("a is None, 값이 없습니다.")
