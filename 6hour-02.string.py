sentence= '나는 소년입니다'
print(sentence)

sentence2 = '파이썬은 좃밥이야'
print(sentence2)

#여러줄?

sentence3= """
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)

jumin = "991122-1234567"

print("성별: "+ jumin[7])
print("연: " + jumin[0:2]) 



python= "Python is Amazing"
print(python.lower())
print(python.upper())

print(python[0].isupper())  #대문자냐?
print(len(python)) #길이
print(python.replace("Python","Java"))

index= python.index("n")  #index안에 문자 몇번쨰임?
print(index)
index = python.index("n", index + 1) #다음번 문자는 몇번째?
print(index)

print(python.find("n"))  #비슷한데

print(python.count("n")) # 몇개인지



#방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")  #" " 를 해줘야댐
print("Apple 은 %c로 시작해요." %"A") #(한글자)

