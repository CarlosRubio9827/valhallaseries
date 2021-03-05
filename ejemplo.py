def jumpingOnClouds(c):
    i = 0
    x = 0
    for i in range(i, len(c)-2):
        print(i)
        if c[i+1] == 1:
            x+=1
            i+=2
            print("a")
        elif c[i+2] == 0:
            i+=3
            x+=1
            print("b")
        else:
            x+=1
            print("c")
        
    # print("================")
    return x
    

c = [0,0,1,0,0,1,0]

y = jumpingOnClouds(c)
print(y)