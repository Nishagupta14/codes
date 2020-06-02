def revers(s):
    new_s =""
    i = len(s)-1
    while(i>=0):
        new_s +=s[i]

        i -=1
    return new_s
s = input()
print(revers(s))