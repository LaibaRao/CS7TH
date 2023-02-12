#DICTIONARY

a={"name":"laiba",
   "roll":"9",
   "marks":[91,85,84]}

       #dictionary methods

#items()
print(a.items())

#keys()
print(a.keys)

#update()
print(a.update({"city":"bwp"}))
print(a)

#get()
print(a.get("roll"))



#SETS


S={0,1,4}
#methods of sets

#add()
print(S.add(7))


       #Operations of sets

#len()
print(len(S))

#remove()
print(S.remove(1))

#pop()
print(S.pop())

#clear
print(S.clear())

#union()
print(S.union({4,8}))

#intersection()
print(S.intersection({4,8}))



#CONDTIONAL STATEMENTS

    #if and else

x=10
if(x>7):
       print("greater")
else:
 print("lesser")


     #elif

a=50
b=50
if(a>b):
       print("a is greater")
elif(a<b):
       print("a is smaller than b")
else:
       print("a and b are same")


#LOOPS 

     #while loop

i=0
while i<5:
       print(i)
       i=i+1


      #for loop
list=[1,2,3,4,5,"ayesha"]
for item in list:
       print(list)
     #range() function in for loop
for i in range (0,10):
       print(i)


     #break statement
for i in range (0,10):
       print(i)
       if i==7:
              break  

        #continue statement 
for i in range (0,10):
       print(i)
       if i==2:
             continue 
       print(i) 



#FUNCTIONS

def Sum(a,b):
       return a+b
       
Sum(5,40) 
print(Sum)

