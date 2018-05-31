from stack import stack
from node import node

array=[]
file = input("Enter the filefile:  ") #file to be parsed
s = open(file, "r").read()

stk = stack()
linestk = stack()
line_Number = 0

for i in range(len(s)):
    if s[i] == "\n":
        line_Number+=1
    elif s[i] == "{":
        stk.push(i)
        linestk.push(line_Number)
    elif s[i] == "}":
        n = node()
        n.level = stk.length()
        n.start = stk.peek()
        n.text = s[stk.pop():i+1]
        if stk.length()==0:
            n.parent = 0
        else:
            n.parent = stk.peek()
        n.lineNum = linestk.pop()
        array.append(n)

def maxLevel(array):
    mx = 0
    for e in array:
        if e.level > mx:
            mx = e.level
    return mx
counter = 2
for j in range(1,maxLevel(array)+1):
    for e in array:
        if e.level == j:
            e.id = counter
            counter+=1
d={}
for element in array:
    if element.parent not in d:
        d[element.parent] = [element.id]
    else:
        d[element.parent].append(element.id)
    
#print(d)

List = {} #placeholder for numbers

for keys in d:
    if keys == 0:
        List[1] = d[keys]
    for ele in array:
        if keys == ele.start:
           List[ele.id] = d[keys]

#list for Control Flow

leaves = []
childToParent = {}
for key in List:
    for e in List[key]:
        childToParent[e] = key
        if e not in List:
            leaves.append(e)


for k in leaves: 
    toprint = [k]
    current = k
    while(current in childToParent): #parsed using nodes
        current = childToParent[current]
        toprint.append(current)

    toprint.reverse()
    for node in toprint:
        if node == toprint[-1]:
            print(node)
        else:
            print(node, end = "  ---> ")

        















