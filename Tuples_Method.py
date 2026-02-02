#Tuple is an ordered, heterogenous and immutable collection of elements.
#Tuple = ()
##Methods of Tuple
#1.count()
t = (10,20,30,20)
print(t.count(20))

#2.index()
t = (10,20,30,20)
print(t.index(20))


##Functions
t = (1,2,3)
print(all(t))

t = (0,0,0)
print(any(t))

t = (10,20,30)
print(max(t))
print(min(t))

t = (30,10,20)
print(sorted(t))

t = (10,20,30)
print(sum(t))

l = [10,20,30]
t =tuple(l)
print(t)

t = ('a','b','c')
print(list(enumerate(t)))
