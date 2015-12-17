def toString(n,base):
    convertString='0123456789ABCDEF'
    if n < base:
        return str(n)
    if n> base:
        return toSTring(n//base,base)+convertString[n%base]
    