#DAY1--->13/03/23
#Multiplication
#Q1
'''num=int(input("Enter a number"))
print(number,type(number))
if number%3==0 and number%5==0:
     print("it is a multiple of both")
elif number%5==0:
      print("it is a multiple of 5")
elif number%3==0:
     print("it is a multiple of 3")
else:
     print("invalid")'''


#Q2
'''for i in range(1,101):
   print(i,end='')'''

#Q3
'''for i in range(100,0,-1):
    print(i,end='')
print()'''

#Q4
'''#99 97......1
for i in range(99,0,-2):
    print(i,end='')
print()'''

#Q5
'''#break
for i in range(1,101):
    if i==50:
       break
    print(i,end=" ")'''

#Q6
'''#continue
for i in range(1,101):
    if i==50:
          continue
    print(i,end=" ")'''

#Q7
'''for i in range(1,101):
    if i==50:
          continue
    print(i,end=" ")
for i in range(1,101):
    if i==50:
        pass
    print(i,end="")'''

#Q8
#Functions
'''def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
function2(10,20) '''

#Q9
'''def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function3(10,20.2))
def function4(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function4(10,20.2))
def function5(num1,num2):
    num3=float(num1)+num2
    return num3
print("value returned",function5('10',20.2))'''


#Q10
#positional argument
'''def function1 (num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,"200",300,400)'''

#Q11
#keyword arguments
'''def function2 (num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=20,num2=10,num3=40)'''

#Q12
#default arguments
'''def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("Swikruti",42,"CSE")
function3("Shraddha",34,"ECE")
function3("Supriya",36,"CST")
function3("Sweeta",29,"CST")'''

#Q13
'''def function3(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("Swikruti",42,)
function3("Shraddha",34,"ECE")
function3("Supriya",36,"CST")
function3("Sweeta",29,"CST")'''

#Q14
#Variable number of arguments
'''def function4(*var):
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)'''

#Q15
'''def function4(*var):
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)


def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
        return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))'''

#Q16
'''n_adults=int(input("Enter the number of adults"))
n_childs=int(input("Enter the number of childs"))
total=((n_adults*37550.0)+(n_childs*37550.0))
print(total)
total1=total*0.07
total2=total+total1
print("with ur service tax",total2)
total_amount=total2*0.90
print(total_amount)'''







#DAY2--->14/03/23
#Q1
#list
'''list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=(10,20.2,20+3j,True,"PYTHON")
print(list3,type(list3))
list4=list([10,30,40,50])
print(list4,type(list4))
list5=[101,102,103,104,105]
print(list5,type(list5))
list5.append(501)
print(list5,type(list5))
list5.extend([601,701,801])
print(list5,type(list5))
list5.insert(0,51)
print(list5,type(list5))
list5.remove(801)
print(list5,type(list5))
list5.pop()
print(list5,type(list5))
list5.pop(0)'''



#Q2
'''def function (str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[l_count,d_count]
print(function("Infosysis"))
print(function("ABCDEFG"))'''      
    

#Q3
'''def fun(marks):
    sum=0
    count=0
    for i in marks:
        sum=sum+i
        avg=sum/10
    for j in marks:    
        if j>avg:
              count+=1
              per=(count/10)*100
        return per
marks=[13,15,17,10,12,8,5,9,4,2]
print(fun(marks))

def sort_marks(marks):
    marks=sorted(marks)
    return marks
def generate_frequency(marks):
    freq=[]
    for x in range(26):
        count=0
        for y in marks:
            if x == y:
                 count+=1
        freq.append(count)
    return freq

print(generate_frequency(marks))
print(sort_marks(marks))'''

#Q4
#Dictionary
'''def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict[i])
    return list2    
dict1={"merry":"god","christmas":"jul","and":"och"," happy":"gott","new":"nytt","year":"ar"} 
list1=["merry","christmas"]
print(translate(list1,dict1))'''

#Q5
#list comprehension
'''n1=int(input("enter a value for n1"))
n2=int(input("enter a value for n2"))
result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)

array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result) '''





             
#DAY3--->Date:15/03/23
#Python Programs


#list comprehension
#for loop version
'''result=[]
for i in range(11):
    result.append(i)
print(result)'''

#list comprehension version
'''print([i for i in range(11)])'''

#list coomprehension-->odd element
'''result=[]
for i in range(11):
      if i%2!=0:
         result.append(i)
      
print(result)
print([i for i in range(11) if i%2!=0])'''

#list comprehension -->even element
'''result=[]
for i in range(11):
      if i%2!=0:
         result.append(i)
      else:
          result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])'''


#list comprehension-->odd element-->square it
                      #even element-->cube it
#Q1
#odd element:-->Square it
'''result=[]
for i in range(11):
    if i%2!=0:
        result.append(i*i)
print(result)        
print=([i*i for i in range(11) if i%2!=0])'''

#Even element:
'''result=[]
for i in range(11):
    if i%2==0:
        result.append(i*i*i)
    
print(result)
print([i*i*i for i in range(11) if i%2==0])'''


'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    for ele in row:
        if ele%2!=0:
            result.append(ele**2)
        else:
             result.append(ele**3)
print(result)'''


'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)'''     



#list comprehension
'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([ele**2 if ele%2!=0 else ele**3 for row in mat for ele in row])'''

#Dynamic 
'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[ele**2 if ele%2!=0 else ele**3 for ele in row]for row in mat])'''


#Question2
'''mylist=[9,3,6,1,5,0,8,2,4]
list_b=[6,4,6,1,2,2]

result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)'''

#list comprehension(Q2)
'''mylist=[9,3,6,1,5,0,8,2,4]
list_b=[6,4,6,1,2,2]
result=[]
print([(i,mylist.index(i))for i in list_b])'''


#Dictionary comprehension(extra)
''''mylist=[9,3,6,1,5,0,8,2,4]
list_b=[6,4,6,1,2,2]
myDict = {mylist:list_b for(mylist,list_b) in zip(mylist, list_b)}
print(myDict)'''

#Dictionary comprehension (Q2)

'''mylist=[9,3,6,1,5,0,8,2,4]
list_b=[6,4,6,1,2,2]
result=[]
print({i:mylist.index(i) for i in list_b})'''



#Question3
'''sentences = ["a new world record was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simulateneously on the banks of the sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']
result=[]
for i in sentences:
    row_data=[]
    for word in i.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)'''    

#Question4
'''array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=" "
for i in l:
    number2+=str(i)
print(int(number2)+number1)'''

#Question5
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))

#Question6
    


    
    
    
                    
          
          


















  
 
  































    
