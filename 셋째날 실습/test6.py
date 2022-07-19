# -----------------------------for문-------------------------------------------
# element = [1,5,4,3,2]
# ab = [1,2,3,4]
# for cd in ab:
#     #print(element)
#     #print(cd)
#     for i in range(3):
#           print(cd)



# # for i in range(3):
# #     print(ab)
# #     print(array)
# -----------------------------dictionary-------------------------------------------
# dict_b = {
#     "director" : ["안소니루소","조루소"],
#     "cast" : ['아이언맨', "타노스", "토르"]
# }

# print(dict_b)
# print("director = ",dict_b["director"])
# print("cast = ",dict_b["cast"])
# print(dict_b["director"][1])
# ------------------------------------------------------------------------
name = "name"
dic_c = {
    name : '홍길동 김기영 jaewoong',
    'age' : 29
}
print (dic_c)
del dic_c['age']
print (dic_c)


key = input(" > 접근하고자 하는 키 : ")
if key in dic_c:   
    print(dic_c[key])
else:
    print("존재x")



