
x=10
under_20=x<20
print("under_20 : ",under_20)
print("not under_20 : ",not under_20)
print()


number = input("정수 입력 > ")
number = int(number)
if number > 0:
    print("양수입니다")
if number < 0:
    print("음수입니다")
if number == 0:
    print(" 0 입니다")
print()


import datetime
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    )
)


if now.hour < 12:
    print("현재시각은 {}시로 오전입니다".format(now.hour))
if now.hour > 12:
    print("오후입니다")
if now.hour == 12:
    print("오후 12시 입니다")


if now.month==1 or 2<=now.month <= 3:
        print("현재는{}월로 봄입니다".format(now.month))
if 4<= now.month <=6:
        print("현재는{}월로 여름입니다".format(now.month))
#if 7<= now.month <=9:
#        print("현재는{}월로 가을입니다".format(now.month))
if 10<= now.month <=12:
        print("현재는{}월로 겨울입니다".format(now.month))

if now.month == 7 or 8 or 9:
        print("현재는{}월로 가을입니다".format(now.month))



