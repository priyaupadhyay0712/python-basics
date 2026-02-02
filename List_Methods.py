#List is an ordered, mutable collection of elements that can hold various datatypes.
#Operatios In List Using List Methods And Functions.
#List = []

##Methods
#Creating a List
l = [10,20,30,40]
print(l)

#1.append()
l = [1,2,3]
l.append(4)
print(l)

#2.extend()
l = [1,2]
l.extend([3,4])
print(l)

#3.insert()
l = [10,20,30]
l.insert(1,15)
print(l)

#4.remove()
l =[10,20,30,20]
l.remove(20)
print(l)

#5.pop()
l = [10,20,30]
l.pop()
print(l)

#6.sort()
l = [4,1,3,2]
l.sort()
print(l)

#7.reverse()
l = [1,2,3]
l.reverse()
print(l)

#8.count(), 9.index()
l = [10,20,10,30]
print(l.count(10))
print(l.index(30))

##Functions
#len(),sum(),max(),min(),sorted()
l = [10,20,50,30]
print(len(l))
print(sum(l))
print(max(l))
print(min(l))
print(sorted(l))

