
# coding: utf-8

# In[16]:

def cnd(a):
    inte=int(a//1)
    deci=a%1
    k1=list(str(inte))
    c=list(str(deci))
    m=[]
    for k in range(len(c)):
        if c[k]=='.':
            pass
        else:
            m.append(c[k])
    if m[0]=='0':
        m.pop(0)
    if len(m)==0:
        m.append(0)
    
    x1=[]
    v2=[]
    for v in range(0,len(k1)):
        v2.append(int(k1[v]) )
    
    for i in range(len(m)):
        x1.append(int(m[i]))
    

    tup=(v2,x1)
    return tup
def suma(x,y):
        
        a=x[1][::]
        b=y[1][::]
        c=x[0][::-1]
        d=y[0][::-1]
        
        nd=max(len(a),len(b))
        red=0
        rs=[]
        
        for i in range(nd-1,-1,-1):
            
            if i>=len(a):
                na=0
            else:
                na=a[i]
        
            if i>=len(b):
                nb=0
            else:
                nb=b[i]
        
            
            s=na+nb+red
            if s<10:
                red=0
            else:
                red=1
            
            rs.append(s%10)
        
        rs.reverse()
        
       
        
        nmax=max(len(c),len(d))
       
        rent=[]
        
        for j in range(nmax):
            if j>=len(c):
                na=0
            else:
                na=c[j]
        
            if j>=len(d):
                nb=0
            else:
                nb=d[j]
        
            
            s2=na+nb+red
            if s2<10:
                red=0
            else:
                red=1
            
            rent.append(s2%10)
            
        if red==1:
            rent.append(1)
            
        rent.reverse()
        
        
        return rent,rs 
    

def Sum(x,y):
    a=x[::-1]
    b=y[::-1]
    nd=max(len(a),len(b))
    red=0
    rs=[]
    for i in range(nd):
        na=0 if i>=len(a) else a[i]
        nb=0 if i>=len(b) else b[i]
        s=na+nb+red
        red=0 if s<10 else 1
        rs.append(s%10)
    if red==1:
        rs.append(1)
    rs.reverse()
    return rs
def multiplicacion(a, b):
    ca=[0]+a[0]+a[1]
    cb=[0]+b[0]+b[1]
             
    ca.reverse()
    cb.reverse()
    res=0
             
    suma=[0]
    for i in range(len(cb)-1):
        P=[]
        for j in range(len(ca)):
            x=cb[i]*ca[j]+res
            P.append(x%10)
            res=int(x/10)
              
        Pd=i*[0]+P
        Pd.reverse()
              
        suma=Sum(suma,Pd)
                 
              
    p=len(suma)-1-len(a[1])-len(b[1])
    PZ=[]
    PD=[]
    for k in range(len(suma)):
        if k<=p:
            PZ.append(suma[k])
        else:
            PD.append(suma[k]) 
                                    
    if PZ[0]==0:
        PZ.pop(0)
    prod=PZ,PD
              
    return prod 

def resta1(x,y):
    return abs(x-y)

def imprimir(a):
    e,d=a
    r=""
    for i in range(len(e)):
        r=r+str(e[i])  
    r=r+"."
    for i in d:
        r=r+str(i)
    return r 

def imp(x):
    r=''
    for i in range(len(x)):
        r=r+str(x[i])

    return int(r)
def imp1(x):
    r=''
    for i in range(len(x)):
        r=r+str(x[i])

    return r

def fun(x,y):
    z=x+y
    return z

def division(a,b):
    md=max(len(a[1]),len(b[1]))
    if len(a[1])==md:
        cca=a[0]+a[1]
    else:
        cca=a[0]+a[1]+[0]*(md-len(a[1]))
    if len(b[1])==md:
        ccb=b[0]+b[1]
    else:
        ccb=b[0]+b[1]+[0]*(md-len(b[1]))
    if len(cca)!=len(ccb):
        if len(cca)>len(ccb):
            ccb=ccb+[0]*abs((len(ccb)-len(cca)))
        else:
            cca=cca+[0]*abs((len(ccb)-len(cca)))


    mn=min(len(cca),len(ccb))
    div=[]
    k=[]
    for i in range(mn):
        k.append(cca[i])
    q=[]
    if len(cca)!=len(ccb):
        for i in range(mn,max(len(ccb),len(cca))):
            q.append(cca[i])
    else:
        for i in range(0,mn):
            q.append(0)
        
    precision=29    
    for j in range(0,(len(cca))-len(ccb)+precision):  
        dib=int(imp(k)/imp(ccb))
        div.append(dib)
        qui=resta1(imp(k),dib*imp(ccb))
        qui1=[int(x) for x in str(qui)]
        añ=fun(qui1,[q[j]]) #lista
        iqui=imp(añ)
        q.append(0)
        k=añ
        
    ent=[]
    if len(a[0])>len(b[0]):
        x=len(a[0])-len(b[0])+1
    else:
        x=1
        div=[0]*(len(b[0])-len(a[0]))+div

    
    for i in range(0,x):
        ent.append(div[i])

    dec=[]
    for i in range(x,len(div)):
        dec.append(div[i]) 
    total=ent,dec
    return ent,dec
def resta(a, b):
    me=[0]+b[0]
    md=[1]+b[1]
    me.pop(0)
    md.pop(0)
    m=me,md
    le=[0]+a[0]
    ld=[1]+a[1]
    le.pop(0)
    ld.pop(0)
    l=le,ld

    ea,da=l
    eb,db=m

    ea.reverse()
    eb.reverse()
    
    
    if len(ea)<len(eb):        
        for i in range(len(eb)-len(ea)):
            ea.append(0)
    elif len(eb)<len(ea):
        for i in range(len(ea)-len(eb)):
            eb.append(0)
    if len(da)<len(db):         
        for i in range(len(db)-len(da)):
            da.append(0)
    elif len(db)<len(da):
        for i in range(len(da)-len(db)):
            db.append(0)
        
    da.reverse()
    db.reverse()
    ca=da+ea
    cb=db+eb
 
        
    for i in range(len(ca)-1,-1,-1): 
        if ca[i]<cb[i]:
            c=cb
            d=ca
            sig="-"
            bolen=1
            break
        elif ca[i]>cb[i]:
            c=ca
            d=cb
            sig="+"
            bolen=1
            break
        else:
            bolen=2
        
        
    if bolen==2: 
        sig="+"
        r=[0]
        er=[0] 
           
           
    else:
        r=[]
        for i in range(len(c)):                 
            if c[i]<d[i]:
                
                if c[i+1]!=0:
                    c[i+1]=c[i+1]-1     
                else:
                    c[i+1]=9
                    for k in range(i+2,len(c)):
                        if c[k]==0:
                            c[k]=9
                        else:
                            c[k]=c[k]-1
                            break
                   
                   
                r.append(10+c[i]-d[i])
            else:
                r.append(c[i]-d[i])
        
            
        r.reverse() 
          
        er=[]
        for z in range(len(r)-len(da)):
            er.append(r[0])
            r.pop(0)
               
        for q in range(len(er)):
            if er[0]==0:
                del er[0]
                   
            else:
                break
        if er==[]:
            er=[0]
        
    return er,r 

def comparacion(a,b):
    x=0
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            if a[i][j]==b[i][j]:
                x+=1
    if (len(a[1])+len(a[0]))!=x:
        return False
    else:
        return a==b

class MyFloat:

    def __init__(self,pi):
        self.pi=pi
        if type(self.pi)==int or type(self.pi)==float:
            self.pi=cnd(pi)
        else:
            self.pi=pi
  
    def __add__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        return MyFloat(suma(self.pi,other))

    def __sub__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        return MyFloat(resta(self.pi,other))

    def __mul__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        
        return MyFloat(multiplicacion(other,self.pi))
    #truediv para python 3
    def __truediv__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        
        return MyFloat(division(self.pi,other))
    
    def __radd__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
            x=MyFloat(suma(self.pi,other))
        
        return x
        
        
    def __rsub__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        res=MyFloat(resta(other,self.pi))
        return res

    def __rmul__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        muls=MyFloat(multiplicacion(self.pi,other))
        return muls

    def __rtruediv__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        divs=MyFloat(division(other,self.pi))
        return divs

    def __str__(self):
        return '{}'.format(self.pi)

    def __repr__(self):
        return '{}'.format(self.pi)

    def __eq__(self,other):
        if type(other)==int or type(other)==float:
            other=cnd(other)
        c=comparacion(self.pi,other)
        return c
       
    def __ne__(self,other):
        if comparacion(self.pi,other)==False:
            return 0
    def __getitem__(self, key):
        return self.pi[key]
    #def __setitem__(self, key):
    #self.pi.bricksId[key] = pi
        
        
        
    
if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    x=0
    for m in range(0,10000):
        if m%2==0:
            x=x+4/(2*MyFloat(m)+1)   
        else:
            x=x-4/(2*MyFloat(m)+1)
   
    print(imprimir(x))

    
       
    


# In[ ]:



