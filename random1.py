import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,200))
mylist=["jadu","aswh","virat","mahi"]
mylist1={"jadu","aswh","viru","mahi"}
print(random.choice(mylist))
print(random.choice(mylist1))
random.shuffle(mylist)
print(mylist)