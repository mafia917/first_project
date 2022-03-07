# cabinet= {3:"유재석", 100:"김태호"}
# print(cabinet[100])

# print(cabinet.get(3))

# print(cabinet.get(5,"사용 가능")) #휘발성
# print(cabinet.get(5)) #none


# print( 3 in cabinet) # ture
# print( 5 in cabinet) # X

# cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet2["A-3"])

# #새손님
# cabinet2["C-20"] ="조세호"

# print(cabinet2.get("C-20"))
# print(cabinet2)

menu=("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")

name="김종국"
age=20
hobby="코딩"
print(name,age,hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합 set
#중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java= {"u", "k" , "y"}
python=set(["u","p"])

#교집합
print(java & python)
print(java.intersection(python)) #동일

#합집함 
print(java | python)
print(java.union(python)) #동일

#차집합 (java 할 수 있지만 python 은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python)) #동일

#python을 할줄 아는 사람이 늘어남
python.add("k")
print(python)


list
tuple
set 