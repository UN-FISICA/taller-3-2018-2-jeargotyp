
# coding: utf-8

# In[48]:

def suma(i,i1):
    
    #i = int(split_num[0])
    #i=str(i)
    sx=i
    str1 = ''.join(str(e) for e in sx)
    #d = int(split_num[1])
    #d=str(d)
    #sd=list(map(int,d))
    
    #i1 = int(split_num1[0])
    #i1=str(i1)
    sx1=i1
    str2 = ''.join(str(e) for e in sx1)
    
    #d1 = int(split_num1[1])
    #d1=str(d1)
    #sd1=list(map(int,d1))
    num=int(str1)
    num1=int(str2)
    num2 = num+num1
    split_num2 = str(num2).split('.')
    i2 = int(split_num2[0])
    i2=str(i2)
    sx2=list(map(int,i2))
    #d2 = int(split_num2[1])
    #d2=str(d2)
    #sd2=list(map(int,d2))

    if len(sx)>len(sx1):
        sx1=[0]*abs(len(sx)-len(sx1))+sx1
    #if len(sd)>len(sd1):
     #   sd1=sd1+[0]*abs(len(sd1)-len(sd))
    if len(sx)<len(sx1):
        sx=[0]*abs(len(sx1)-len(sx))+sx
    #if len(sd)<len(sd1):
      #  sd=sd+[0]*abs(len(sd1)-len(sd))



    for i in range(len(sx)):
        for j in range(i,len(sx)):
            sx[i],sx[j]=sx[j],sx[i]

    s=sx


    for i in range(len(sx1)):
        for j in range(i,len(sx1)):
            sx1[i],sx1[j]=sx1[j],sx1[i]
    s1=sx1


#Parte decimal

    #for i in range(len(sd)):
        #for j in range(i,len(sd)):
            #sd[i],sd[j]=sd[j],sd[i]

    #sdec=sd


    #for i in range(len(sd1)):
    #    for j in range(i,len(sd1)):
     #       sd1[i],sd1[j]=sd1[j],sd1[i]
    #sdec1=sd1
    Ki1=0
    X1=[]   
    #for j in range(len(sd)):
    
     #   if (sdec1[j]+sdec[j])>=10:
     #       nn=0      
     #       C11=sdec1[j]+sdec[j]
     #       C22=str(C11)
     #       Cx=list(map(int, C22))
     #       X1.append(Cx[len(Cx)-1]+Ki1)
     #       nn+=(Cx[0])
     #       Ki1=nn
        
        
    
      #  elif (sdec1[j]+sdec[j])<10:
        
       #     X1.append(sdec[j]+sdec1[j]+Ki1)
        #    Ki1=0
    #print(Ki1)
        
    #for i in range(len(X1)):
     #   for j in range(i,len(X1)):
      #      X1[i],X1[j]=X1[j],X1[i]  

        
    #Sd=0
    #if (len(sd1)>len(sd)):
       # if len(sd2)>len(sd1):
       #     Sd+=1
       # if len(sd2)==len(sd):
      #      Sd+=0
    
    #else:
      #  if len(sd2)>len(sd):
      #      Sd+=1
       # if len(sd2)==len(sd):
         #   Sd+=0


    Sd=0
    t=0
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
        
            
            if (s1[i]+s[i])<10:
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
                C1=s1[i]+s[i]+Sd
                C2=str(C1)
                C=list(map(int, C2))
                X.append(C[len(C)-1]+t)
                mm+=(C[0])
                t=mm
                Sd=0
        #print(t)
        
            
            if (s1[i]+s[i])<10:
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
        
    
    return(X)
    
    
    
    
    
    
    

num = 1994.11
split_num = str(num).split('.')
i = int(split_num[0])
i= str(i)
sx=list(map(int,i))
d = int(split_num[1])
d=str(d)
sd=list(map(int,d))

num1 = 10.12
split_num1 = str(num1).split('.')
i1 = int(split_num1[0])
i1=str(i1)
sx1=list(map(int,i1))
d1 = int(split_num1[1])
d1=str(d1)
sd1=list(map(int,d1))
#sx= largo
#sx1=corto
for i in range(len(sx)):
    for j in range(i,len(sx)):
        sx[i],sx[j]=sx[j],sx[i]

s=sx


for i in range(len(sx1)):
    for j in range(i,len(sx1)):
        sx1[i],sx1[j]=sx1[j],sx1[i]
s1=sx1

#s=largo
#s1=corto

v=0
t=0
Mul=[]
for i in range(len(sx1)):
    for j in range(len(sx)):
        if (s1[i]*s[j])>=10:
            carry=0
            C1=s1[i]*s[j]+v+t
            C2=str(C1)
            C=list(map(int, C2))
            Mul.append(C[len(C)-1])
            carry+=C[0]
            t=carry
            v=0
        else:
            carry2=0
            C3=s1[i]*s[j]+t+v
            C3=str(C3)
            C4=list(map(int,C3))
            Mul.append(C4[len(C4)-1])
            carry2+=C4[0]
            v=0
            t=0
            
        

        

#print(Mul)        
for i in range(len(Mul)):
    for j in range(i,len(Mul)):
        Mul[i],Mul[j]=Mul[j],Mul[i]        



#print(Mul)

P1=[]
P2=[]
for i in range(int(len(Mul)/2)):
    P1.append(Mul[i])


P1=P1+[0]
for i in range(int(len(Mul)/2),len(Mul)):
    P2.append(Mul[i])
P2=[0]+P2

#print(P1)

#print(P2)

Huntermm=suma(P1,P2)
print(num,'x',num1)
print(Huntermm)




# In[ ]:




# In[ ]:



