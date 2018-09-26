
# coding: utf-8

# In[4]:

#suma part decimal
num = 1980.0
split_num = str(num).split('.')
i = int(split_num[0])
i=str(i)
sx=list(map(int,i))
d = int(split_num[1])
d=str(d)
sd=list(map(int,d))

num1 = 29.0
split_num1 = str(num1).split('.')
i1 = int(split_num1[0])
i1=str(i1)
sx1=list(map(int,i1))
d1 = int(split_num1[1])
d1=str(d1)
sd1=list(map(int,d1))

num2 = num+num1
split_num2 = str(num2).split('.')
i2 = int(split_num2[0])
i2=str(i2)
sx2=list(map(int,i2))
d2 = int(split_num2[1])
d2=str(d2)
sd2=list(map(int,d2))

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

        
Sd=0
if (len(sd1)>len(sd)):
    if len(sd2)>len(sd1):
        Sd+=1
    if len(sd2)==len(sd):
        Sd+=0
    
else:
    if len(sd2)>len(sd):
        Sd+=1
    if len(sd2)==len(sd):
        Sd+=0


#Sd=0
t=0
z=0
X=[]

if(len(sx1)>len(sx)):
    
    for i in range(len(sx1)):
        
    
        if (s1[i]+s[i]+0)>=10:
            mm=0
            C1=s1[i]+s[i]+Sd
            C2=str(C1)
            C=list(map(int, C2))
            X.append(C[len(C)-1]+t)
            mm+=(C[0])
            t=mm
            Sd=0
        #print(t)
        
            
        elif (s1[i]+s[i])<10:
            if Sd!=0:
                carrysd=0
                carrys=s1[i]+s[i]+Sd+t
                carrys1=str(carrys)
                carr=list(map(int,carrys1))
                X.append(carr[len(carr)-1])
                carrysd+=carr[0]
                t=0
                Sd=carrysd
            else:
                X.append(s[i]+s1[i]+t)
                t=0
            #Sd=0
        
#Decimal part

else:
    for i in range(len(sx)):
        
        
    

    
        if (s1[i]+s[i]+0)>=10:
            mm=0
            C1=s1[i]+s[i]+Sd+t
            C2=str(C1)
            C=list(map(int, C2))
            X.append(C[len(C)-1])
            mm+=(C[0])
            t=mm
            z=0
            Sd=0
        #print(t)
        
            
        elif (s1[i]+s[i])<10:
            if Sd!=0:
                carrysd=0
                carrys=s1[i]+s[i]+Sd+t
                carrys1=str(carrys)
                carr=list(map(int,carrys1))
                X.append(carr[len(carr)-1])
                carrysd+=carr[0]
                t=0
                z=0
                Sd=carrysd
   
            else:
                k=0
                Cz=s1[i]+s[i]+Sd+t+z
                Cz=str(Cz)
                Czz=list(map(int, Cz))
                if len(Czz)==1:
                    Czz=[0]+Czz
                else:
                    Czz=Czz
                
                X.append(Czz[len(Czz)-1])
                k+=Czz[0]
                z=k
                t=0
                
           
                    
                #print(z)
                
if z!=0:
    X[len(X)-1]=X[len(X)-1]+z
           
else:
    X=X
    
    
for i in range(len(X)):
    for j in range(i,len(X)):
        X[i],X[j]=X[j],X[i]   
        
        
if (len(sx1)>len(sx)):
    if len(sx2)>len(sx1):
        X=[1]+X
    else:
        X=X
    
else:
    if len(sx2)>len(sx):
        X=[1]+X
    else:
        X=X
        

print(num1+num)
amalgama=(X,X1)
print(amalgama)


# In[ ]:



