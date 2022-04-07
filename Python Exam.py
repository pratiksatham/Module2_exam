#!/usr/bin/env python
# coding: utf-8

# In[16]:


for i in range (1,6):
    for j in range(1,i+1):
        print(j%2,end=" ")
    print()


# In[7]:


#Convert given hrs & mins in second 

hr=int(input("enter the number: "))
min=int(input("enter minutes: "))
sec=(hr*3600)+(min*60)
print(hr,"hours and",min,"minutes are totals",sec,"seconds")


# In[ ]:


#Write a code to accept a number & print
#in words


# In[18]:


n=int(input("enter the digit : "))
print("entered digit :",end=" " )
if n==0:
    print("zero")
elif n==1:
    print("one")
elif n==2:
    print("two")
elif n==3:
    print("three")
elif n==4:
    print("four")
elif n==5:
    print("five")
elif n==6:
    print("six")
elif n==7:
    print("seven")
elif n==8:
    print("eight")
elif n==9:
    print("nine")
else:
    print("not a digit : ")


# In[ ]:


#Accept String & print only alternate
#characters on a string


# In[13]:


p=input("enter the string: ")
print(p[1::2])


# In[ ]:


#Create menu driven code for
#1) Accept 2 numbers
#2) Add
#3) Sub
#4) Mul
#5) Div


# In[16]:


a1=float(input("enter the num"))
a2=float(input("enter the second number"))

print("enter which operation you want to perform?")
ch=input("Enter the specific operations")

result=0
if ch=="+":
    result=a1+a2
elif ch== "_":
    result=a1-a2
elif ch == "/":
    result==a1/a2
elif ch == "*":
    result==a1*a2
else:
    print("Invalid Output")

print(a1,ch,a2,':',result)


# In[ ]:


#Convert Paise in Rupees &
#Paises
#Ex: 350 is 3 Rupees 50 Paise
#3.50 print Rupees: 3
#Paise: 50


# In[17]:


p=100
rupees=int(input("enter the amount in rupees: "))
total=rupees*p
print(total,"paise")


# In[19]:


#Q.no.(8)

a="13567"
for i in range(0,len(a)):
    print(a[i]*(i+1))


# In[28]:


#Q.no(6) Q.6) Read file & count numbers of digit
#alphabets & symbols

a= input("enter the string ")
d=l=s=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
    print("letters",l)
    print("digits",a)
    print("Symbols",s)


# In[23]:


#Q.6

def function(n1,n2,n3,n4=0):
    if n4==0:
        sum=n1+n2+n3
        avg=sum/3
        return avg
    else:
        sum=n1+n2+n3+n4
        avg=sum/4
        return avg
    


# In[24]:


function(5,10,15)


# In[29]:


function(10,20,30,40)


# In[ ]:




