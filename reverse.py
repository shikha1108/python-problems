l=[1,2,3,4,5]

def reverse_list(l):
    l2=[]
    for x in range(0,len(l)):
        current = l[len(l)-x-1]
        l2.append(current)
    print("added element in l2")
    return l2
    
print(reverse_list(l))


print(len(l))


total = 0

list1 = [11, 5, 17, 18, 23]

for x in range(0, len(list1)):
    total = total + list1[x]

print("Sum of all elements in given list: ", total)

l.reverse()
print(l)
