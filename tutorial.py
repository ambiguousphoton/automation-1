mylist = ['cherry', 'apple', 'mango']

mylist.insert(1,'banana')
mylist2 = list()

def rev(rlist,list ):
    x = 1   
    for i in list:
        rlist.append(list[len(list) - x])
        x = x + 1 
    
rev(mylist2,mylist)

print(mylist)

print(mylist2)