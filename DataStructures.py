#lists
x = [1,2,3,4,5]
print(x[0])
#list contains any type of data
xx = ["satya",1,1.5,[3,2]]
print(xx[3])
len(xx)#lentgth of list
xx.insert(1,"tome")#to insert to list
# to  remove any element from list
print(xx)
xx.remove("tome")
print(xx)
xx.pop()# to remove last element
print(xx)
#to sort all the elements in a list
xx.sort()
print(xx)
# to reverse all the value
xx.reverse()
print(xx)
xx.append(100)
s= xx.copy() # ti will coompy all the values in a list
print(s)
s.count(2)# it will count how many two are in a list
#to remove all the values in a list
xx.clear()
print(xx)
