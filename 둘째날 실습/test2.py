format_a="{}만 원".format(5000)
format_b="파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c="{} {} {}".format(3000, 4000, 5000)
format_d="{}{}".format(1, " 문자열 ", True)
print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()
output_b = "{:=+015.4f}".format(-52.456)
print(output_b)
print()
output_a=-52.0
output_b="{:=+015g}".format(output_a)
print(output_b)
print()
a="hi my name is LimJaeWoong"
print(a.upper())
print(a.lower())
print()



input_a = """
       안녕하세요
            문자열의 함수를
    알아    
           봅시다
"""
print(input_a.strip())
print()

a="10, 20, 30, 40, 50".split(", ")
print(a)
print()

a = input("> 1번째 숫자 : ")
b = input("> 2번째 숫자 : ")

print("{} + {} = {}".format(a ,b, int(a)+int(b)))


