def create_phone_number(n):
    bracketed = n[0:3]
    middles = n[3:6]
    lasts = n[6:]    #Slice given array into 3 separate lists
    
    sbrack="".join(map(str,bracketed))
    smid="".join(map(str,middles))
    slast="".join(map(str,lasts))    #Convert separated arrays into strings
    
    phone_number = "("+sbrack+") "+smid+"-"+slast    #Concaternate strings with formatting
    return phone_number