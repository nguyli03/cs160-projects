def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
def main():
    x=int(input('please choose a number the represent the index of \
    a number in the Fib sequence: '))
    print(fib(x))
if __name__=='__main__':
    main()
    