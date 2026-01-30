#Loops=It controls flow of structures that execute block of code repeatedly until desired condition is met.There are 3 types of Loops:
#1.While Loop 2.For Loop 3.Nested Loop

##1.While Loop - It repeatedly excutes the code as long as boolean expression is true(condition is true)
#i = 1
#while i <= 6:
     #print("College")
     #i = i + 1

##2.For Loop - repeated execution og a grouo of statments for the desired number of times.
#numbers = [1, 2,4, 6, 11, 20]  #sqr or n numbers
#seq = 0
#for val in numbers:
 #   seq = val * val
  #  print(seq)

##4. Nested Loops - When one loop is defined within another loop
for i in range(1,6):
    for j in range (5,i-1,-1):
      print(i,end="")
      print(' ')

  
