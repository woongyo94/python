# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
# print_3_times()
# print()

# for i in range(3):
#     print_3_times()
# ------------------------------------------
# def print_n_times(value,n):
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요",4)
# ---------------------------------------------
# def print_n_times(n,*values):
#     for i in range(n):
#         for value in values:
#             print(i,value)
#         print()
# print_n_times(3,"안녕하세요","즐거운","파이썬프로그래밍")
# --------------------------------------------------------
# def print_n_times(*values,n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times("안녕하세요","즐거운","파이썬",n=3)
# -----------------------------------------------------------
# def test(a,*values,b=10,c=100):
#     print(a+b+c)
#     for value in values:
#         print(value)

# #test(10,20,30)
# #test(a=10,b=100,c=200)
# #test(c=10,a=100,b=200)
# #test(10,c=200)
# test(10,"즐거운", "파이썬","프로그래밍",c=30)
# ---------------------------------------------------------------------
# a=int(input("첫번쨰 값 : "))
# b=int(input("두번쨰 값 : "))

# def sumA(start,end):
#     output=0
#     for i in range(start,end+1):
#         output += i
#     return output
# print(sumA(start=a,end=b))
# --------------------
def example(*A):
    C=1
    for i in A:
        C*=i
    return C
print(example(5,7,9,10))




    












