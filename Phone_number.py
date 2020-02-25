#!/usr/bin/env python3.8
def create_phone_number(n):
    bracketed = n[0:3]
    middles = n[3:6]
    lasts = n[6:]    #Slice given array into 3 separate lists
    
    sbrack="".join(map(str,bracketed))
    smid="".join(map(str,middles))
    slast="".join(map(str,lasts))    #Convert separated arrays into strings
    
    phone_number = "("+sbrack+") "+smid+"-"+slast    #Concaternate strings with formatting
    return phone_number

my_number = [1,2,3,4,5,6,7,8,9,0]

print(create_phone_number(my_number))