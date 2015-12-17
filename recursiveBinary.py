def Binary(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        return str(Binary(m//2))+str(m%2)
    
def main():
    print(Binary(8))
main()