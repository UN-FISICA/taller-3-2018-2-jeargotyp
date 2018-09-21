
# coding: utf-8

# In[91]:

num = 1.45655
split_num = str(num).split('.')
i = int(split_num[0])
i=str(i)
sx=list(map(int,i))
d = int(split_num[1])
d=str(d)
sd=list(map(int,d))

num1 = 1356.4555
split_num1 = str(num1).split('.')
i1 = int(split_num1[0])
i1=str(i1)
sx1=list(map(int,i1))
d1 = int(split_num1[1])
d1=str(d1)
sd1=list(map(int,d1))

if len(sx)>len(sx1):
    sx1=[0]*abs(len(sx)-len(sx1))+sx1
if len(sd)>len(sd1):
    sd1=sd1+[0]*abs(len(sd1)-len(sd))
if len(sx)<len(sx1):
    sx=[0]*abs(len(sx1)-len(sx))+sx
if len(sd)<len(sd1):
    sd=sd+[0]*abs(len(sd1)-len(sd))




for i in range(len(sx)):
    for j in range(i,len(sx)):
        sx[i],sx[j]=sx[j],sx[i]

s=sx


for i in range(len(sx1)):
    for j in range(i,len(sx1)):
        sx1[i],sx1[j]=sx1[j],sx1[i]
s1=sx1


#Parte decimal

for i in range(len(sd)):
    for j in range(i,len(sd)):
        sd[i],sd[j]=sd[j],sd[i]

sdec=sd


for i in range(len(sd1)):
    for j in range(i,len(sd1)):
        sd1[i],sd1[j]=sd1[j],sd1[i]
sdec1=sd1




#print(sdec1)



print(num+num1)


X=[]
for i in range(len(sx1)):
    
    
    
    
    if (s1[i]+s[i]+0)>=10:
        mm=0
        C1=s1[i]+s[i]
        C2=str(C1)
        C=list(map(int, C2))
        mm+=(C[0])
        t=mm
        X.append(C[len(C)-1])
            
    if (s1[i]+s[i])<10:
        
        X.append(s[i]+s1[i]+t)
        t=0
        
#Decimal part





for i in range(len(X)):
    for j in range(i,len(X)):
        X[i],X[j]=X[j],X[i]   

t1=(sx,sd)
t2=(sx1,sd1)


print(X)


# In[ ]:




# In[144]:

#parte entera
num = 1.45655
split_num = str(num).split('.')
i = int(split_num[0])
i=str(i)
sx=list(map(int,i))
d = int(split_num[1])
d=str(d)
sd=list(map(int,d))

num1 = 1356.4555
split_num1 = str(num1).split('.')
i1 = int(split_num1[0])
i1=str(i1)
sx1=list(map(int,i1))
d1 = int(split_num1[1])
d1=str(d1)
sd1=list(map(int,d1))

if len(sx)>len(sx1):
    sx1=[0]*abs(len(sx)-len(sx1))+sx1
if len(sd)>len(sd1):
    sd1=sd1+[0]*abs(len(sd1)-len(sd))
if len(sx)<len(sx1):
    sx=[0]*abs(len(sx1)-len(sx))+sx
if len(sd)<len(sd1):
    sd=sd+[0]*abs(len(sd1)-len(sd))




for i in range(len(sx)):
    for j in range(i,len(sx)):
        sx[i],sx[j]=sx[j],sx[i]

s=sx


for i in range(len(sx1)):
    for j in range(i,len(sx1)):
        sx1[i],sx1[j]=sx1[j],sx1[i]
s1=sx1


#Parte decimal

for i in range(len(sd)):
    for j in range(i,len(sd)):
        sd[i],sd[j]=sd[j],sd[i]

sdec=sd


for i in range(len(sd1)):
    for j in range(i,len(sd1)):
        sd1[i],sd1[j]=sd1[j],sd1[i]
sdec1=sd1




#print(sdec1)



print(num+num1)

Ki1=0
X=[]
for i in range(len(sx1)):
    
    
    
    
    if (s1[i]+s[i]+0)>=10:
        mm=0
        C1=s1[i]+s[i]
        C2=str(C1)
        C=list(map(int, C2))
        X.append(C[len(C)-1]+t)
        mm+=(C[0])
        t=mm
        
            
    if (s1[i]+s[i])<10:
        
        X.append(s[i]+s1[i]+t)
        t=0
        
#Decimal part





for i in range(len(X)):
    for j in range(i,len(X)):
        X[i],X[j]=X[j],X[i]   

t1=(sx,sd)
t2=(sx1,sd1)


print(X)


# In[143]:

#suma part decimal
num = 1.45655
split_num = str(num).split('.')
i = int(split_num[0])
i=str(i)
sx=list(map(int,i))
d = int(split_num[1])
d=str(d)
sd=list(map(int,d))

num1 = 1356.4555
split_num1 = str(num1).split('.')
i1 = int(split_num1[0])
i1=str(i1)
sx1=list(map(int,i1))
d1 = int(split_num1[1])
d1=str(d1)
sd1=list(map(int,d1))

if len(sx)>len(sx1):
    sx1=[0]*abs(len(sx)-len(sx1))+sx1
if len(sd)>len(sd1):
    sd1=sd1+[0]*abs(len(sd1)-len(sd))
if len(sx)<len(sx1):
    sx=[0]*abs(len(sx1)-len(sx))+sx
if len(sd)<len(sd1):
    sd=sd+[0]*abs(len(sd1)-len(sd))




for i in range(len(sx)):
    for j in range(i,len(sx)):
        sx[i],sx[j]=sx[j],sx[i]

s=sx


for i in range(len(sx1)):
    for j in range(i,len(sx1)):
        sx1[i],sx1[j]=sx1[j],sx1[i]
s1=sx1


#Parte decimal

for i in range(len(sd)):
    for j in range(i,len(sd)):
        sd[i],sd[j]=sd[j],sd[i]

sdec=sd


for i in range(len(sd1)):
    for j in range(i,len(sd1)):
        sd1[i],sd1[j]=sd1[j],sd1[i]
sdec1=sd1
Ki1=0
X1=[]   
for j in range(len(sd)):
    
    if (sdec1[j]+sdec[j])>=10:
        nn=0      
        C11=sdec1[j]+sdec[j]
        C22=str(C11)
        Cx=list(map(int, C22))
        X1.append(Cx[len(Cx)-1]+Ki1)
        nn+=(Cx[0])
        Ki1=nn
        
        
    
    elif (sdec1[j]+sdec[j])<10:
        
        X1.append(sdec[j]+sdec1[j]+Ki1)
        Ki1=0
    #print(Ki1)
        
for i in range(len(X1)):
    for j in range(i,len(X1)):
        X1[i],X1[j]=X1[j],X1[i]  



print(num+num1)
print(X1)


# In[ ]:

0.45655 
0.45550
-------
0.00005

