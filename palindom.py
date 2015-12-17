def reverseString(string):
    if string=="":
        return string
    else:
        return reverseString(string[1:])+ string[0]
def palindom(string):
    return string==reverseString(string)
def main():
    print(palindom('I am Linh'))
    print(palindom('abcdcba'))
if __name__=='__main__':
    main()