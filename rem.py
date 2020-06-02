def rem(s):
    new_s=" "
    for i in s:
        if i in "aeiouAEIOU":
            pass
        else:
            new_s +=i
    print(new_s)
s= input()
rem(s)