def multChar(string):
    outlist = []
    for i in list(string):
        outlist.append(i*3)
    return "".join(outlist)

def getBert(string):
    low = string.lower()
    lowlist = low.split('bert')
    if len(lowlist) != 3:
        return ""
    else:
        offstart = 4 + len(lowlist[0])
        offend = 4 + len(lowlist[2])
        Bert = string[-(offstart+1):offend-1:-1]
        return Bert

def evenlySpaced(a,b,c):
    s = sorted([a,b,c])
    if s[2]-s[1] == s[1]-s[0]:
        return True
    else:
        return False

def nMid(string,a):
    s = int((len(string)-a)/2)
    start = string[:(s)]
    end = string[-s:]
    return start+end
