def reverseString(string):
    if string=="":
        return string
    else:
        return reverseString(string[1:])+ string[0]
def main():
    print(reverseString('I am Linh'))
if __name__=='__main__':
    main()