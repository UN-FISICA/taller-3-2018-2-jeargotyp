
# coding: utf-8

# In[16]:

class MyFloat:

    def __init__(self,pi):
        self.pi=pi
        
    def __add__(self,other):
        return MyFloat(other+self.pi)

    def __sub__(self,other):
        return MyFloat(self.pi-other)

    def __mul__(self,other):
        return MyFloat(other*self.pi)
    #truediv para python 3 o div por python 2
    def __truediv__(self,other):
        return MyFloat(self.pi/other) 
    
    def __radd__(self,other):
        res=self+other
        return res
    def __rsub__(self,other):
        res=other-self.pi
        return res

    def __rmul__(self,other):
        muls=self.pi*other
        return muls

    def __rtruediv__(self,other):
        divs=other/self.pi
        return divs

    def __str__(self):
        return '{0:.30f}'.format(self.pi)

    def __repr__(self):
        return '{0:.30f}'.format(self.pi)

    def __eq__(self,other):
        if type(self.pi)==int or type(self.pi)==float:
            return self.pi
       
    def __ne__(self,other):
        if self.pi!=other:
            return self.pi
        
        
        
    
if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    pi=MyFloat(0)
    for k in range(0,100000):
        pi+=4*(-1)**(k)/(2*k+1)
    print(pi)


# In[ ]:




# In[ ]:



