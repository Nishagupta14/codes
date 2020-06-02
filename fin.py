def fin(s,c):
    i =0
    while(i < len(s)):
        if s[i] == c:
            print(i)
            return
        else:
            pass
        i += 1
    print("not present")
s = input()
c = input()
fin(s,c)