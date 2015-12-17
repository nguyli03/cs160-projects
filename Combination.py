def Combination(m,n):
    if m==n or n==0:
        return 1
    else:
        return Combination(m-1,n-1)+Combination(m-1,n)
def main():
    print(str(Combination(10,3)))
    print(str(Combination(7,3)))
    print(str(Combination(5,1)))
    print(str(Combination(4,4)))
    print(str(Combination(10,0)))
if __name__=='__main__':
    main()