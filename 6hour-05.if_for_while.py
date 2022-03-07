# weather= "비"
# if weather =="비":
#     print("우산을 챙기시오")
    
    
# temp= int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
    
    
for waiting_no in [0,1,2,3,4]:
    print("대기번호: {0}".format(waiting_no))
    
print("----------------")
for waiting_no2 in range(5):
    print("대기번호: {0}".format(waiting_no2))
print("----------------")
for waiting_no2 in range(1,6):
    print("대기번호: {0}".format(waiting_no2))


star  = ["i","t", "iam"]
for customer in star:
    print("{0}".format(customer))
print("----------------")

#while
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer,index))
    index -=1
    if index ==0:
        print("커피는 폐기처분되었습니다.")
    