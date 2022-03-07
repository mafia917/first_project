from random import random


from random import *

users = range(1,21)
users = list(users) # 오오 이게 중요하다

shuffle(users) #섞기ddd


winners= sample(users,4) #4명 중에서 1명은 치킨 3명은 피자 주자





print(users)
print(winners)

print(" 당첨자 발표")
print("치킨: {0}".format(winners[0]))
print("커피: {0}".format(winners[1:4]))
print("축하")