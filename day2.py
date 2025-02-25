#---1

fullname =input()
letr =input()
indexs=[]
for index ,let in enumerate(fullname):
    if let ==letr:
        indexs.append(index)
print(indexs)


#--2
num = int(input("Enter a number: "))  
indexs = []  
count = 1
for count in range(1,num):
    var=1
    l = [] 
    for var in (1,count):
        result = var * count
        l.append(result)  
    indexs.append(l)  
    count += 1  
print(indexs)


# #-------------3
list=eval(input("enter your name :"))

dic ={}
list=["felopater","hamdy","moham"]
let =0
list.append(input)

while let < len(list):
    dic[list[let][0]] =list[let]
    let +=1


print(dic)
