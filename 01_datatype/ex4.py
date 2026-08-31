# 문자열(str)
# ""(권장), ''

# a = "python"
# print(a, type(a))

# print("I'll be back")
# print("I'll be back")

# 여러줄 문자열
# a = """
# Life is short
# You need python
# """
# print(a)

# a = """Life is short
# You need python"""
# print(a)


# def func():
#     x = 1
#     """
#     func() 함수에 대한 설명 작성
#     """
#     pass


# print(func.__doc__)

# 문자열 연결
# print("fuck u" + " World")

# 문자열 반복
# print("fuck u" * 30)

# print("*" * 30)

# 문자열 연산 시 주의사항
# print("Hello" + 3)
# print("Hello" + str(3))

# print("10" + "2")  # 102
# print(int("10") + int("2"))

# 문자열 포맷팅 (f-string)
#
pi = 3.141592653589793
print(f"원주율: {pi:.3f}")  # 원주율: 3.142
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")
