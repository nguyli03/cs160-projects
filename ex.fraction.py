class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    def __str__(self):
        common=gcd(self.num, self.den)
        return str(self.num//common)+'/'+str(self.den//common)
       
     
    def __add__(self, otherfraction):
        newnum=self.num*otherfraction.den + otherfraction.num*self.den
        newden=self.den*otherfraction.den
        return Fraction(newnum,newden)
    def __multiply__(self, otherfraction):
        newnum=self.num*otherfraction.num
        newden=self.den*otherfraction.den
        return Fraction(newnum,newden)
    def __divide__(self, otherfraction):
        newnum=self.num*otherfraction.den
        newden=self.den*otherfraction.num
        return Fraction(newnum,newden)
    def __subtract__(self, otherfraction):
        newnum=self.num*otherfraction.den - otherfraction.num*self.den
        newden=self.den*otherfraction.den
        return Fraction(newnum,newden)
    
    def __comparision__(self,otherfraction):
        newnum=self.num*otherfraction.den-otherfraction.num*self.den
        newden=self.den*otherfraction.den
        common=gcd(newnum,newden)
        if newnum//common>0:
            return str(Fraction(self.num,self.den))+' is bigger'
        elif newnum//common<0:
            return str(Fraction(otherfraction.num,otherfraction.den))+' is bigger'
        else:
            return "these fractions are equal"
def gcd(m,n):
    while m%n!=0:
        oldm=m
        oldn=n
        m=oldn
        n=oldm%oldn
    return n
def main():
    m=int(input('please enter a number to be the numerator for the first fraction:'))
    n=int(input('please enter a number to be the denumerator for the first fraction:'))
    h=int(input('please enter a number to be the numerator for the second fraction:'))
    k=int(input('please enter a number to be the denumerator for the second fraction:'))
    common=gcd(m,n)
    if n==0 or k ==0:
        raise RuntimeError('these numbers must be different from 0')
    else:
        x=Fraction(m,n)
        y=Fraction(h,k)
        z=x.__add__(y)
        l=x.__subtract__(y)
        print(x.__comparision__(y))
        print(z,l,common)
if __name__=='__main__':
    main()